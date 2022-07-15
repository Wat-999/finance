#selenium库是一个自动化测试工具，能够驱动浏览器模拟人的操作，如鼠标单击、键盘输入等。通过selenium库能够比较容易地获取到网页的源代码，
#还可以进行网络内容的批量自动下载等。

#网络数据挖掘的难点
#本小节将解决爬虫技术难题：获取网页"真正"的源代码，或者说数据挖掘需要的源代码。例如，上海证券交易所的公开信息、新浪财经的股票行情实时数据等。
#用常规爬虫手段会发现获取到的网页源代码内容很少且没有用。因为这些网页上展示的信息是动态渲染出来的，而通过常规爬虫手段获取的则是未经渲染的信息，
#所以其中没有我们想要的信息。

#然后用常规爬虫手段，以requests(url).text的方式获取这个网页的源代码，然后按快捷键ctrl+F，在源代码中搜索刚才看到的指数数值，会发现搜索不到。
#通过右击选择检查可以看到的内容，为什么用python却爬取不到呢？这是因为通过右击选择检查看到的其实是网站动态渲染后的内容，
#它能够被常规手段爬取的信息很有限。一个快速验证的办法就是按command+option+u快捷键，所看到的网页源代码内容很少，也没有显示通过右击选择检查可以看到的内容，
#此时就可以判定通过右击选择检查看到的网页源代码是动态渲染后的结果。面对这种动态渲染的网页，在数据挖掘时就需要使用Selenium库，通过模拟人在浏览器
#中的操作，快速获取渲染后的网页源代码。

#模拟浏览器chromeDrive的下载与安装
#Selenium库安装完成之后，先来试着运行如下代码进行测试
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
#此时会看到通过python模拟打开了一个浏览器窗口，并打开了百度首页。窗口中会显示"chrome正受到自动测试软件的控制"的提示信息。

#selenium库的使用
#1访问及关闭网页、浏览器窗口最大化：通过如下代码，就可以访问网页了，相当于模拟人打开了一个浏览器，然后访问指定的网址。
from selenium import webdriver
browser = webdriver.Chrome()    #声明要模拟的浏览器是谷歌浏览器
browser.get('https://www.baidu.com/')  #通过browser.get()函数访问网址
browser.quit()   #关闭模拟浏览器
browser.maximize_window()  #将模拟浏览器窗口最大化，用得比较少。

#查找元素模拟鼠标和键盘操作
#selenium库还可以模拟人在浏览器中鼠标和键盘操作。要在刚才打开的百度首页的搜索框内输入'python'，然后单击"百度一下"按钮进行搜索，该怎么模拟实现呢？
#首先得知道如何查找查找。网页是由一个个元素构成的，搜索框和百度一下按钮都是网页上的元素，而要对元素进行操作，得先找到它们。
#查找元素主要有两种方法：xpath法和css_selector法
#xpath法
Chrome.find_element(By.XPATH, 'xpath内容')
#xpath是一个定位各个元素对手段，可以把xpath理解为这个元素对名字或id。按右键选择检查，利用"选择"(一个小箭头标志的)按钮选中搜索框，
#然后在搜索框对应的那一行源代码右击，在弹出的快捷菜单中选择"copy>copy xpath"命令，把复制的内容(搜索框的xpath内容是//*[@id="kw"]）
#粘贴到上面的代码里替换xpath内容即可
#自动在搜索框里输入内容的代码如下：
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
Chrome = Chrome()#启动chromedriver
Chrome.get('http://www.baidu.com')#打开http://www.baidu.com
Chrome.find_element(By.XPATH, '//*[@id="kw"]').send_keys('python')
#第5行代码，定位到搜索框，然后加入.send_keys('python') 就可以模拟在搜索框里输入"python"的效果了。运行之后便会自动用模拟浏览器打开百度并在
#搜索框中输入"python"关键词，如果搜索框里有默认文字，可使用如下代码清空默认文字，再通过send_keys()输入内容
Chrome.find_element(By.XPATH, '//*[@id="kw"]').clear()
#用同样的方法找到"百度一下"按钮的xpath内容为"//*[@id="su"]"，那么要模拟单击"百度一下"按钮，在之前的代码后面补上如下代码：
Chrome.find_element(By.XPATH, '//*[@id="su"]').click()
#这一行代码用Chrome.find_element(By.XPATH, '//*[@id="su"]').click()定位到"百度一下"按钮，然后通过click()模拟鼠标单击的操作，完整代码如下
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
Chrome = Chrome()#启动chromedriver
Chrome.get('http://www.baidu.com')#打开http://www.baidu.com
Chrome.find_element(By.XPATH, '//*[@id="kw"]').send_keys('python') #在搜索框中输入python
Chrome.find_element(By.XPATH, '//*[@id="su"]').click()  #点击百度一下

#2css_selector法
Chrome.find_element(By.CSS_SELECTOR, 'css_selector内容')
#css_selector法与#xpath法类似，括号里css_selector内容获取方法也和xpath类似，按右键选择检查，利用"选择"(一个小箭头标志的)按钮选中搜索框，
#然后在搜索框对应的那一行源代码右击，在弹出的快捷菜单中选择"copy>copy xpath"命令，把复制的内容(搜索框的xpath内容是'#kw'）
#粘贴到上面的代码里替换css_selector内容即可；完整代码如下：
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
Chrome = Chrome()#启动chromedriver
Chrome.get('http://www.baidu.com')#打开http://www.baidu.com
Chrome.find_element(By.CSS_SELECTOR, '#kw').send_keys('python')
Chrome.find_element(By.CSS_SELECTOR, '#su').click()#点击百度一下
#两种方法在本质上是一样的，有时用其中方法会失效，换成另一种方法就有效，所以必须两种方法都要掌握


#获取网页真正的源代码
#使用selenium库的主要目的就是获取原来难以获取的网页源代码，代码如下
data = browser.page_source
print(data)
#完整代码如下：
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
Chrome = Chrome()#启动chromedriver
Chrome.get('http://www.baidu.com')#打开http://www.baidu.com
Chrome.find_element(By.XPATH, '//*[@id="kw"]').send_keys('python') #在搜索框中输入python
Chrome.find_element(By.XPATH, '//*[@id="su"]').click()  #点击百度一下
data = Chrome.page_source
print(data)  #运行结果，按command+F键搜索python，确实获取到来网页源代码

#需要注意的是，通过单击按钮(如上面的"百度一下"按钮)跳转到新的网页时，
#有时新网页的加载需要一定时间，会导致直接执行Chrome.page_source获取不到新网页的源代码，这时就需要在单击按钮后等待几秒再获取源代码，如下
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import time
Chrome = Chrome()#启动chromedriver
Chrome.get('http://www.baidu.com')#打开http://www.baidu.com
Chrome.find_element(By.XPATH, '//*[@id="kw"]').send_keys('python') #在搜索框中输入python
Chrome.find_element(By.XPATH, '//*[@id="su"]').click()  #点击百度一下
time.sleep(5)  #因为是单击按钮后跳转，所以最好等待几秒再获取源代码
data = Chrome.page_source
print(data)  #运行结果，按command+F键搜索python，确实获取到来网页源代码

#如果是直接访问网址则通常不需要等待，利用Chrome.page_source便可获取源代码。用这个方法来试试之前难以获取的新浪财经上证综合指数网页
from selenium.webdriver import Chrome
Chrome = Chrome()#启动chromedriver
Chrome.get('https://stock.finance.sina.com.cn/hkstock/quotes/SSECOMP.html')#打开http://www.baidu.com
data = Chrome.page_source
print(data)  #运行结果，按command+F键搜索python，确实获取到来网页源代码
#运行结果，在获取的源代码里可以搜索到上证指数数值，说明获取成功

#4无界面浏览器设置
#有时希望程序在后台运行，不需要弹出模拟浏览器，就要用到chrome Headless方法，将浏览器转到后台运行而不显示出来。代码如下
#法一：
from selenium.webdriver import Chrome
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
Chrome = Chrome(options=chrome_options)#启动chromedriver
Chrome.get('https://stock.finance.sina.com.cn/hkstock/quotes/SSECOMP.html')#打开http://www.baidu.com
data = Chrome.page_source
print(data)  #运行结果，按command+F键搜索python，确实获取到来网页源代码
#法二：
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)  # 参数名由chrome_options改成了options
browser.get('https://stock.finance.sina.com.cn/hkstock/quotes/SSECOMP.html')#打开http://www.baidu.com
data = browser.page_source
print(data)
#运行之后发现，无需弹出模拟器就能渲染后的网页源代码。在selenium库的实战中一般都会启用无界面浏览器设置，因为通常不希望频繁弹出一个模拟浏览器窗口







