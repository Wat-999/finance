#之前爬取多百度新闻并不是按照时间排序的，这是因为百度新闻默认以"按焦点排序"的方式显示搜索结果，也就是把热点新闻放在最前面
#如果想按照时间顺序来获取新闻，只需要点击"按焦点排序"的下拉列表框里选择"按时间排序"
#此时按时间排序的网址为：https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=阿里巴巴
#之前按焦点排序的网址为：https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=阿里巴巴
#可以看到，它们唯一的区别就在于中间的"rtt="之后的数字，我们可以推断出"rtt=4"表示按照时间排序，"rtt=1"按照焦点排序。
#那么如果要写按照时间顺序爬取百度新闻的代码就很容易了，只要把之前代码里的url中"rtt=1"改成"rtt=4"
def baidu(company):
    url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=' + company

#一次性批量爬取多页内容
#其实批量爬取多页和按时间顺序爬取比较类似，都是在网址上做文章。先来看下用百度新闻搜索"阿里巴巴"得到的第一页内容的网址
#https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=阿里巴巴
#在第一页底部单击链接跳转到第二页，网址如下(删除来不影响跳转的内容）：
#https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=阿里巴巴&pn=10
#第三页
#https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=阿里巴巴&pn=20
#可以再多翻几页，对比一下网址，就能发现一个规律：从第二页开始，每个网址只有一个内容有变化，即&pn=xx，其等号后的数字呈现10、20、～～～～～的递增规律
#可以推断这个就是爬取多页的关键(猜测pn可能是page number的缩写）。有读者会问：第一页的网址中并没有"&pn=xx"的内容？
#其实在网址中，有些内容不是必需的，我们可以删除一些内容来试试看。网址中的参数通常通过&符号连接，所以删除参数也是根据&符号进行，
#例如上面的网址如果删去"&bsst=1"或"&c1=2"，仍然能访问。
#回到第一页的网址问题，按照前面发现的递增规律，猜测第一页的网址参数应该是"&pn=0"，可以构造出第一页的网址
##https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=阿里巴巴&pn=0
#将这个网址复制、粘贴到浏览器的地址栏中并打开，可以看到的确是第一页的内容，说明上述规律是有效的。
def baidu(page):
    num = (page - 1) * 10   # 参数规律是（页数-1）*10
    url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=阿里巴巴&pn=' + str(num)
    res = requests.get(url, headers=headers).text
    #此处省略是数据提取、清洗代码、注意缩进
for i in range(10):   #i是从0开始的序号，所以下面写成i+1
    baidu(i+1)
    print('第' + str(i+1), '页爬取成功')  #注意num、i是数字类型的变量，所以在做字符串拼接时要用str()函数进行转换

#2批量爬取多家公司的多页信息
def baidu(company, page):
    num = (page - 1) * 10
    url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=' + company + str(num)
    res = requests.get(url, headers=headers).text
    # 此处省略是数据提取、清洗代码、注意缩进

companys = ['阿里巴巴', '万科集团', '百度集团', '腾讯', '京东']
for company in companys:
    for i in range(20):
    baidu(company, i + 1)
    print(company + '第' + str(i + 1), '页爬取成功')


#知识点访问超时设置——timeout参数的使用
#有时访问一个网址，可能等待很久都没有反应，由于无法获得网页源代码，程序就会一直等待，呈现"假死"状态。为避免陷入无限等待中，需要设置访问超时
#也就是说，如果访问一个网址的等待响应时间超过指定秒数，就报出异常，停止访问。
#访问超时的设置方法非常简单，只要在 requests.get(url, headers=headers)中再加一个timeout=10(10代表10秒,可以改为自己想设定的秒数)
def baidu(company, page):
    num = (page - 1) * 10  # 参数规律是（页数-1）*10
    url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=' + company + str(num)
    res = requests.get(url, headers=headers, timeout=10).text
    # 此处省略是数据提取、清洗代码、注意缩进

companys = ['阿里巴巴', '万科集团', '百度集团', '腾讯', '京东']
for company in companys:
    for i in range(20):
        try:
            baidu(company, i + 1)
            print(company + '第' + str(i + 1), '页爬取成功')
        except:
            print(company + '第' + str(i + 1), '页爬取失败')

