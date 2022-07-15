#东方财富网是一家专业的互联网财经媒体，提供7X24小时财经资讯及全球金融市场报价。通过requests库来访问，加上headers也无法获取网页源代码

#获取网页源代码
from selenium.webdriver import Chrome
from selenium import webdriver
import re
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
Chrome = Chrome(options=chrome_options)#启动chromedriver
Chrome.get('https://so.eastmoney.com/news/s?keyword=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4')#打开http://www.baidu.com
data = Chrome.page_source
#print(data)  #运行结果，按command+F键搜索python，确实获取到来网页源代码
Chrome.quit()  #退出模拟浏览器

#编写正则式
p_title = '<div class="news_item_t".*?<a href=".*?">(.*?)</a>'
p_href = '<div class="news_item_t".*?<a href="(.*?)".*?</a>'
p_date = '<span class="news_item_time">(.*?)</span>'
title = re.findall(p_title, data, re.S)
herf = re.findall(p_href, data, re.S)
date = re.findall(p_date, data, re.S)
#检查爬取到到内容，及检查列表元素到数量
print(title)
print(len(title))
print(herf)
print(len(herf))
print(date)
print(len(date))

#数据清洗打印输出
#数据清洗相对较容易。新闻标题里有一些类似<em>的符号，可以用sub函数进行替换，新闻日期里有一些不需要的时间摘要等内容
#他们中间通过空格分隔，可以用split()函数进行分割
for i in range(len(title)):
    title[i] = re.sub('<.*?>', '', title[i])
    date[i] = date[i].split(' ')[0]
    print(str(i + 1) + '.' + title[i] + ' - ' + date[i])
    print(href[i])

#函数定义及使用
url = 'http://so.eastmoney.com/news/s?keyword=' + company
Chrome.get(url)
#再补上异常处理模块，完整代码如下：
from selenium import webdriver
import re


def dongfang(company):
    browser = webdriver.Chrome()  # 这里改成了有界面模式，方便调试代码
    url = 'http://so.eastmoney.com/news/s?keyword=' + company
    browser.get(url)
    data = browser.page_source
    browser.quit()
    # print(data)  # 如果正则发生变化，可以通过打印源代码进行调试

    p_title = '<div class="news_item_t".*?<a href=".*?">(.*?)</a>'
    p_href = '<div class="news_item_t".*?<a href="(.*?)".*?</a>'
    p_date = '<span class="news_item_time">(.*?)</span>'
    title = re.findall(p_title, data)
    href = re.findall(p_href, data)
    date = re.findall(p_date, data, re.S)


    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i])
        date[i] = date[i].split(' ')[0]
        print(str(i+1) + '.' + title[i] + ' - ' + date[i])
        print(href[i])


#dongfang('贵州茅台')  # 可以通过它来调试，如果没问题，再通过下面的代码批量运行

companys = ['华能信托', '阿里巴巴', '腾讯', '京东', '万科']
for i in companys:
    try:
       dongfang(i)
       print(i + '该公司东方财富网爬取成功')
    except:
       print(i + '该公司东方财富网爬取失败')
