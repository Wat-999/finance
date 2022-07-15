#相对而言，股票、期货、外汇的实时数据都是比较难以获取的，本节演示反爬。
#获取网页源代码
from selenium.webdriver import Chrome
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
Chrome = Chrome(options=chrome_options)#启动chromedriver
Chrome.get('https://stock.finance.sina.com.cn/hkstock/quotes/SSECOMP.html')#打开http://www.baidu.com
data = Chrome.page_source
print(data)  #运行结果，按command+F键搜索python，确实获取到来网页源代码
#Chrome.quit()  #退出模拟浏览器

#数据提取
#获取网页源代码之后，接着要做的就是提取数据，如提取实时的股价、涨跌幅、成交量等多个股票数据。
#首先利用右键检查元素，看看上证综合指数的源代码有没有什么规律，可以发现上证综合指数的id为id="mts_stock_hk_price"。
#id类似身份证号码，一个网页中的id一般不会重复，而price是价格的意思，可以推测id为price的网页元素就是股价。而class表示类别
#示例中上证综合指数在上涨，其class为up，所以推测up表示为上涨的类别，并进一步推测down表示下跌的类别。以一只下跌股为例进行验证，确实其class为down
#最终总结出股价的源代码规律如下所示：<div id="price" class="up/dowm">3093.70</div>
#假设我们只关心股价的数值，不关心其涨跌，可以编写出提取股价的正则表达式：
import re
p_price = '<div id="price" class=".*?">(.*?)</div>'
price = re.findall(p_price, data)
#进而编写出获取实时股价的完整代码如下：
from selenium.webdriver import Chrome
from selenium import webdriver
import re
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
Chrome = Chrome(options=chrome_options)#启动chromedriver
Chrome.get('https://finance.sina.com.cn/realstock/company/sh000001/nc.shtml')#打开http://www.baidu.com
data = Chrome.page_source
#print(data)  #运行结果，按command+F键搜索python，确实获取到来网页源代码
Chrome.quit()  #退出模拟浏览器
p_price = '<div id="price" class=".*?">(.*?)</div>'
price = re.findall(p_price, data)
print(price)
#运行结果，与在网页上看到的数据一致(该数据是实时变化的，稍微会有点变化)
#通过类似的方法可以获取新浪财经上证综合指数或股票的其他实时数据，只要把Chrome.get里的网址换成想爬取的网址，并相应修改正则表达式。
#另一种获取股票数据的方法是使用股票数据接口，如Tushare库。那么这里为什么还要通过爬虫来获取股票数据了？主要原因有三方面：一是为了练习selenium库的用法
#二是高阶的股票数据接口大多是收费的，二通过爬虫获取数据的成本则较低；三是有些数据的获取很难找到合适的数据接口，如期货实时数据，通过爬虫能比较容易地获取
