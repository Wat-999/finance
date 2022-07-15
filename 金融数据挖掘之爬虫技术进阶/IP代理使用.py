#讯代理操作说明
#1登录账号后，单击右上角的头像进入个人中心。
#2在左侧单击"我的订单"选项，在右侧界面中可看到购买的订单。
#3单击"生生API"链接，进入生成API的新页面(API是接口的意思，让用户可以连接到讯代理到IP代理池)
#4在弹出到生成API页面中选择刚才购买到订单
#5设置提取数量为1
#6在数据格式选项组中单击TXT单选按钮
#7单击生成API链接按钮
#8单击复制按钮，将API链接复制下来
#复制API链接后，可以先简单测试一下。把该链接粘贴到浏览器到地址栏中打开，网页中显示的IP地址就是所提取的一个IP地址。
#之前讲过，把IP代理地址部署到python程序中使用的是下面这几行代码。上面网页中显示的IP代理地址可以直接复制、粘贴到第2行代码中使用，但不建议这样做
#因为每次调用API链接后IP代理地址都会发生变化，并且每个IP代理地址还有使用时间限制(通常为30分钟到几小时），所以实战中会通过编写代码从网页源代码中提取IP代理地址来使用


#完整代码如下：
import requests  # 讯代理官网：http://www.xdaili.cn/
proxy = requests.get('http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=890fff42d97343ecbb39c346691044d9&orderno=YZ20225168198U2P78s&returnType=1&count=5').text
proxy = proxy.strip()  # 这一步非常重要，因为要把看不见的换行符等给清除掉
print(proxy)
proxies = {'http': 'http://'+proxy, 'https': 'https://'+proxy}
url = 'https://httpbin.org/get'
res = requests.get(url, timeout=10, proxies=proxies).text
print(res)