import requests
import re
import pymysql
import time

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}
def baidu(company):   #定义一个函数
    url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=阿里巴巴'  # 把链接中rtt参数换成4即是按时间排序，默认为1按焦点排序，3.4.1小节也有讲到
    res = requests.get(url, headers=headers, timeout=10).text  # 加上headers用来告诉网站这是通过一个浏览器进行的访问,timeout=10为访问超时设置(10即为代表10秒，超时会报异常）
    # print(res)

    # 正则表达式提取内容
    p_href = '<div class="result-op c-container xpath-log new-pmd".*?<a class="source-link_Ft1ov" href="(.*?)"'
    href = re.findall(p_href, res, re.S)
    p_title = '<div class="result-op c-container xpath-log new-pmd".*?<div><!--s-data:{"title":"(.*?)"'
    title = re.findall(p_title, res, re.S)
    p_date = '发布于：(.*?)"'
    date = re.findall(p_date, res, re.S)
    p_source = '新闻来源：(.*?)"'
    source = re.findall(p_source, res, re.S)

    # print(title)
    # print(href)
    # print(news)
    # 数据清洗及打印
    for i in range(len(title)):  # range(len(title)),这里因为知道len(title) = 10，所以也可以写成for i in range(10)
        title[i] = title[i].strip()  # strip()函数用来取消字符串两端的换行或者空格，不过这里好像不太需要了
        title[i] = re.sub('<.*?>', '', title[i])  # 核心，用re.sub()函数来替换不重要的内容
        if ('小时' in date[i]) or ('分钟' in date[i]) or ('今天' in date[i]):  # 下面这几行代码是对日期做了一个处理，如果包含小时或者分钟，就转为当天日期
            date[i] = time.strftime("%Y-%m-%d")
        else:
            date[i] = date[i]
        print(str(i + 1) + '.' + title[i] + '(' + date[i] + '-' + source[i] + ')')
        print(href[i])
    # 将数据存入数据库
    for i in range(len(title)):
        db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', port=3306, db='sys', charset='utf8')
        cur = db.cursor()
        sql = 'INSERT INTO test(company,title,href,date,source) VALUES (%s,%s,%s,%s,%s)'
        cur.execute(sql, (company, title[i], href[i], date[i], source[i]))
        db.commit()
        cur.close()
        db.close()


companys = ['华能信托', '阿里巴巴', '万科集团', '百度集团', '腾讯', '京东']
for company in companys:
    try:
        baidu(company)
        print(company + '爬取并存入数据成功')
    except:
        print(company + '爬取并存入数据失败')


