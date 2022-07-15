'''2019年8月份之后裁判文书网改版，其反爬非常强，所以模拟键盘鼠标操作后等待很久也等不到刷新，
所以这里主要给大家练习下如何通过selenium库模拟键盘鼠标操作。'''

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import time
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
Chrome = Chrome(options=chrome_options)    #前三行，启动chromedriver,无界面浏览
#Chrome = Chrome()       #有界面浏览
Chrome.get('http://wenshu.court.gov.cn/')
Chrome.maximize_window()
Chrome.find_element(By.XPATH, '//*[@id="_view_1540966814000"]/div/div[1]/div[2]/input').clear()  # 清空原搜索框
Chrome.find_element(By.XPATH, '//*[@id="_view_1540966814000"]/div/div[1]/div[2]/input').send_keys('房地产')  # 在搜索框内模拟输入'房地产'三个字
Chrome.find_element(By.XPATH, '//*[@id="_view_1540966814000"]/div/div[1]/div[3]').click()  # 点击搜索按钮
time.sleep(20)  # 现在裁判文书网反爬非常厉害，所以可能等待也等不到刷新，所以这里主要给大家练习下模拟键盘鼠标操作
data = Chrome.page_source
Chrome.quit()
print(data)