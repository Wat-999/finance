#数据去重
#因为数据库不能自动识别重复信息，所以同样的内容很有可能被重复存入数据库。过多的重复数据不仅浪费空间，而且会给数据提取造成很多麻烦。
#数据去重的思路：爬取到一条新闻数据的数据后，先查询数据库，如果发现该新闻的标题已经存在，就不把该新闻存入数据库
import requests

sql_1 = 'SELECT * FROM teest WHERE company = %s'     #按公司名称选取数据
cur.execute(sql_1, company)    #执行sql语句，选取公司名称为company的数据
data_all = cur.fetchall()   #提取所有数据
title_all = []    #创建一个空列表用来存储新闻标题
for j in range(len(data_all)):
    title_all.append(data_all[j][1])    #将数=数据中的新闻标题存入列表
#上述代码和之前在数据库中查询数据的代码基本一致，唯一的变化在于这里创建了一个空列表title_all,并使用apeend()函数将每条新闻标题存入该列表
#。因为data_all得到的是一个大元组(和指定的某家公司相关的所有新闻信息)，若要提取其中各个小元组(每条新闻的各项数据)的第二个元素(新闻标题）
#就得利用从data_all[j][1]的方式完成(data_all[j],提取小元组，data_all[j][1]提取小元组的第二个元素）。之前写for i in range(len(title))
#已经用过一次变量i了，所以这里最好用j作为变量。
#这里的for循环还有一种写法，即直接写for j in data_all,这样每一个j就不再是数字，而是data_all这个大元组中的一个小元组，j[1]就是小元组中的新闻标题
for j in data_all:
    title_all.append(j[1])
#获取到数据库中存储的每条新闻标题后，就可以对新爬取到的新闻进行筛选了。只需要判断新爬取到的新闻标题是在在title_all列表里，
#如果不在，说明它确实是一条新的新闻，可以存入数据库
if title_all[i] not in title_all:    #判断是否为新的新闻，是的话存入数据库
    sql_2 = 'INSERT INTO teest(company,title,href,source,data) VALUES (%s,%s,%s,%s,%s)'
    cur.execute(sql_2, (company, title[i], href[i], source[i], date[i]))
    db.commit()    #提交修改
#这里使用的是not in逻辑判断，就是"不在的意思"，即如果新爬取到的新闻标题不在数据库已有的数据里，那么就执行下面的存入数据库的操作

#把查询数据、筛选数据和插入数据汇总：
import pymysql
for i in range(len(title)):
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', port=3306, db='sys', charset='utf8')
    cur = db.cursor()  #获取会话指针，用力啊调用sql语句

    #1.查询数据
    sql_1 = 'SELECT * FROM teest WHERE company = %s'  # 按公司名称选取数据
    cur.execute(sql_1, company)  # 执行sql语句，选取公司名称为company的数据
    data_all = cur.fetchall()  # 提取所有数据
    title_all = []  # 创建一个空列表用来存储新闻标题
    for j in range(len(data_all)):
        title_all.append(data_all[j][1])  # 将数数据中的新闻标题存入列表

    #2.判断新爬取到的数据是否已在数据库中，不在的话才将数据存入
    if title_all[i] not in title_all:  # 判断是否为新的新闻，是的话存入数据库
        sql_2 = 'INSERT INTO teest(company,title,href,source,data) VALUES (%s,%s,%s,%s,%s)'
        cur.execute(sql_2, (company, title[i], href[i], source[i], date[i]))
        db.commit()  # 提交修改
        cur.close()  #关闭会话指针
        db.close()   #关闭数据库连接


#常见的数据清洗手段积日期格式统一
#1.用strip()函数删除空格及换行符等非相关符号
res = ' 华能信托2018年实现利润32.05亿元，行业排名第四    '
res.strip()  #删除上面字符串首尾的空格
#2用split()函数截取需要的内容
date = '2019-01-20 10:10:10'
date = data.split('')[0]  #提取年月日信息
#3用sub()函数进行内容替换
import re
title = '阿里<em>巴巴<em\>人工智能再发力'
title = re.sub('<.*?>', '', title)  #将形式为<xxxx>的内容替换为空值
#利用这些常规的数据清洗手段，已经可以对标题、网址等信息进行一轮处理。这里以"2019-01-20"的格式作为统一的标准。
#那么对于"2019-01-20 10:10:10"这样的日期格式，可以利用split()函数来截取前半部分；对于"2019年01月14日"这样的日期格式，可以利用sub()函数
#将"年""月"替换为"-"号，将"日"字符替换为空字符，即删除；对于"4小时前""58分钟前"这样的日期格式，处理方法也不复杂，只要包含"小时"或"分钟"的日期统一替换为今天的日期即可
import time
for i in range(len(title)):
    date[i] = date[i].split('')[0]  #处理带具体时分秒的日期
    date[i] = re.sub('年', '-', date[i])
    date[i] = re.sub('月', '-', date[i])
    date[i] = re.sub('日', '', date[i])
    if ('小时' in date[i]) or ('分钟' in date[i]):   #包含"小时"或"分钟"的日期
        date[i] = time.strftime("%Y-%m-%d")   #统一替换为今天的日期
    else:
        date[i] =date[i]
#通过time.strftime("%Y-%m-%d")获得当天的标准格式的日期，利用in逻辑判断条件实现如果出现"小时'或"分钟"则替换为今天的日期。
#如果想更加简洁，可以把这几行代码写到for i in range(len(title))循环代码里

#文本内容深度过滤——剔除噪声数据
#因为数据来自网络，所以经常会获取到一些噪声数据。例如，搜索"红豆集团"，结果搜出来"王菲经典歌曲红豆再登怀旧音乐榜榜首，这显然不是我们想要的。
#那么如何将这些噪声数据过滤掉呢第一种是根据新闻标题进行简单过滤，第二种则是根据新闻正文内容进行深度过滤

#1根据新闻标题进行简单过滤(比较粗暴）
#这种方法的思路是判断新闻标题是否包含要爬取公司的名称
for i in range(len(title)):
    if company not in title[i]:
        title[i] = ''
        href[i] = ''
        date[i] = ''
        source[i] = ''
while '' in title:   #遍历列表里所有的空字符串
    title.remove('') #删除列表元素，使用格式为：列表.remove(元素）
while '' in href:
    href.remove('')
while '' in date:
    date.remove('')
while '' in source:
    source.remove('')
#这里先遍历标题列表，如果标题不包含公司名称，则把相应的标题、网址、日期、来源都赋值为空值，然后批量删除列表中的空元素
#有的读者可能会感到疑惑：为什么不直接在for循环语句里用del title[i]的方式来删除元素，而是先将它赋值为空值再删除来？
#这是因为，如果在for循环语句里就把列表元素删除，len(title)并不会随之改变，即循环次数在for循环语句时便已经固定了。
#例如，列表原来有10个元素，列表元素被删除后剩下8个元素，那么此时的title[8]\title[9]就没有内容，会导致列表序号越界报错。
#所以需要先赋值为空值，然后通过while循环语句进行批量处理
#通过标题进行筛选，有时会过于粗放，因为有些新闻虽然标题里没有公司名称，但是在正文里有公司名称，这种新闻也是我们需要的

#根据新闻正文内容进行深度过滤
#我们之前已经获取到里每一条新闻的网址，那么只要补写如下一行代码就能轻松地进行正文爬取。其实就是通过Requests库来访问每一条新闻的网址，并获取相应的网页源代码
article = requests.get(href[i]).text  #获取新闻正文信息
#再加上headers来模拟浏览器访问网页，加上timeout来防止访问超时，还可以加上try/except
try:
    article = requests.get(href[i], headers=headers, timeout=10).text
except:
    atticle = '单个新闻爬取失败'

#再配合之前讲的数据清洗的方法
for i in range(len(title)):
    try:
        article = requests.get(href[i], headers=headers, timeout=10).text
    except:
        atticle = '单个新闻爬取失败'

    if company not in article:   #检查正文是否包含公司名称
        title[i] = ''
        href[i] = ''
        date[i] = ''
        source[i] = ''
    while '' in title:  # 遍历列表里所有的空字符串
        title.remove('')  # 删除列表元素，使用格式为：列表.remove(元素）
    while '' in href:
        href.remove('')
    while '' in date:
        date.remove('')
    while '' in source:
        source.remove('')
#现在可以通过新闻正文来筛选需要的新闻来，但是还有可以改进的地方。例如筛选下面两条新闻正文内容时，如果将公司名称设置为"华能信托"，
#那么第二条新闻就不符合判断标准，会被删除；而如果将公司名称设置为"华能贵诚信托"，则会导致第一条新闻被删除。然而"华能信托"和"华能贵诚信托"指的是同一家公司
#前者为简称，后者为全称，所以这两条新闻都是我们需要的
article1 = '华能信托2018年实现利润32.05亿元，行业排名第四'
article2 = '华能贵诚信托2018年实现利润32.05亿元，行业排名第四'
#此时可以把原来的判断条件代码if company not in article换成如下
company_re = company[0] + '.{0,5}' + company[-1]
if len(re.findall(company_re, article)) < 1:

#上述第一行代码中用了一个正则表达式，其中company_re 是匹配规则，company[0]表示公司名称的第一个字，company[-1]表示公司名称的最后一个字
#'.{0,5}'是个新知识点，"."表示任意一个字符，'.{0,5}'则表示任意0～5个任意字符(这里的逗号后一定不能有空格），所以company_re就是用来匹配
#"公司名称第一个字+0～5个任意字符+公司名称最后一个字"这样的字符串。如果公司名称较长，可以根据实际需要将5修改为稍大的数字
#然后通过re.findall(company_re, article)寻找满足匹配规则company_re的内容。如果能找到相关内容，则通过findall()获得的列表长度就大于1，
#如果没找到相关内容，则列表长度小于1，就可以执行将该新闻赋值为空值进行清除的操作了
#通过这样的判断条件，就能较精准地过滤和筛选正文。例如，把公司名称设置为"华能信托"，就能同时找到正文含有"华能信托"或"华能贵诚信托"的相关新闻


