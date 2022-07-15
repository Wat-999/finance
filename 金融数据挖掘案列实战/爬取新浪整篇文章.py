import time
import requests
from bs4 import BeautifulSoup
info = requests.get('http://news.sina.com.cn/w/2018-09-04/doc-ihiixzkm4326136.shtml')
info.encoding = 'utf-8'
html = BeautifulSoup(info.text, 'html.parser')

print(html.select('.second-title')[0].text)#获取大标题
print(html.select('.date')[0].text)#获取发布时间
#dt = time.strptime(timesource, '%Y年%m月%d日 %H:%M') #用来格式化时间字符串为时间格式方便储存
#dt.strftime('%Y-%m-%d')
print(html.select('.source')[0].text + '  '+html.select('.source')[0]['href'])
article = []
for v in html.select('.article p')[:-1]:#获取article中被p包含的内容去除最后一个p标签即责任编辑
    article.append(v.text.strip())#将内容添加到列表中，并去除两边特殊字符
author_info = '\n'.join(article)#将列表中内容以换行连接
print(author_info)
print(html.select('.show_author')[0].text.lstrip(u'责任编辑：'))#输出编辑姓名