import requests
import re

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}

url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=阿里巴巴'  # 把链接中rtt参数换成4即是按时间排序，默认为1按焦点排序，3.4.1小节也有讲到
res = requests.get(url, headers=headers).text  # 加上headers用来告诉网站这是通过一个浏览器进行的访问
# print(res)

#正则提取
p_href = '<div class="result-op c-container xpath-log new-pmd".*?<a class="source-link_Ft1ov" href="(.*?)"'
href = re.findall(p_href, res, re.S)   #re.S参数用于自动处理换行   提取新闻网址
p_title = '<div class="result-op c-container xpath-log new-pmd".*?<div><!--s-data:{"title":"(.*?)"'
title = re.findall(p_title, res, re.S)   #re.S参数用于自动处理换行   提取新闻标题
p_news = '<span class="c-color-gray" aria-label="新闻来源：(.*?)"'
news = re.findall(p_news, res, re.S)   #re.S参数用于自动处理换行   提取新闻来源

# print(title)
# print(href)
# print(news)


for i in range(len(title)):  # range(len(title)),这里因为知道len(title) = 10，所以也可以写成for i in range(10)
    title[i] = title[i].strip()  # strip()函数用来取消字符串两端的换行或者空格，不过目前（2020-10）并没有换行或空格，所以其实不写这一行也没事
    title[i] = re.sub('<.*?>', '', title[i])  # 核心，用re.sub()函数来替换不重要的内容
    print(str(i + 1) + '.' + title[i] + '(' + news[i] + ')')  #因为i是数字，所以字符串拼接时要用str()函数进行转换，二i是从0开始的，所以写成(i+1)
    print(href[i])

