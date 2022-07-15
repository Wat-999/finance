#所有代码汇总如下：
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium import webdriver
import time
import re
chrome_options = webdriver.ChromeOptions()  # 下面三行代码是无界面模式
chrome_options.add_argument('--headless')
Chrome = Chrome(options=chrome_options)

url = 'http://stockdata.stock.hexun.com/dzjy/index.aspx'
Chrome.get(url)
Chrome.maximize_window()  # 将模拟浏览器窗口最大化，用得比较少。
time.sleep(3)  # 因为是单击按钮后跳转，所以最好等待几秒再获取源代码



# 1.自动翻页获取源码源代码
data_all = pd.DataFrame()  #创建一个空列表用来汇总数据
for i in range(1):   # 页面数据总没有显示，只能手动填入页数

    Chrome.find_element(By.XPATH, '//*[@id="tradeTableMore"]').click()  # 点击展开更多
    time.sleep(3)

    Chrome.find_element(By.CSS_SELECTOR, '#tradeTable_page > table > tbody > tr > td > div > ul > li.next').click()  # 点击下一页
    time.sleep(3)  # 因为是单击按钮后跳转，所以最好等待几秒再获取源代码，防止页面没有加载完毕
    data = Chrome.page_source  # 获取网页源代码
    table = pd.read_html(data)[0]   #通过pandas库提取表格数据
    time.sleep(2)  # 防止没有加载完毕


    #添加股票代码
    p_code = '<a href="(.*?).shtml'
    code = re.findall(p_code, data)[0]
    table['股票代码'] = code  # 这里利用通过列表创建dataframe的方法将获取的code列表添加到已有的table表格中

    #通过concat()函数将各页的表格纵向拼接成一个总的dataframe
    data_all = pd.concat([data_all, table], ignore_index=True)  #设置ignore_index=True，以忽略原来的行索引

data_all.to_excel('大宗交易报告.xlsx', index=False)  #设置index为忽略原来的数字行索引
print('完成')

