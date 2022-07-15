import pandas as pd
from selenium import webdriver
import re
browser = webdriver.Chrome()

data_all = pd.DataFrame()  # 创建一个空列表用来汇总所有表格信息
for pg in range(1, 2):  # 可以将页码调大，比如2019-04-30该天，网上一共有176页，这里可以将这个2改成176
    url = 'http://yanbao.stock.hexun.com/ybsj5_' + str(pg) + '.shtml'
    browser.get(url)  # 通过Selenium访问网站
    data = browser.page_source  # 获取网页源代码
    table = pd.read_html(data)[0]  # 通过pandas库提取表格
    print(table)  # 2020-09完善
    # 如果上面打印的table里的表头有问题，则需要使用如下代码将第一行为表头，然后从第二行开始取数
    # table.columns = table.iloc[0]  # 将原来的第一行内容设置为表头
    # table = table.iloc[1:]  # 改变表格结构，从第二行开始选取

    # 添加股票代码信息
    p_code = '<a href="yb_(.*?).shtml'
    code = re.findall(p_code, data)
    table['股票代码'] = code

    # 通过concat()函数纵向拼接成一个总的DataFrame
    data_all = pd.concat([data_all, table], ignore_index=True)

print(data_all)
print('分析师评级报告获取成功')
data_all.to_excel('分析师评级报告.xlsx')