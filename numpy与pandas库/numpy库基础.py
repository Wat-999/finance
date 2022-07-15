#numpy库与数组
import numpy as np
a = [1, 2, 3, 4]
b = np.array([1, 2, 3, 4])  #创建数组的一种方式，array就是数组的意思
print(a)  #[1, 2, 3, 4]列表的展现形式
print(b)  #[1 2 3 4]数组的展现形式
print(type(a))  #<class 'list'>  a的类型为列表
print(type(b))  #<class 'numpy.ndarray'>   b的类型为数组
print(a[1])  #列表a索引调用的结果
print(b[1])  #数组b索引调用的结果
print(a[0:2])  #[1, 2]列表切片的结果，注意列表切片也是"左闭右开"
print(b[0:2])  #[1 2]数组b切片的结果，注意列表切片也是"左闭右开"
#从输出结果可以看出，列表和数组有着相同的索引机制，唯一的区别就是数组中的元素是通过空格分隔，而列表中的元素是通过逗号分隔。
#那么为什么python又要创建一个numpy库呢？其原因很多，这里主要讲2点
#第一numpy作为一个数据处理的库，能很好地支持一些数学运算，而列表较为麻烦，演示代码如下：
c = a * 2
d = b * 2
print(c)   #[1, 2, 3, 4, 1, 2, 3, 4]
print(d)   #[2 4 6 8]
#可以看到同样做乘法运算，列表只是把元素复制里一遍，而数组则是对元素做里数学运算
#第而，数组支持多维数据，而列表通常只能存储一维数据。一维数据和多维数据是什么意思呢？
#我们可以借用立体几何中对概念来理解：一维类似一条直线，多维类似平面(二维)或立体(三维)等。列表中对数据是一维的，而excel工作表中的数据则是二维的，演示如下：
e = [[1, 2], [3, 4], [5, 6]]  #列表里的元素维小列表
f = np.array([[1, 2], [3, 4], [5, 6]])   #创建二维数组的一种方式
#可以看到，列表e虽然包含3个小列表，但其结构是一维的，而数组f是3行2列的二维结构，这也是之后学习pandas库的核心内容。因为数据处理中经常用到二维数组，即二维的表格结构

#创建数组的几种方式
#创建一维数组
a = np.array([1, 2, 3, 4])
#创建二维数组
b = np.array([[1, 2], [3, 4], [5, 6]])

#除此之外，还有一些常见的创建数组的方式。以一维数组为例，可以使用np.arange()函数来创建一维数组，括号里可以输入1～3个参数
#1个参数：起点默认值0，参数值为终点，步长默认为1，左闭右开
x = np.arange(5)
#2个参数：第一个参数为起点，第2个参数值为终点，步长默认为1，左闭右开
y = np.arange(5, 10)
#3个参数：第一个参数为起点，第2个参数值为终点，第3个参数为步长，左闭右开
z = np.arange(5, 10, 0.5)

#我们还可以使用np.random()函数来创建随机一维数组。例如，通过np.random.randn(3)创建一个包含服从正态分布(均值为0，方差为1的分布)的3个随机数的一维数组。
c = np.random.randn(3)

#至于二维数组，可以利用创建一维数组的np.arange()函数和reshape()函数来创建，例如，将0～11这12个整数转换成3行4列的二维数组
d = np.arange(12).reshape(3, 4)

#这里再简单介绍一种创建随机整数二维数组的方法
e = np.random.randint(0, 10, (4, 4))
#其中np.random.randint()函数用来创建随机整数，括号里第1个元素0表示起始数，第2个元素10表示终止数，第3个元素(4, 4)则表示创建一个4行4列的二维数组

#pandas库基础：pandas库更善于处理二维数据。pandas库主要有两种数据结构：series和DataFrame
#Series类似于通过numpy库创建的一维数组，不同的是series对象不仅包含数值，还包含一组索引，其创建方式如下：
import pandas as pd
s1 = pd.Series(['丁一', '王二', '张三'])
#s1也是一个一维数据结构，并且每个元素都有一个行索引可以用来定位，例如，可以通过s1[1]来定位到第二个元素"王二"
#Series单独使用相对较少，pandas库主要使用DataFrame数据结构。DataFrame是一种二维表格数据结构，可以将其看成一个excel表格。

#二维数据表格DataFrame的创建与索引的修改
#1通过列表创建DataFrame
import pandas as pd
a = pd.DataFrame([[1, 2], [3, 4], [5, 6]])
print(a)
#注意它也有行索引和列索引，索引序号是从0开始的

#创建dataframe自定义列索引和行索引的名称
c = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['date', 'score'], index=['a', 'b', 'c', 'd'])
#columns代表列索引名称， index代表行索引名称

#通过列表创建dataframe还可以采用如下形式
a = pd.DataFrame()
date = [1, 3, 5]
score = [2, 4, 6]
a['date'] = date
a['score'] = score
#注意要保证date列表和score列表的长度一致，否则会报错。在评估券商分析师预测准确度时会有应用

#通过字典创建dataframe
#这里默认字典键列索引，演示如下
b = pd.DataFrame({'a': [1, 3, 5], 'b': [2, 4, 6]}, index=['x', 'y', 'z'])

#如果想要字典键变成行索引，可以通过from_dict的方式来将字典转换成dataframe，并同时设置orient参数为index
c = pd.DataFrame.from_dict({'a': [1, 3, 5], 'b': [2, 4, 6]}, orient="index")
#其中orient参数用于指定字典键对应的方向，默认值为columns，即默认字典键为列索引，如果设置成index，则表示字典键为行索引

#通过二维数组创建dataframe
#在numpy库创建的二维数组的基础上，也可以创建dataframe
import pandas as pd
import numpy as np
d = pd.DataFrame(np.arange(12).reshape(3, 4), index=[1, 2, 3], columns=['a', 'b', 'c', 'd'])

#dataframe索引的修改
#修改行索引，列索引用得相对较少，如果想设置行索引那一列的名称，可以通过index。name的方式来设置
a = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['date', 'score'], index=['a', 'b', 'c', 'd'])
a.index.name = '公司'

#如果想对索引进行重命名，可以使用rename()函数
a = a.rename(index={'a': '万科', 'b': '阿里', 'c': '百度'}, columns={'date': '日期', 'score': '分数'})
#rename()函数是用新索引名新建一个dataframe，未改变a的内容，所以这里将新dataframe赋值给a来改变其内容。也可以设置inplace参数为True来实现真正的重命名
a = a.rename(index={'a': '万科', 'b': '阿里', 'c': '百度'}, columns={'date': '日期', 'score': '分数'}, inplace=True)

#如果想将行索引转换为常规列，可以重置索引，同样需要将其重新赋值给a，或者在reset_index()的括号里设置inplace参数为True
a = a.reset_index()
#此时行索引内容将被重置为数字序号，原行索引变成新的一列

#如果想把常规列转换为行索引
a = a.set_index('日期')  #或者直接写a.set_index('日期', inplace=True)