#巨潮资讯网是中国证券监督管理委员会指定的上市公司信息批露网站，创建于1995年，是国内最早的证券信息专业网站，也是国内首家全面批露深沪3000多家公司
#公告信息和市场数据的大型证券专业网站。
#用requests库获取不来网页源代码，才使用selenium库
#如果在有界面浏览器模式下可以看到，并没有出现页面加载的过程，就可以不需要添加time.sleep()进行等待

from selenium import webdriver
import re
import time


def juchao(keyword):
    # browser = webdriver.Chrome()  # 这里改成了有界面模式，方便调试代码
    chrome_options = webdriver.ChromeOptions()  # 下面三行代码是无界面模式
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    url = 'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=' + keyword
    browser.get(url)
    time.sleep(3)  #等待时间设置
    data = browser.page_source
    # print(data)
    browser.quit()

    # 巨潮网网页结构调整后的正则表达式代码（2019-12-31日改）
    p_title = '<span title="" class="r-title">(.*?)</span>'
    p_href = '<a target="_blank" href="(.*?)" data-id='
    p_date = '<span class="time">(.*?)</span>'
    title = re.findall(p_title, data)
    href = re.findall(p_href, data)
    date = re.findall(p_date, data, re.S)  # 注意(.*?)中有换行（/n），而常规的(.*?)匹配不了换行，所以需要加上re.S取消换行的影响

    for i in range(len(title)):
        title[i] = re.sub(r'<.*?>', '', title[i])
        href[i] = 'http://www.cninfo.com.cn' + href[i]  #因为爬取的网址缺少一个前缀'http://www.cninfo.com.cn'，所以使用字符串拼接来解决
        href[i] = re.sub('amp;', '', href[i])      #爬取到的网址有多余的字符串'amp;'利用sub()函数将其替换为空值
        date[i] = date[i].strip()  # 清除空格和换行符
        date[i] = date[i].split(' ')[0]  # 只取“年月日”信息，不用“时分秒”信息，用空格分割不需要的时间，提取年月日
        print(str(i + 1) + '.' + title[i] + ' - ' + date[i])
        print(href[i])


keywords = ['理财', '现金管理', '纾困']
for i in keywords:
    try:
       juchao(i)
       print(i + '该公司巨潮资讯网网爬取成功')
    except:
        print(i + '该公司巨潮资讯网网爬取失败')


