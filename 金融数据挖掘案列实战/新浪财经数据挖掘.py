import requests  #网页链接源定位有问题
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

def xinlang(company):
    url = 'https://search.sina.com.cn/?c=news&ie=utf-8&q=' + company + '&range=all&c=news&sort=time&ie=utf-8'

    res = requests.get(url, headers=headers, timeout=10).text

    print(res)

    p_href = '<h2><a href="(.*?)"'
    p_title = '<h2>.*?>(.*?),'
    p_date = '<h2><span.*?>(.*?)</h2>'
    #p_source = '<h2><span class="fgray_time">(.*?)  </h2>'
    href = re.findall(p_href, res, re.S)
    title = re.findall(p_title, res, re.S)
    date = re.findall(p_date, res, re.S)
    #source = re.findall(p_source, res, re.S)
    # print(title)
    # print(href)
    # print(date)

    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i])

        print(str(i + 1) + '.' + title[i] + '(' + date[i] + ')')
        print(href[i])

# xinlang('京东')  # 可以通过这个来调试


companys = ['阿里巴巴', '万科集团', '百度', '腾讯', '京东']
for i in companys:
    try:
        xinlang(i)
        print(i + '新浪财经新闻获取成功')
    except:
        print(i + '新浪财经新闻获取失败')


