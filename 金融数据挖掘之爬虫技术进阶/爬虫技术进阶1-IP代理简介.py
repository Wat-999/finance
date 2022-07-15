#IP代理的工作原理：IP代理就是IP地址伪装，把本机的IP地址伪装成其他IP地址。IP代理服务提供商一般拥有海量IP地址，这些海量IP地址被称为IP代理池
#我们购买IP代理服务后，所要做的就是在IP代理池里提取IP地址，然后写到自己的python程序里，这样就可以把自己的IP地址伪装成其他IP地址，从而躲过某些网站对于固定IP地址访问次数的限制

#IP代理的使用方法
import requests
proxy = 'IP代理地址'  #这个是需要购买的；这里以讯代理这个IP代理服务提供商为例
proxies = {"http": "http://"+proxy, "https": "https://"+proxy}
url = 'https://httpbin.org/get'
res = requests.get(url, headers=headers, timeout=10, proxies=proxies).text
#第二行代码中的IP代理地址需要替换为自己购买的IP代理地址
#第三行代码是配置IP代理地址的固定写法，其作用在于将IP代理地址配置到http和https协议上。
#第四行代码就是要访问的网址，这里设置为'https://httpbin.org/get'，因为它能够显示当前使用的IP地址，可以帮助我们查看IP代理地址是否调用成功
#第五行代码就是在访问具体网址时调用IP代理地址，其写法和之前设置headers=headers, timeout=10一样，只要再加上proxyies=proxyies即可

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
import requests
proxy = 'IP代理地址'  #这个是需要购买的；这里以讯代理这个IP代理服务提供商为例
proxies = {"http": "http://"+proxy, "https": "https://"+proxy}

#在浏览器中查看打开API链接所得网页到源代码，会发现只有两行内容，一行是IP代理地址，另一行是空行。因此，获取到网页源代码后，还要利用strip()函数
#清除其中到换行符和空格，才能得到我们需要到IP代理地址。

#从API链接到网页源代码中提取IP代理地址的代码如下：
proxy = requests.get('API链接').text
proxy = proxy.strip()  #这一步很重要，因为要把换行符等清除掉

#完整代码如下：
import requests
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}
proxy = requests.get('API链接').text
proxy = proxy.strip()  #这一步很重要，因为要把换行符等清除掉
proxies = {"http": "http://"+proxy, "https": "https://"+proxy}
url = 'https://httpbin.org/get'
res = requests.get(url, headers=headers, timeout=10, proxies=proxies).text
print(res)
#运行结果：在获取到网页源代码中，origin参数反映到就是IP地址，可以看到IP地址已经更换来，而不是本机地址。
#在实战中，偶尔会遇到IP地址反爬到网址，即通过固定IP地址访问次数过多就会拒绝访问到网址，只要以类似到方法设置requests.get()里的proxies参数，即可正常访问
