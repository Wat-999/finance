#舆情数据评分系统版本4——处理非相关信息
#舆情数据评分系统版本3已经很完善里，不过还有可以改进的地方。实际上，通过"article = requests.get(href[i], headers=headers, timeout=10).text"
#获得的是新闻网页的所有源代码，而这导致会有"误伤"，即本来是正面新闻，结果却被扣了分。之所以会产生这个问题，是因为有的网页中会有非相关的内容，如滚动新闻
#例如搜索"阿里巴巴"得到的一个新闻网页。我们关心的是左侧的新闻内容，可以看出对阿里巴巴来说这是一条正面新闻。右侧的"相关推荐"内容虽然与左侧新闻无关
#但是由于通过"article = requests.get(href[i], headers=headers, timeout=10).text"获取到的是网页上所有内容，所以右侧的"相关推荐"内容
#包含负面词，就会导致这条新闻内容被误判为阿里巴巴的负面新闻，解决这个问题要用到一个比较有技巧的办法，段落内容通常由<p></p>包围，
#而大部分网页段正文内容都包含在<p></p>中，再来看前面的"相关推荐"内容在网页源代码中的结构，发现它不是由<p></p>标签包围，而是有<li></li>标签包围
#利用这个规律便可以解决非相关信息对干扰问题：先用正则表达式提取所有<p></p>标签包围的内容，再利用'连接符'.join(列表名)的方式，
#把正则表达式获得的列表转换为字符串，再进行if判断。
#p_article = '<p>(.*?)</p>'
#article_main = re.findall(p_article, article)  #获取正文内容
#article = ''.join(article_main)  #将列表转换为字符串
#把这三行代码再结合舆情数据评分系统版本-根据正文内容评分，获得版本4

import requests
import re
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


'''舆情评分系统 - 通过新闻标题和新闻正文来进行评分'''
def baidu(company, page):
    num = (page - 1) * 10  # 参数规律是（页数-1）*10
    url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=' + company + '&pn=' + str(num)
    res = requests.get(url, headers=headers).text

    # print(res)

    # 正则表达式编写，这边为了代码简洁，只演示了标题和链接（正则更新）
    # 正则表达式提取内容
    p_href = '<div class="result-op c-container xpath-log new-pmd".*?<a class="source-link_Ft1ov" href="(.*?)"'
    p_title = '<div class="result-op c-container xpath-log new-pmd".*?<div><!--s-data:{"title":"(.*?)"'
    p_date = '发布于：(.*?)"'
    p_source = '新闻来源：(.*?)"'
    href = re.findall(p_href, res, re.S)
    title = re.findall(p_title, res, re.S)
    date = re.findall(p_date, res, re.S)
    source = re.findall(p_source, res, re.S)

    # 舆情评分版本4
    score = []
    keywords = ['违约', '诉讼', '兑付', '阿里', '百度', '京东', '互联网']  # 这个关键词列表可以自己定义，
    for i in range(len(title)):
        num = 0
        # 获取新闻正文
        try:
            article = requests.get(href[i], headers=headers, timeout=10).text
        except:
            article = '爬取失败'
        # 解决可能存在的乱码问题
        try:
            article = article.encode('ISO-8859-1').decode('utf-8')  # 方法3
        except:
            try:
                article = article.encode('ISO-8859-1').decode('gbk')  # 方法2
            except:
                article = article  # 方法1
        # 只筛选真正的正文内容，旁边的滚动新闻之类的内容忽略
        p_article = '<p>(.*?)</p>'  # 有的时候p标签里还有class等无关内容，所以更严谨的写法是<p.*?>(.*?)</p>
        article_main = re.findall(p_article, article)  # 获取<p>标签里的正文信息
        article = ''.join(article_main)  # 将列表转换成为字符串
        for k in keywords:
            if (k in article) or (k in title[i]):   #根据正文和标题进行评分
                num -= 5
        score.append(num)

    for i in range(len(title)):
        title[i] = title[i].strip()  # strip()函数用来取消字符串两端的换行或者空格，不过目前（2020-10）并没有换行或空格，所以其实不写这一行也没事
        title[i] = re.sub('<.*?>', '', title[i])  # 核心，用re.sub()函数来替换不重要的内容
        print(str(i + 1) + '.' + title[i] + '(' + date[i] + '-' + source[i] + ')')
        print(company + '该条新闻舆情评分为' + str(score[i]))  # 这边注意，不要写score[i]，因为它是数字，需要通过str()函数进行字符串拼接
        print(href[i])
    print('——————————————————————————————')  # 这个是当分隔符使用


companys = ['阿里巴巴', '万科集团', '百度']
for company in companys:
    for i in range(10):  # 这里一共爬取了10页
        baidu(company, i+1)  # i是从0开始的序号，所以要写成i+1表示第几页
        print(company + '第' + str(i+1) + '页爬取成功')  # i是从0开始的序号，所以写i+1
        time.sleep(3)  # 不要爬太快，爬太快会被百度反爬





