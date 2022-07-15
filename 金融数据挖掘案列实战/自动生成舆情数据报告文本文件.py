import requests
import re
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


def baidu(company):
    url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=' + company
    res = requests.get(url, headers=headers).text
    # print(res)

    p_href = '<div class="result-op c-container xpath-log new-pmd".*?<a class="source-link_Ft1ov" href="(.*?)"'
    href = re.findall(p_href, res, re.S)
    p_title = '<div class="result-op c-container xpath-log new-pmd".*?<div><!--s-data:{"title":"(.*?)"'
    title = re.findall(p_title, res, re.S)
    p_date = '发布于：(.*?)"'
    date = re.findall(p_date, res)
    p_source = '<span class="c-color-gray" aria-label="新闻来源：(.*?)"'
    source = re.findall(p_source, res, re.S)  # re.S参数用于自动处理换行   提取新闻来源

    for i in range(len(title)):  # range(len(title)),这里因为知道len(title) = 10，所以也可以写成for i in range(10)
        title[i] = title[i].strip()  # strip()函数用来取消字符串两端的换行或者空格，不过这里好像不太需要了
        title[i] = re.sub('<.*?>', '', title[i])  # 核心，用re.sub()函数来替换不重要的内容
        print(str(i + 1) + '.' + title[i] + '(' + date[i] + '-' + source[i] + ')')
        print(href[i])

    file1 = open('E:\\数据挖掘报告.txt', 'a')  # 如果把a改成w的话，则每次生成txt的时候都会把原来的txt清空，用w不太好，因为这样只能保留一家公司信息；如果出现乱码问题，则设置encoding参数为utf-8，写成file1 = open('E:\\数据挖掘报告.txt', 'a'，encoding='utf-8')
    #w写模式：每次写入新数据，都会清除与原来的数据
    #a追加模式：不清除原来的数据，在原来的数据之后写入新数据
    file1.write(company + '数据挖掘completed！' + '\n' + '\n')   #\n表示换行  write()函数把字符串写入文本文件中
    for i in range(len(title)):
        file1.write(str(i + 1) + '.' + title[i] + '(' + date[i] + source[i] + ')' + '\n')
        file1.write(href[i] + '\n')  # '\n'表示换行
    file1.write('——————————————————————————————' + '\n' + '\n')


companys = ['阿里巴巴', '万科集团', '百度集团', '腾讯', '京东']
for i in companys:
    baidu(i)
    print(i + '百度新闻爬取成功')

print('数据获取及生成报告成功')

