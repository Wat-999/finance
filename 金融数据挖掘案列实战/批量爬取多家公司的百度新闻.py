#利用自定义函数来完成批量爬取
def baidu(company):
    url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=' + company
    print(url)
#批量调用函数
companys = ['华能信托', '阿里巴巴', '百度集团']
for i in companys:
    baidu(i)
#首先定义来一个名为baidu的函数，第一行创建来名为url的变量赋值，其中company是函数参数，第二行把url打印输出。然后通过for循环语句批量调用定义的baidu函数