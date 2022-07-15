from selenium import webdriver
import re
import time


def dongfang(company):
    #browser = webdriver.Chrome()  # 这里改成了有界面模式，方便调试代码
    chrome_options = webdriver.ChromeOptions()  #下面三行代码是无界面模式
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    url = 'http://so.eastmoney.com/news/s?keyword=' + company
    browser.get(url)
    time.sleep(3)
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

