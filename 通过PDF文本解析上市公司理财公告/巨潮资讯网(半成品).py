import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import os
import random
from PyPDF2 import PdfFileReader
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
Chrome = Chrome(options=chrome_options)


# os.makedirs('D:\\公司年报')  #在D盘创建文件夹，若重复运行，注释此行

# 解析网址
def get_html_content(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36"
    }
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        r.encoding = 'utf-8'
        # print(r.content)
        return r.content
    else:
        return None


# 保存pdf
def report_save(url, pdf_name):
    report = get_html_content(url)
    path = "/Users/macbookair/Desktop:\\公司年报\\" + pdf_name + ".pdf"
    with open(path, 'wb') as f:
        f.write(report)
        f.close


# 获取年报页数
def get_num_pages(pdf_name):
    path = "/Users/macbookair/Desktop:\\公司年报\\" + pdf_name + ".pdf"
    reader = PdfFileReader(path)
    if reader.isEncrypted:
        reader.decrypt('')
    page_num = reader.getNumPages()
    return page_num


url = 'http://www.cninfo.com.cn/new/commonUrl/pageOfSearch?url=disclosure/list/search&checkedCategory=category_ndbg_szsh#sse'
Chrome.get(url)

# 修改财报公布日期期间
Chrome.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[2]/div[1]/div[2]/form/div[1]/div/div/i[1]').click()
Chrome.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[1]/button[7]').send_keys(Keys.ENTER)

items = []
count = 1
while count <= 1:
    count += 1
    time.sleep(2)
    all_tr = Chrome.find_element(By.XPATH,
        '//*[@id="main"]/div[2]/div[1]/div[1]/div[2]/div/div[3]/table/tbody').find_element(By.XPATH, './/tr')
    for tr in all_tr:
        item = {}
        a = random.random() * 3
        time.sleep(a)  # 设置随机休息
        number = tr.find_elements_by_xpath('./td')[0].find_element_by_xpath('.//span').text
        item['公司代码'] = number
        name_pre = tr.find_elements_by_xpath('./td')[1].find_element_by_xpath('.//span').text
        name = name_pre.replace('*', '')  # windows命名不能包含*，去除*
        item['公司名称'] = name
        title = tr.find_elements_by_xpath('./td')[2].find_element_by_xpath('.//a').text
        item['年报标题'] = title
        date = tr.find_elements_by_xpath('./td')[3].find_element_by_xpath('.//span').text
        item['年报发布日期'] = date
        year = str(int(date[0:4]) - 1)
        item['年报对应年份'] = year
        pdf_name = number + "-" + name + "-" + year  # 设置pdf命名
        print(pdf_name)
        handle_main = browser.current_window_handle  # 句柄
        tr.find_elements_by_xpath('./td')[2].find_element_by_xpath('.//a').send_keys(Keys.ENTER)  # 点击进入网页
        if len(browser.window_handles) > 1:
            for handle in browser.window_handles:
                if handle != handle_main:
                    browser.switch_to.window(handle)  # 切换到新句柄
                    pdf_href = browser.find_element_by_xpath(
                        '//*[@id="noticeDetail"]/div/div[2]/div[1]/a').get_attribute('href')  # 获取pdf网址
                    print(pdf_href)
                    report_save(pdf_href, pdf_name)
                    browser.close()
        Chrome.switch_to.window(handle_main)  # 切换回主句柄
        page_num = get_num_pages(pdf_name)
        print(page_num)
        item['年报页数'] = page_num
        items.append(item)

    if Chrome.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[1]/div[3]/div/button[2]').get_attribute(
            'disabled') == 'disabled':
        break
    Chrome.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[1]/div[3]/div/button[2]/i').click()

df = pd.DataFrame(items)
df.to_excel(r'/Users/macbookair/Desktop//公司年报/上市公司年报.xlsx')

