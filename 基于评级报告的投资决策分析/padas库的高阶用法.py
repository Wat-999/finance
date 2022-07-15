#1。重复值处理
import pandas as pd
data = pd.DataFrame([[1, 2, 3], [1, 2, 3], [4, 5, 6]], columns=['c1', 'c2', 'c3'])
#如果数据量较大，可以用duplicated()函数查询重复的内容
print(data[data.duplicated()])  #即可将重复的第2行筛选出来

#用sum()函数可以统计重复行的数量
print(data[data.duplicated().sum()])

#用drop_duplicates()函数可以删除重复行
print(data.drop_duplicates())
#注意drop_duplicated()函数并不会改变原表格的结构，所以需要重新赋值，

#若要按列去重，如c1列出现重复的内容，就把该列出现内容的行给删除
print(data.drop_duplicates('c1'))

#缺失值处理
#先构造一个含有缺失值的dataframe
data = pd.DataFrame([[1, 2, 3], [np.nan, 2, 3], [np.nan, np.nan, np.nan]], columns=['c1', 'c2', 'c3'])#np.nan代表空值

#可以用isnull()函数或isna()(两者作用类似）来查看空值
data.isnull()  #或者写data.isna()
#isnull()函数用于判断是否为空值，若是则返回True，否则返回False

#也可以查看单列的缺失值情况
data['c1'].isnull()

#如果数据量较大，可以筛选某列内容为空值的行
data[data['c1'].isnull()]
#其本质是根据data['c1'].isnull()得到的true和false来筛选，如果是true就筛选出来，可以看到c1列是空行的内容都被筛选出来了

#对于空值有两种常见的处理方式：删除空值和填补空值
#用dropna()函数可以删除空值
a = data.dropna()  #这种写法是只要含有空值的行就会被删除

#如果觉得这种一旦出现空值就删除整行的方法过于严格，可以在括号中设置thresh参数，例如设置为2，则表示如果该行的非空值少于2个，，则删除该行
#用fillna()函数可以填补空值，如下代码采用的是均值填充法，即用每一列的均值填充该列的空值，也可以把其中的data.mean()换成data.median()，变为中位数填充
b = data.fillna(data.mean())  #每列的空值都被填充为该列的均值


#用groupby()函数分组汇总数据
#数据量较大时，需要对数据进行分组，才能对数据有更清晰的认识
import pandas as pd
data = pd.DataFrame([['丁一', '阿里', 0.4, 0.2], ['王二', '百度', 0.2, 0.6], ['王二', '腾讯', 0.4, 0.8], ['张三', '京东', 0.1, 0.4], ['张三', '拼多多', 0.1, 0.2]], columns=['分析师', '股票名称', '30天收益率', '90天收益率'])
#我们需要计算每个分析师预测的收益率的平均值
means = data.groupby('分析师')[['30天的收益率']].mean()
#其含义为先根据分析师进行分组，然后看分组后的30天收益率，并通过mean()函数求每个组里的30天收益率的平均值。注意要用两对中括号来选取列
#写成[['30天的收益率']]，否则获得的会是一个一维结构的series对象，二非二维结构的dataframe

#除列选取单列来运算外，还可以选取多列来运算
means = data.groupby('分析师')[['30天收益率', '90天收益率']].mean()

#除了根据单列进行分组，还可以根据多列进行多重分组
means = data.groupby('分析师', '股票名称')[['30天的收益率']].mean()
#这里设置了多重行索引，其中第一重行索引为"分析师"，第二重索引为"股票名称"

#除了mean()函数外，还可以通过max()函数选取最大值，min()函数选取最小值，count()函数取频次。
#例如，要统计分析师预测的次数
count = data.groupby('分析师')[['30天的收益率']].count()
#此时列名还是30天收益率，可以用rename()函数将其改为"预测次数"
count = count.rename(columns={'30天收益率': '预测次数'})


#用pandas库进行批量处理
#主要介绍pandas库中常用于批量处理数据的apply()函数、pandas库常规的批量处理功能、常与apply()函数搭配使用的lambda()函数
import pandas as pd
data = pd.DataFrame([[-1, -2, -3], [1, 2, 3], [4, 5, 6]], columns=['c1', 'c2', 'c3'])

#如果此时希望把这个dataframe里的每个数字都加1，就可以利用apply()函数进行批量处理
def y(x):   #定义一个函数，函数返回值为x+1
    return x + 1
data.apply(y)      #传入函数名称，这个函数会作用于整张表格
#在上面代码中，apply()函数会自动遍历data每一列，然后将函数y(x)作用于每一列中的每一个元素，从而实现整张表格的数字都加1

#上面的例子是针对整张表格的，如果想对单列进行批量操作
data['c1'].apply(y)  #此时y(x)函数就只作用在c1列上 ，此时获得的是一个一维的series对象

data[['c1']].apply(y)  #此时获得的是一个二维的

#如果想修改原表格，需要重新赋值
data['c1'] = data['c1'].apply(y)  #只有c1列的所有数值加了1

#常规批量处理方式
#值得注意的是，对于一些简单的数值运算，不用apply()函数也能完成，因为现在pandas库已经支持大部分数值运算
data = pd.DataFrame([[-1, -2, -3], [1, 2, 3], [4, 5, 6]], columns=['c1', 'c2', 'c3'])
a = data + 1  # 对于整张表格加一
b = data['c1'] + 1  # 对于c1列加一
data['c1'] = data['c1'] + 1  # 对于c1列加一，并赋值给原来的c1列
print(a)
print(b)
print(data)

# 可以看到通过常规方式反而更加简洁，但是对于一些较为复杂的函数的话，比如函数中涉及if判断语句，最好还是利用apply()库，代码如下：
data = pd.DataFrame([[-1, -2, -3], [1, 2, 3], [4, 5, 6]], columns=['c1', 'c2', 'c3'])
def y(x):
    if x > 0:
        return x + 100
    else:
        return x - 100


a = data['c1'].apply(y)
print(a)


#lambda函数
#利用lambda()匿名函数可以避免定义过多的函数，使代码更加简洁，尤其是在可pands库里的apply()函数一起应用的时候
y = lambda x: x+1
print(y(1))

#上述代码类似于如下代码
def y(x):
    return x + 1
print(y(1))

#lambda函数的特点在于不用通过def来定义函数

#上述代码中虽然没有def，但仍给函数命名为y，与匿名函数但名称有点不相符，如果和apply()函数相结合，不仅不需要写def，连函数名也不需要
data.apply(lambda x: x+1)   #这里的x针对data中整张表格
data['c1'].apply(lambda x: x+1)  #这里的x针对data中的c1列

#如果要对c1列取绝对值，则可以使用abs(0函数
data['c1'].apply(lambda x: abs(x))
#因为abs()函数并不复杂，所以不用lambda()函数也可以
abs(data['c1'])

#如果想将c1列和c2列相加成新的一列
data['c4'] = data.apply(lambda x: x['c1'] + x['c2'], axis=1)
#注意apply()函数默认axis=0，即在纵向方向进行计算， 而这里是要对c1列和c2列进行横向相加，所以要设置axis=1，即在横向方向进行计算

#因为pandas库已经支持一些简单的运算，所以也可以采用如下写法：
data['c4'] = data['c1'] + data['c2']
#到这里会有疑问：既然pandas库已经支持一些简单运算，为什么还要学习apply()函数和lambda()函数呢？
#原因有两方面：一是因为还有很多人习惯使用apply()函数和lambda()函数，学习相关知识有助于看懂其他人编写的代码；二是因为有些运算比较复杂，
#这种情况下用apply()函数进行批量操作就比较方便
