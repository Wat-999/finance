from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium import webdriver
import time
import re




def juchao(keyword):
    chrome_options = webdriver.ChromeOptions()  # 下面三行代码是无界面模式
    chrome_options.add_argument('--headless')
    Chrome = webdriver.Chrome(options=chrome_options)
    url = 'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=' + keyword
    Chrome.get(url)
    Chrome.maximize_window()  #将模拟浏览器窗口最大化，用得比较少。
    time.sleep(3)  #因为是单击按钮后跳转，所以最好等待几秒再获取源代码
    data = Chrome.page_source   #获取网页源代码
    #p_count = '<span class="total-box" style="">约(.*?)条.*?</span>'多的时候出现是约多少条
    # p_count = '<span class="total-box" style="">共(.*?)条.*?</span>'内容条数少的时候会出现共多少条
    p_count = '<span class="total-box" style="">(.*?)条.*?</span>'
    counts = re.findall(p_count, data)[0]
    count = counts.split(' ')[1]  # 加上这句代码是因为有的内容条数少的时候会出现共多少条，多的时候出现是约多少条
    pages = int(int(count) / 10)


    # 1.自动翻页获取源码源代码
    datas = []
    datas.append(data)  # 这边是把第一页源代码先放到datas这个列表里
    for i in range(2):  # 这边为了演示改成了range(3)，想爬全部的话改成range(pages)
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

keywords = ['理财', '纾困', '现金管理']
for i in keywords:
    try:
       juchao(i)
       print(i + '该公司巨潮资讯网网爬取成功')
    except:
        print(i + '该公司巨潮资讯网网爬取失败')
