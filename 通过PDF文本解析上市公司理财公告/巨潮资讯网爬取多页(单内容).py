from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium import webdriver
import time
import re
chrome_options = webdriver.ChromeOptions()  # 下面三行代码是无界面模式
chrome_options.add_argument('--headless')
Chrome = Chrome(options=chrome_options)
url = 'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=%E7%BA%BE%E5%9B%B0'
Chrome.get(url)
Chrome.maximize_window()  #将模拟浏览器窗口最大化，用得比较少。
time.sleep(3)  #因为是单击按钮后跳转，所以最好等待几秒再获取源代码
data = Chrome.page_source   #获取网页源代码
p_count = '<span class="total-box" style="">(.*?)条.*?</span>'
counts = re.findall(p_count, data)[0]
count = counts.split(' ')[1]  #加上这句代码是因为有的内容条数少的时候会出现共多少条，多的时候出现是约多少条
print(count)
#在获取公告总数时，一定记得在findall()最后写一个[0],因为findall()获取的是一个列表，仍然要写一个[0]来提取列表中的元素。
pages = int(int(count)/10)
 #计算总页数
#在计算总页数用到来两个int()函数，原因是：首先，利用findall()获取到的公告总数(存储在变量count中)在本质上是字符串，所以需要转换成数字后才能进行
#除法运算，其次，int(count)除以10之后可能会变成小数，但是总页数只能是整数，所以需要用int()函数将其转换成整数。

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
#把列表转换成字符串的代码为：'连接符'.join(列表名)。其中引号里的内容为列表各元素之间的连接符，这里选择空字符串作为连接符
Chrome.quit()   #退出模拟浏览器

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
    href[i] = 'http://www.cninfo.com.cn' + href[i] #因为爬取的网址缺少一个前缀'http://www.cninfo.com.cn'，所以使用字符串拼接来解决
    href[i] = re.sub('amp;', '', href[i])
    date[i] = date[i].strip()
    date[i] = date[i].split(' ')[0]   #用空格分割不需要的时间，提取年月日
    print(str(i + 1) + '.' + title[i] + ' - ' + date[i])
    print(href[i])

