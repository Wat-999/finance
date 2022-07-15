import requests
import re
import time
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


def baidu(company):
    url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=' + company
    res = requests.get(url, headers=headers).text
    # print(res)

    p_href = '<div class="result-op c-container xpath-log new-pmd".*?<a class="source-link_Ft1ov" href="(.*?)"'
    href = re.findall(p_href, res, re.S)
    p_title = '<div class="result-op c-container xpath-log new-pmd".*?<div><!--s-data:{"title":"(.*?)"'
    title = re.findall(p_title, res, re.S)
    p_date = '<span class="c-color-gray2 c-font-normal">(.*?)</span>'
    date = re.findall(p_date, res)
    p_news = '<span class="c-color-gray" aria-label="新闻来源：(.*?)"'
    news = re.findall(p_news, res, re.S)  # re.S参数用于自动处理换行   提取新闻来源

    for i in range(len(title)):  # range(len(title)),这里因为知道len(title) = 10，所以也可以写成for i in range(10)
        title[i] = title[i].strip()  # strip()函数用来取消字符串两端的换行或者空格，不过这里好像不太需要了
        title[i] = re.sub('<.*?>', '', title[i])  # 核心，用re.sub()函数来替换不重要的内容
        print(str(i + 1) + '.' + title[i] + '(' + news[i] + ')')
        print(href[i])
while True:  # 一直运行的意思
    companys = ['华能信托', '阿里巴巴', '万科集团', '百度集团', '腾讯', '京东']
    for i in companys:
        try:
            baidu(i)
            print(i + '百度新闻爬取成功')
        except:
            print(i + '百度新闻爬取失败')

    time.sleep(10800)  # 每3600秒运行一次，即3小时运行一次，注意缩进
#至此实现了24小时不间断地爬取多家公司的新闻数据。有的读者可能会有这样的疑问：这里只爬取了百度新闻的第一页，会错过其他重要新闻吗？答案是不会的
#因为这是24小时不间断爬取，所以只要出现新的新闻就可以捕捉到。又有读者疑问：这样一直爬取，会不会爬取到很多重复的新闻呢？答案是会的，
#不间断爬取的确会爬取到重复的内容，而如何进行数据去重，则需要用到数据库的相关知识
