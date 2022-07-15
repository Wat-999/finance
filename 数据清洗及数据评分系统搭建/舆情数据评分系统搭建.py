#有时除里新闻的标题、网址、日期、来源，还需要挖掘一些其他内容。例如，我们希望能够获取到每条新闻的评分，用于新闻筛选或深度分析。
#此时，就需要进行舆情数据评分系统的搭建。
#1舆情数据评分系统版本1——根据标题评分
score = []  #定义一个空列表
keywords = ['违约', '诉讼', '兑付', '阿里', '百度', '腾讯', '京东', '互联网']
#定义一个列表，其中存储的负面词清单，负面词可以根据自己的需要任意添加与删除，这里方便演示评分效果，放进里一些公司名称，实战中不会这么做
for i in range(len(title)):   #遍历每一条新闻标题
    num = 0                   #设定每一条新闻的初始评分都为0分
    for k in keywords:        #利用for循环语句和if判断语句计算新闻的评分
        if k in title[i]:
            num -= 5    #就是num = num - 5   即对于keywords列表中的每一个负面词，只要出现在标题中，就将评分减5分
    score.append(num)   #把评分添加到score列表中


#完整代码如下：
import requests
import re
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


# 爬取多个公司的多页, 可以给函数传入两个参数，供参考
def baidu(company, page):
    num = (page - 1) * 10  # 参数规律是（页数-1）*10
    url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=' + company + '&pn=' + str(num)
    res = requests.get(url, headers=headers).text

    # 正则表达式提取内容
    p_href = '<div class="result-op c-container xpath-log new-pmd".*?<a class="source-link_Ft1ov" href="(.*?)"'
    href = re.findall(p_href, res, re.S)
    p_title = '<div class="result-op c-container xpath-log new-pmd".*?<div><!--s-data:{"title":"(.*?)"'
    title = re.findall(p_title, res, re.S)
    p_news = '<span class="c-color-gray" aria-label="新闻来源：(.*?)"'
    news = re.findall(p_news, res, re.S)  # re.S参数用于自动处理换行   提取新闻来源

    # 1舆情数据评分系统版本1——根据标题评分
    score = []  # 定义一个空列表
    keywords = ['违约', '诉讼', '兑付', '阿里', '百度', '腾讯', '京东', '互联网']
    # 定义一个列表，其中存储的负面词清单，负面词可以根据自己的需要任意添加与删除，这里方便演示评分效果，放进里一些公司名称，实战中不会这么做
    for i in range(len(title)):  # 遍历每一条新闻标题
        num_s = 0  # 设定每一条新闻的初始评分都为0分
        for k in keywords:  # 利用for循环语句和if判断语句计算新闻的评分
            if k in title[i]:
                num_s -= 5  # 就是num = num - 5   即对于keywords列表中的每一个负面词，只要出现在标题中，就将评分减5分
        score.append(num_s)  # 把评分添加到score列表中

    for i in range(len(title)):  # range(len(title)),这里因为知道len(title) = 10，所以也可以写成for i in range(10)
        title[i] = title[i].strip()  # strip()函数用来取消字符串两端的换行或者空格，不过这里好像不太需要了
        title[i] = re.sub('<.*?>', '', title[i])  # 核心，用re.sub()函数来替换不重要的内容
        print(str(i + 1) + '.' + title[i] + '(' + news[i] + ')')
        print(href[i])
        print(company + '该条舆情评分为', + str(score[i]))


companys = ['阿里巴巴', '万科集团', '百度集团', '腾讯', '京东']
for company in companys:
    for i in range(10):  # 这里一共爬取了10页
        baidu(company, i+1)  # i是从0开始的序号，所以要写成i+1表示第几页
        print(company + '第' + str(i+1) + '页爬取成功')  # i是从0开始的序号，所以写i+1
        time.sleep(3)  # 不要爬太快，爬太快会被百度反爬
