#例如，想要深入到pdf的正文内容进行解析，就需要用到pdf文本解析技术。python中有多个用于解析pdf文本的库，如pdfplumber、pdfminer、Tabula库等
#目前pdfplumber库是目前使用最方便的库，它不仅能解析文字，还能方便地解析表格。

#pdfplumber库的使用方法非常简单。通过pdfplumber库的extrct_text()函数可以解析PDF文件的文本内容。
import pdfplumber
pdf = pdfplumber.open('/Users/macbookair/Desktop/数据分析/书本配套资料及电子书/python/Python金融/0.《Python金融》最新配套源代码文件（2020-12-07完善）/第10章源代码汇总/公司A理财公告.PDF')
pages = pdf.pages  #通过pages属性获取所有页的信息，此时pages是一个列表
page = pages[0]    #获取第一页的内容
text = page.extract_text()    #用extract_text()函数获取第一页的文本内容
print(text)
pdf.close()    #关闭pdf文件

#如果想解析每一页的内容，可以通过for循环语句实现
import pdfplumber
pdf = pdfplumber.open('/Users/macbookair/Desktop/数据分析/书本配套资料及电子书/python/Python金融/0.《Python金融》最新配套源代码文件（2020-12-07完善）/第10章源代码汇总/公司A理财公告.PDF')
pages = pdf.pages  #通过pages属性获取所有页的信息，此时pages是一个列表
text_all = []      #建立一个空列表
for page in pages:     #遍历pages中的每一页的信息
    text = page.extract_text()   #提取当前页的信息
    text_all.append(text)        #用列表的append()函数汇总每一页的文本内容
text_all = ''.join(text_all)     #把列表转换成字符串
print(text_all)        #打印输出文本内容
pdf.close()
#用里一个小技巧：首先创建一个空列表，然后通过列表的append()函数将每一页的文本内容存储到列表中，最后通过'连接符'.join(列表名)的方法将其列表转换成字符串


#用pdflumber库extrct_tables()提取表格内容
import pdfplumber
pdf = pdfplumber.open('/Users/macbookair/Desktop/数据分析/书本配套资料及电子书/python/Python金融/0.《Python金融》最新配套源代码文件（2020-12-07完善）/第10章源代码汇总/公司A理财公告.PDF')
pages = pdf.pages  #通过pages属性获取所有页的信息，此时pages是一个列表
page = pages[3]  #因为表格在第4页，所以提取第4页
tables = page.extract_tables()   #用extract_tales()函数提取该页所有表格
table = tables[0]  #因为第4页只有1个表格，所以通过tables[0]提取
print(table)   #打印table是一个嵌套列表结构，即大列表里包含多个小列表，每个小列表的内容，即表格中每一行的内容

#可以使用pandas库使最终展现效果更加美观，代码如下：

import pandas as pd
df = pd.DataFrame(table[1:], columns=table[0])
print(df)

#可以看到获得的表格内容中存在一些换行符/n，这是因为在原表格中这些字符之间是存在换行的。如果想把这些换行符去掉，可以利用raplace()函数将换行符替换掉
for i in range(len(table)):      #遍历大列表中每一个子列表
    for j in range(len(table[i])):    #遍历子列表中的每一个元素
        table[i][j] = table[i][j].replace('\n', '')    #替换字符
#获得的table是一个嵌套列表结构，所以需要通过两层循环来定位到具体的文本内容，table[i][j]表示子列表中的元素，然后通过replace()函数替换换行符，
#注意这里需要将替换后的内容重新赋值给table[i][j] ，才能真正完成替换

#完整代码如下
import pdfplumber
import pandas as pd
pdf = pdfplumber.open('/Users/macbookair/Desktop/数据分析/书本配套资料及电子书/python/Python金融/0.《Python金融》最新配套源代码文件（2020-12-07完善）/第10章源代码汇总/公司A理财公告.PDF')
pages = pdf.pages  #通过pages属性获取所有页的信息，此时pages是一个列表
page = pages[3]  #因为表格在第4页，所以提取第4页
tables = page.extract_tables()   #用extract_tales()函数提取该页所有表格
table = tables[0]  #因为第4页只有1个表格，所以通过tables[0]提取
#print(table)   #打印table是一个嵌套列表结构，即大列表里包含多个小列表，每个小列表的内容，即表格中每一行的内容

#可以看到获得的表格内容中存在一些换行符/n，这是因为在原表格中这些字符之间是存在换行的。如果想把这些换行符去掉，可以利用raplace()函数将换行符替换掉
for i in range(len(table)):      #遍历大列表中每一个子列表
    for j in range(len(table[i])):    #遍历子列表中的每一个元素
        table[i][j] = table[i][j].replace('\n', '')    #替换字符
pd.set_option('display.max_columns', None)  # 显示全部列   在引用pandas库时添加
df = pd.DataFrame(table[1:], columns=table[0])  #table[0]为表格第一行，  table[1:]为表格第二行及其以下的内容
print(df)

