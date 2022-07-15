#1获取网页源代码
import requests
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}
url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=阿里巴巴'
res = requests.get(url, headers=headers).text
print(res)


#2编写正则表达式提取新闻信息
#提取新闻的来源和日期
#观察网页源代码，会发现每条新闻的来源和发布日期都夹在<div class="result-op c-container xpath-log new-pmd"和</a>之间，
#因此用用<div class="result-op c-container xpath-log new-pmd"和</a>作为文本A和文本B，提取中间的来源和日期信息
import re
p_info = '<div class="result-op c-container xpath-log new-pmd"(.*?)</a>'
info = re.findall(p_info, res, re.S)   #re.S参数用于自动处理换行
print(info)
#可以看到获得的新闻来源和日期是混杂在一起的，而且夹杂着很多其他的东西，所以还需要对数据进行二次提炼

#提取新闻的网址和标题.*?代替不关心的内容
p_href = '<div class="result-op c-container xpath-log new-pmd".*?<a class="source-link_Ft1ov" href="(.*?)"'
href = re.findall(p_href, res, re.S)   #re.S参数用于自动处理换行   提取新闻网址
p_title = '<div class="result-op c-container xpath-log new-pmd".*?<div><!--s-data:{"title":"(.*?)"'
title = re.findall(p_title, res, re.S)   #re.S参数用于自动处理换行   提取新闻标题
p_news = '<span class="c-color-gray" aria-label="新闻来源：(.*?)"'
news = re.findall(p_news, res, re.S)   #re.S参数用于自动处理换行   提取新闻来源
print(href)
print(title)
print(news)
#可以看到提取的网址基本没有问题，而提取的标题并不完善。标题中间含有<em>和</em>等无效字符，此时就需要对数据进行清洗

#新闻标题清洗  strip()函数用来去掉不需要的空格和换行符，sub()函数用来清洗<em>和</em>
for i in range(len(title)):
    title[i] = title[i].strip()
    title[i] = re.sub('<.*?>', '', title[i])   #.*?可以代替文本A和文本B之间的所有的内容，所以<.*?>表示任何形式<xxxxx>的内容即清洗掉<em>和</em>
    print(title[i])


