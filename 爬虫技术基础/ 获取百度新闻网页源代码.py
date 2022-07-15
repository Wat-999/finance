import requests
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}
url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=阿里巴巴'
res = requests.get(url, headers=headers).text
print(res)


#headers参数提供的是网站访问者的信息
#headers中User-Agent(用户代理）表示是用什么浏览器访问的
#设置完headers之后，在通过requests.get()请求时需加上headers参数，这样就能模拟是在通过一个浏览器访问网站了
#User-Agent(用户代理）的获取，这里用的是谷歌浏览器，在地址栏中输入"chrome://version/"