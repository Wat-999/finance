#文件的读取
#读取excel工作簿中的数据
import numpy as np
import pandas as pd
data = pd.read_excel('data.xlsx')  #data为dataframe结构
#这里使用的文件路径为相对路径(即文件在代码文件下），也可以设置成绝对路径。read_excel()函数还可以设定参数，如下
data = pd.read_excel('data.xlsx', sheetname=0, encoding='utf-8')
#sheetname用于指定工作表，可以是工作表名称，也可以是数字(默认为0，即第一个工作表)
#encoding用于指定文件编码方式，一般设置为utf-8或GBK，以避免中文乱码
#idex用于设置某一列为行索引

#读取csv文件
data = pd.read_csv('data.csv')
#read_csv也可以设定参数
data = pd.read_csv('data.csv', delimiter=',', encoding='utf-8')
#delimter参数用于指定csv文件的分隔符号，默认为逗号，其他参数同上

#文件的写入
#先创建一个DataFrame
data = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['a列', 'b列'])
#将DataFrame中的数据写入excel工作簿
data.to_excel('data.xlsx')  #这里的文件存储路径使用的是相对路径，可以根据需要写成绝对路径，运行之后将在代码文件夹生成一个"data.xlsx"文件
#输出结果中，行索引信息保留在工作簿的第一列中，如果想在写入数据时不保留行索引信息，可以设置to_excel()函数的参数。
#常用参数有：sheetname用于指定工作表名称，index用于指定是否写入行索引信息，默认为true,即保存行索引信息至输出文件的第1列，若设置为false，则忽略行索引信息
#columns用于指定要写入的列，encoding用于指定编码方式
#例如，要将data中的a列数据写入Excel工作簿并忽略行索引信息，代码如下：
data.to_excel('data.excel', columns=['a列'], index=false)
#通过类似的方式，可以将data中的数据写入cdv文件
data.to_csv('data.csv')


#数据的读取与编辑
#首先创建一个3行4列的DataFrame用于演示，行索设定为r1,r2,r3,列索引设定为c1,c2,c3
data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['c1', 'c2', 'c3'], index=['r1', 'r2', 'r3'])
#也可以通过二维数组创建DataFrame
data = pd.DataFrame(np.arange(1, 10).reshape(3, 3), columns=['c1', 'c2', 'c3'], index=['r1', 'r2', 'r3'])

#数据的读取
#按照列读取数据
a = data['c1']
#可以看到读取的数据不包含列索引信息，这是因为通过data['c1']读取一列时返回的是一维数据series类型的数据，通过如下代码可以返回一个二维的表格数据
b = data[['c1']]
#如果要读取多列，则需要在中括号[]中指定列表，例如读取c1列和c3列，可以写为data[['c1','c3']],注意：这里必须是一个列表，而不能是data['c1','c3']
c = data[['c1', 'c3']]
#按照行读取数据：可以根据行序号来读取数据，例如读取第2～3行数据，注意序号从0开始，左闭右开
a = data[1:3]
#二pandas库推荐使用iloc方法来根据行序号读取数据，这样更直观，而且不想data[1:3]可能会引起混淆
b = data.iloc[1:3]
#而且要读取单行，就必须用iloc方法，例如，读取倒数第一行
c = data.iloc[-1]
#此时如果使用data[-1]则会报错，因为程序可能会认为-1是列名，导致混淆报错；
#除了通过行序号读取数据外，还可以通过loc方法根据行的名称来读取数据
d = data.loc[['r2', 'r3']]
#如果行数很多，可以通过head()函数来读取前5行数据,括号里可以填数字满足所需读取的行数
e = data.head()

#按区块读取数据
#如果想读取某几行的某几列数据，例如读取c1和c3列的前2行数据
a = data[['c1', 'c3']][0:2]  #也可以写成data[0:2][['c1', 'c3']]
#在实战中，通常采用iloc和列读取相结合的方式来读取特定的区块数据,还有一个ix方法，它的索引不像loc和iloc必须为字符串索引或数字索引。目前，不推荐使用
b = data.iloc[0:2][['c1', 'c3']]

#数据的运算
#从已有的列中，通过数据运算创造新的一列
data['c4'] = data['c3'] - data['c1']
data.head()

#数据的筛选，例如读取c1列中数字大于1的行
a = data[data['c1'] > 1]

#如果有多个筛选条件，可以通过"&"表示且或"｜"表示或连接。例如，筛选c1列中数字大于1且c2列中数字等于5的行。
#注意在筛选条件两侧要加上小括号，此外，判断两者是否相等是用"=="而不是"="(一个等号表示赋值，两个等号表示逻辑判断）
b = data[(data['c1'] > 1) &data['c2'] == 5]

#数据的排序：使用sort_values()可以根据列对数据进行排序，例如，要按c2列进行降序排序
a = data.sort_values(by='c2', ascending=False)
#其中，by参数用于指定根据哪一列来排序；ascending参数为上升的意思，默认为True，表示升序排序，设置为false则表示降序排序
#使用sort_index()则可以根据行索引进行排序。例如，按行索引进行升序排序的代码如下：
a = a.set_index()  #同样可以设置参数ascending

#数据的删除
#如果要删除数据表中的数据，就需要用到drop()函数，具体方法如下：
DataFrame.drop(index=None, columns=None, inplace=False)
#drop()函数常用的几个参数：index用于指定删除的行，columns用于指定要删除的列，
#inplace默认为False表示该删除操作不改变原表格，而是返回一个执行删除操作后的新DataFrame
#如果设置inplace为True，则会直接在原表格中进行删除操作
#例如，删除c1列的数据
a = data.drop(columns='c1')
#删除多列数据，例如，删除c1列和c3列，可以通过列表的方式声明
b = data.drop(columns=['c1', 'c3'])
#如果要删除行数据，例如删除第1行和第3行
c = data.drop(index=['r1', 'r3'])
#需要注意的是，上述代码中要输入行索引的名称而不是数字序号，除非行索引名称本来就是数字，才可以输入对应的数字。
#上述代码中删除数据后又赋值给新的变量，不会改变原表格data的结构，如果想改变原表格data的结构，可以设置inplace参数为True，代码如下
data.drop(index=['r1', 'r3'], inplace=True)

#数据表格的拼接
#pandas库还提供列一些高级功能，其中数据合并与重塑为两个数据表的拼接提供列极大的便利，主要涉及merge()函数、concat()函数、apeend()函数。其中merge()函数用得较多
#假设创建了如下两个dataframe数据表，需要将他们合并
import pandas as pd
df1 = pd.DataFrame({'公司': ['万科', '阿里', '百度'], '分数': [90, 95, 85]})
df2 = pd.DataFrame({'公司': ['万科', '阿里', '京东'], '股价': [20, 180, 30]})

#merge()函数可以根据一个或多个列将不同数据表中多行连接起来
df3 = pd.merge(df1, df2)
#如果相同列名不止一个，可以同on参数指定按照哪一列进行合并
df3 = pd.merge(df1, df2, on='公司')
#默认多合并其实是取交集(inner连接),即选取两表共有多内容，如果想取并集(outer连接)，即选取两表所有的内容，可以设置"how"参数
df3 = pd.merge(df1, df2, how='outer')
#如果想保留左表df1的内容，而对右表df2不太在意，可以将how参数设置为left
df3 = pd.merge(df1, df2, how='left')
#同理如果想保留右表df2的全部内容，而不太在意左表df1，可以将how参数设置为right

#如果想根据行索引进行合并，可以设置left_index和right_index,代码如下
df3 = pd.merge(df1, df2, left_index=True, right_index=True)


#concat()函数：是一种全连接(union all)方式，它不需要对齐，而是直接进行合并，即不需要两表的某些列或索引相同，只是把数据整合到一起。
#所以concat()函数没有how参数，而是通过axis参数指定连接的轴向。该参数默认为0， 按行方向连接，即纵向拼接
df3 = pd.concat([df1, df2])  #或写成df3 = pd.concat([df1, df2]，axis=0)
#此时的行索引为原来两表各自的索引，如果想重置索引，可以使用rset_index(inplace=True),或者在concat()函数中设置ignore_index=True
df3 = pd.concat([df1, df2], ignore_index=True)
#如果想按列方向连接，也即横向拼接，可以设置参数axis=1
df3 = pd.concat([df1, df2], axis=1)

#append()函数：可以说是concat()函数的简化版，效果和pd.concat([df1, df2])类似，实现的也是纵向拼接
df3 = df1.append(df2)
#append()函数还有个常用的功能，和列表.append()一样,可用来新增元素
df3 = df1.append({'公司': '腾讯', '分数': '90'}, ignore_index=True)
#这里一定要设置ignore_index=True忽略原索引，否则会报错
