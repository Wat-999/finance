#和讯研报网是和讯旗下专注于批露券商分析师研究报告(简称研报)信息的网站，本节的任务便是获取该网站上的券商研报数据，为之后的进一步分析做准备。
#和讯研报将研报分为不同的种类，如目标涨幅最大股、机构强烈推荐股等，这里以券商评级调升股为例进行相关数据的获取和分析。打开和讯研报网的"券商评级调升股"
#版块（http://yanbao.stock.hexun.com/ybsj5.shtml)

#表格数据的常规获取方法
#文件形式的表格数据——世界银行项目表：官网(https://datacatalog.worldbank.org/search/dataset/0037800)
#利用右键检查元素，可以发现其存储数据的csv文件的下载链接是固定的："https://search.worldbank.org/api/projects/all.csv"
#csv文件和excel工作簿都是用来存储数据的，不过csv文件不包含 格式、公式、宏等，所以所占空间通常比较小
#获取到下载链接之后，直接利用requests库访问该下载链接，及可下载csv文件

import requests
url = "https://search.worldbank.org/api/projects/all.csv"
res = requests.get(url)
file = open('世界银行项目表.csv', 'wb')  #可以修改文件保存路径
#open('文件路径'，'打开文件的模式')创建一个csv文件。这里设置的路径为相对路径(代码文件所在的文件夹)，也可以根据需要设置为绝对路径。
#需要注意的是，打开文件的模式要选择wb二进制模式，因为csv、excel、图片等文件都是以二进制模式进行文件读写的，然后利用writ()函数写入文件具体内容
file.write(res.content) #将数据的二进制形式写入文件
file.close()  #关闭文件

# 1.下载CSV数据文件
# 这个文件比较大下载时间较长，所以如果想尝试的话，可以先将下面的代码批量注释掉（都选中后ctrl+/进行注释），先运行下面的图片下载进行文件下载体验
import requests
url = 'http://search.worldbank.org/api/projects/all.csv'
res = requests.get(url)  # 只要能够获得下载链接，像Excel文件、图片文件都可以进行下载
file = open('世界银行项目表.csv', 'wb')  # 可以修改所需的文件保存路径，这里得选择wb二进制的文件写入方式
file.write(res.content)
file.close()  # 通过close()函数关闭open()函数打开的文件，有助于释放内存，是个编程的好习惯
print('世界银行项目表.csv下载完毕')

# 2.通过requests库还可以下载图片
import requests
url = 'http://images.china-pub.com/ebook8055001-8060000/8057968/shupi.jpg'
res = requests.get(url)  # 只要能够获得下载链接，像Excel文件、图片文件都可以进行下载
file = open('图片.jpg', 'wb')  # 这里采用的是相对路径，也即代码所在的文件夹
file.write(res.content)
file.close()  # 通过close()函数关闭open()函数打开的文件，有助于释放内存，是个编程的好习惯
print('图片.jpg下载完毕，并保存在代码所在的文件夹')


#2网页形式的表格数据——新浪财经大宗交易表
#有时表格数据是直接呈现在网页上的，如新浪财经数据中心的表格数据，我们便以它为例讲解网页形式表格数据的获取技巧，
#该技巧也会在获取和讯研报网的表格数据时发挥作用。
# 大宗交易针对的是一笔数额较大股票或债券交易，有时可以透漏出较强的交易信号。


import pandas as pd

url = 'http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/dzjy/index.phtml'  # 新浪财经数据中心提供股票大宗交易的在线表格
table = pd.read_html(url)[0]  # 通过pd.read_html(url)获取的是一个列表，所以仍需通过[0]的方式提取列表的第一个元素
#pd.read_html()函数可以获取该网页上的所有表格，并自动解析成dataframe类型的二维表格。得到的table是一个表格列表，网页上有几张表格，
#table中就有几个元素，需要注意的是通过pd.read_html(url)获取的是一个列表，所以仍需通过[0]的方式提取列表的第一个元素。
#如果如果网页上有多个表格，则按序号提取需要的表格
print(table)

print(table)
table.to_excel('大宗交易表.xlsx')  # 如果想忽略行索引的话，可以设置index参数为False

print('获取表格成功！')
#知识点
#大宗交易针对的是一笔数额较大的证券交易，其数额超过监管规定的成交量限额。大宗交易是场外交易，即不在二级市场直接交易，交易手续费和买股成本较低。
#每笔大宗交易的成交量、成交价、及买卖双方收盘后单独公布，不纳入指数计算，因此对于当天的股价无影响。大宗交易对股票未来走势的影响则需要分情况讨论
#如果大宗交易是因为大股东减持，可能是因为大股东不看好该上市公司未来的股票走势，从而抛售股票，那么该股票下跌的可能性较大。
#如果是因为炒家，也就是常说的庄家在通过大宗交易吸收筹码(通常大宗交易吸筹成本低于在二级市场直接进行股票交易），那么未来一段时间例，股票就可能会有一波强劲上扬走势


#用selenium库爬取和讯研报网表格数据
#对于和讯研报网来说，用pd.read_html()函数解析表格会被网站拒绝访问，这是就需要利用selenium库来访问网页并获取网页源代码，然后使用pd.read_html()函数来解析

from selenium import webdriver
#设置无界面模式
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)
#访问网页并获取网页源代码
url = 'http://stockdata.stock.hexun.com/dzjy/index.aspx'
browser.get(url)
data = browser.page_source

#获取网页代码后，利用pd.read_html()函数解析表格
import pandas as pd
table = pd.read_html(data)[0]   #该表格是网页上的第一张表格，所以用data[0]来提取
#此时表格数据已经比较完善来，不过还需要获得每只股票的代码，因为只有通过股票代码才能利用Tushare库查询股票信息。
#在网页源代码观察中，发现网页源代码是含有股票代码的，可以用正则表达式提取股票代码：
import re
p_code = '<a href="(.*?).shtml'
code = re.findall(p_code, data)
table['股票代码'] = code       #这里利用通过列表创建dataframe的方法将获取的code列表添加到已有的table表格中

#新的table包含大宗交易信息版块第一页的表格数据，如果想获取所有页的表格数据，可以通过for循环语句来实现，
#先通过翻页观察网址的变化，发现其表达为如下格式：
#所有代码汇总如下：  (获取股票代码编号正则提取有问题）
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium import webdriver
import time
import re
chrome_options = webdriver.ChromeOptions()  # 下面三行代码是无界面模式
chrome_options.add_argument('--headless')
Chrome = Chrome(options=chrome_options)

url = 'http://stockdata.stock.hexun.com/dzjy/index.aspx'
Chrome.get(url)
Chrome.maximize_window()  # 将模拟浏览器窗口最大化，用得比较少。
time.sleep(3)  # 因为是单击按钮后跳转，所以最好等待几秒再获取源代码



# 1.自动翻页获取源码源代码
data_all = pd.DataFrame()  #创建一个空列表用来汇总数据
for i in range(1):   # 页面数据总没有显示，只能手动填入页数

    Chrome.find_element(By.XPATH, '//*[@id="tradeTableMore"]').click()  # 点击展开更多
    time.sleep(3)

    Chrome.find_element(By.CSS_SELECTOR, '#tradeTable_page > table > tbody > tr > td > div > ul > li.next').click()  # 点击下一页
    time.sleep(3)  # 因为是单击按钮后跳转，所以最好等待几秒再获取源代码，防止页面没有加载完毕
    data = Chrome.page_source  # 获取网页源代码
    table = pd.read_html(data)[0]
    time.sleep(2)  # 防止没有加载完毕


    #添加股票代码
    p_code = '<a href="(.*?).shtml'
    code = re.findall(p_code, data)[0]
    table['股票代码'] = code  # 这里利用通过列表创建dataframe的方法将获取的code列表添加到已有的table表格中

    #通过concat()函数将各页的表格纵向拼接成一个总的dataframe
    data_all = pd.concat([data_all, table], ignore_index=True)

data_all.to_excel('大宗交易报告.xlsx', index=False)
print('完成')

