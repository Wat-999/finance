import requests
from bs4 import BeautifulSoup
import time
import json
import re
import pandas
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
def getnewcontent(url):
    result = {}
    info = requests.get(url)
    info.encoding = 'utf-8'
    html = BeautifulSoup(info.text, 'html.parser')
    result['title'] = html.select('.second-title')[0].text
    result['date'] = html.select('.date')[0].text
    result['source'] = html.select('.source')[0].text
    article = []
    for v in html.select('.article p')[:-1]:
        article.append(v.text.strip())
    author_info = '\n'.join(article)
    result['content'] = author_info
    result['author'] = html.select('.show_author')[0].text.lstrip('责任编辑：')
    newsid = url.split('/')[-1].rstrip('.shtml').lstrip('doc-i')
    commenturl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gj&newsid=comos-{}&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&thread=1&callback=jsonp_1536041889769&_=1536041889769'
    comments = requests.get(commenturl.format(newsid))
    regex = re.compile(r'(.*?)\(')#去除左边特殊符号
    tmp = comments.text.lstrip(regex.search(comments.text).group())
    jd = json.loads(tmp.rstrip(')'))
    result['comment'] = jd['result'] #获取评论数 加上['count']['total']代码报错
    return result
def getnewslink(url):
    test = requests.get(url)
    test2 = test.text.lstrip('newsloadercallback(')
    jd = json.loads(test2.rstrip(')\n'))
    content = []
    for v in jd['result']['data']:
        content.append(getnewcontent(v['url']))
    return content
def getdata():
    url = 'https://interface.sina.cn/news/get_news_by_channel_new_v2018.d.html?cat_1=51923&show_num=27&level=1,2&page={}&callback=newsloadercallback&_=1536044408917'
    weibo_info = []
    for i in range(1,3):
        newsurl = url.format(i)#字符串格式化用i替换{}
        weibo_info.extend(getnewslink(newsurl))
    return weibo_info
new_info = getdata()
df = pandas.DataFrame(new_info)
df.to_excel('weibonews.xlsx')
#将文件下载为excel表格 df.to_excel('weibonews.xlsx')