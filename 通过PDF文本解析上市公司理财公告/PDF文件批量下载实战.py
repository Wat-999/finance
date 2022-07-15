#爬取多页内容：一般常用的爬取多页的是修改网址参数的方法，但这种方法对巨潮资讯网不适用，因为在巨潮资讯网进行翻页操作时，网址并没有发生变化。
#此时可以利用selenium库模拟鼠标单击下一页按钮，并根据公告数量来确定模拟单击的次数，每单击一次就获取一下该页的源代码，最后把获取到的各页源代码存储到一个列表里。

#首先来完成自动模拟单击按钮的操作，只要获取到"下一页"按钮的xpath内容，就可以用selenium库模拟单击了。在网页上右击选择检查元素，然后在下一页
#按钮对应的源代码上右击，在弹出的快捷菜单中选择"copy-copy xpath"命令，再把复制的内容粘贴到代码里即可
import re

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import time
Chrome = Chrome()     #启动chromedriver
url = 'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=理财'
Chrome.get(url)
Chrome.maximize_window()  #将模拟浏览器窗口最大化，用得比较少。
time.sleep(3)  #因为是单击按钮后跳转，所以最好等待几秒再获取源代码
Chrome.find_element(By.XPATH, '//*[@id="fulltext-search"]/div/div[1]/div[2]/div[4]/div[2]/div/button[2]').click()  #点击下一页

#实现自动翻页后，接着要考虑如何计算总页数。总页数与搜索到到公告总数有关，因为每页显示10条公告，所以把公告总数除以10，就是总页数。
#公告总数显示在网页到右下角，利用检查观察源代码的规律，编写出提取公告总数的正则表达式如下：
p_count = '<span class="total-box" style="">约(.*?)条.*?</span>'

#获取公告总数和总页数的完整代码如下：

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import time
import re
Chrome = Chrome()     #启动chromedriver
url = 'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=理财'
Chrome.get(url)
Chrome.maximize_window()  #将模拟浏览器窗口最大化，用得比较少。
time.sleep(3)  #因为是单击按钮后跳转，所以最好等待几秒再获取源代码
data = Chrome.page_source   #获取网页源代码
p_count = '<span class="total-box" style="">约(.*?)条.*?</span>'
count = re.findall(p_count, data)[0]
#在获取公告总数时，一定记得在findall()最后写一个[0],因为findall()获取的是一个列表，仍然要写一个[0]来提取列表中的元素。
#print(count)
pages = int(int(count)/10)   #计算总页数
#在计算总页数用到来两个int()函数，原因是：首先，利用findall()获取到的公告总数(存储在变量count中)在本质上是字符串，所以需要转换成数字后才能进行
#除法运算，其次，int(count)除以10之后可能会变成小数，但是总页数只能是整数，所以需要用int()函数将其转换成整数。
print(pages)

#把自动翻页和获取总页数的代码写到一起，再添加代码，在每次翻页时都获取当页的源代码，并把每一页的源代码存储到datas列表中。
#这里为来严谨，引用了time库，每次翻页和获取该页的源代码之后都等待2秒及1秒，再进行下一步操作，代码如下：
datas = []  #建立一个空列表
datas.append(data)    #把获取的第一页源代码存储到datas列表里
for i in range(pages):
    Chrome.find_element(By.XPATH, '//*[@id="fulltext-search"]/div/div[1]/div[2]/div[4]/div[2]/div/button[2]').click()  # 点击下一页
    time.sleep(3)  # 因为是单击按钮后跳转，所以最好等待几秒再获取源代码
    data = Chrome.page_source  # 获取网页源代码
    datas.append(data)
    time.sleep(2)
#接下来需要完成的工作就是把datas列表转换成字符串，因为只有在字符串中才能进行正则表达式的操作，提取我们想要的各个页面的公告标题、网址、日期等信息
#把列表转换成字符串的代码为：'连接符'.join(列表名)。其中引号里的内容为列表各元素之间的连接符，这里选择空字符串作为连接符
alldata = ''.join(datas)

#之后只需要把提取标题、链接、及日期的正则表达式应用到汇总里所有页面源代码的alldatas中即可
# 巨潮网网页结构调整后的正则表达式代码（2019-12-31日改）
p_title = '<span title="" class="r-title">(.*?)</span>'
p_href = '<a target="_blank" href="(.*?)" data-id='
p_date = '<span class="time">(.*?)</span>'
title = re.findall(p_title, data)
href = re.findall(p_href, data)
date = re.findall(p_date, data, re.S)  # 注意(.*?)中有换行（/n），而常规的(.*?)匹配不了换行，所以需要加上re.S取消换行的影响

#所有代码汇总如下：
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium import webdriver
import time
import re
chrome_options = webdriver.ChromeOptions()  # 下面三行代码是无界面模式
chrome_options.add_argument('--headless')
Chrome = Chrome(options=chrome_options)
url = 'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=理财'
Chrome.get(url)
Chrome.maximize_window()  #将模拟浏览器窗口最大化，用得比较少。
time.sleep(3)  #因为是单击按钮后跳转，所以最好等待几秒再获取源代码
data = Chrome.page_source   #获取网页源代码
p_count = '<span class="total-box" style="">约(.*?)条.*?</span>'
count = re.findall(p_count, data)[0]
pages = int(int(count)/10)

# 1.自动翻页获取源码源代码
datas = []
datas.append(data)  # 这边是把第一页源代码先放到datas这个列表里
for i in range(3):  # 这边为了演示改成了range(3)，想爬全部的话改成range(pages)
    Chrome.find_element(By.XPATH,
                        '//*[@id="fulltext-search"]/div/div[1]/div[2]/div[4]/div[2]/div/button[2]').click()  # 点击下一页
    time.sleep(3)  # 因为是单击按钮后跳转，所以最好等待几秒再获取源代码，防止页面没有加载完毕
    data = Chrome.page_source  # 获取网页源代码
    datas.append(data)
    time.sleep(2)  # 防止没有加载完毕
alldata = "".join(datas)
Chrome.quit()

# 2.编写正则表达式
p_title = '<span title="" class="r-title">(.*?)</span>'
p_href = '<a target="_blank" href="(.*?)" data-id='
p_date = '<span class="time">(.*?)</span>'
title = re.findall(p_title, alldata)
href = re.findall(p_href, alldata)
date = re.findall(p_date, alldata, re.S)


# 3.清洗数据
for i in range(len(title)):
    title[i] = re.sub('<.*?>', '', title[i])
    href[i] = 'http://www.cninfo.com.cn' + href[i]
    href[i] = re.sub('amp;', '', href[i])
    date[i] = date[i].strip()
    date[i] = date[i].split(' ')[0]
    print(str(i + 1) + '.' + title[i] + ' - ' + date[i])
    print(href[i])



