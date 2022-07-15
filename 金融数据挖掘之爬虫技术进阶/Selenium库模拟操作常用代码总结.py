#总结一下用selenium库模拟键盘鼠标操作的常用代码
#1打开网页、浏览器窗口最大化及关闭网页
from selenium.webdriver import Chrome
chrome = Chrome()    #声明要模拟的浏览器是谷歌浏览器
chrome.get('https://www.baidu.com/')  #通过browser.get()函数访问网址
chrome.maximize_window()  #将模拟浏览器窗口最大化，用得比较少。
chrome.quit()   #关闭模拟浏览器

#2定位元素的两种方法
Chrome.find_element(By.XPATH, 'xpath内容')
Chrome.find_element(By.CSS_SELECTOR, 'css_selector内容')

#3模拟鼠标单击的两种方法
Chrome.find_element(By.XPATH, 'xpath内容').click()
Chrome.find_element(By.CSS_SELECTOR, 'css_selector内容').click()

#4模拟键盘输入内容的两种方法
Chrome.find_element(By.XPATH, 'xpath内容').send_keys('输入内容')
Chrome.find_element(By.CSS_SELECTOR, 'css_selector内容').send_keys('输入内容')

#5清空原有内容的两种方法
Chrome.find_element(By.XPATH, 'xpath内容').clear()
Chrome.find_element(By.CSS_SELECTOR, 'css_selector内容').clear()

#6获取网页真正的源代码
#法1
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
Chrome = Chrome()#启动chromedriver
Chrome.get('http://www.baidu.com')#打开http://www.baidu.com
Chrome.find_element(By.XPATH, '//*[@id="kw"]').send_keys('python') #在搜索框中输入python
Chrome.find_element(By.XPATH, '//*[@id="su"]').click()  #点击百度一下
data = Chrome.page_source
print(data)  #运行结果，按command+F键搜索python，确实获取到来网页源代码

#法2
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("https://www.baidu.com/")
time.sleep(3)  # 因为是点击按钮后跳转，所以最好休息3秒钟再进行源代码获取,如果是直接访问网站，则通常不需要等待。
data = browser.page_source
print(data)


#7无界面浏览器设置
#法1
from selenium import webdriver
from selenium.webdriver import Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome = Chrome(options=chrome_options)  # 参数名由chrome_options改成了options
chrome.get('https://stock.finance.sina.com.cn/hkstock/quotes/SSECOMP.html')#打开http://www.baidu.com
data = chrome.page_source
print(data)

#法2
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)  # 3.8以上参数名由chrome_options改成了options
browser.get('https://stock.finance.sina.com.cn/hkstock/quotes/SSECOMP.html')#打开http://www.baidu.com
data = browser.page_source
print(data)

#与requests库相比，selenium库的优势明显，不需要设置headers等参数就能非常方便地获取到一些requests库难以获取的网页源代码，而且能模拟键盘和鼠标操作
#写法也很简洁。有读者可能产生这样的疑问：既然selenium库这么厉害，为什么不对所有网站都用selenium库来爬取呢？这是因为，通过selenium库访问网站
#是相当于模拟人打开一个浏览器进行访问的，其访问速度比requests库慢很多，所以对于普通的网站，使用requests库来爬取，
#对于requests库无法获取网页源代码的复杂网站，再使用selenium库来爬取。