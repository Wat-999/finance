#if语句
score = 100
year = 2018
if (score < 0) and (year == 2018):
    print('录入数据库')
else:
    print('不录入数据库')

score = 85
if score >= 60:
    print('及格')
else:
    print('不及格')

# 多种情况，这个用到的较少，了解即可
score = 55
if score >= 80:
    print('优秀')
elif (score >= 60) and (score < 80):
    print('及格')
else:
    print('不及格')

#for循环语句
#for语句的底层逻辑是循环，其常用格式如下所示，注意冒号和缩进
#for i in 区域：
#    要重复执行的代码
class1 = ['丁一', '王二', '张三', '李四', '王五']
for i in class1:
    print(i)
#for后面的i只是一个代号，可以换成任何内容，如j或一个字符串，只需和重复执行的代码内容匹配即可。
#for语句还常与range()函数合用。range()函数可以创建一个整数列表，基本用法如下：
#a = range(10)  从0～9的整数，类似列表切片的"左闭右开"，不包含10，其本质是创建一个列表[0,1,~9]

#for语句与range()函数结合的演示代码如下：
for i in range(3):
    print('hahaha')
#总结
#对于"for i in 区域"来说，若区域是一个列表，则i代表列表的元素
#对于"for i in 区域"来说，若区域是一个字典，则i代表列表的键名
#对于"for i in 区域"来说，若区域是一个range(n)，则i代表0～n-1的n个整数

#while循环语句
#while语句的底层逻辑也是循环，其格式如下所示，注意冒号及缩进
#while 条件：
#    要重复的代码
a = 1
while a < 3:
    print(a)
    a = a + 1   #也可以写成 a +=1
#a一开始等于1，满足小于3的条件，打印输出1，然后a在1的基础上加上1等于2，此时a仍然小于3，所以仍会执行打印输出的命令，打印输出2，
#然后a在2的基础上加上1等于3；此时a已经不满足小于3的条件，循环便终止了。

#while经常与True搭配使用，写成while True进行永久循环，其基本结构如下所示：
#while True：
#    代码块

#try/except异常处理语句：通过try/except异常处理语句可以避免因为某一步程序出错而导致整个程序终止，使用方法如下：
#try：
#    主代码
#except：
#       主代码出错时要执行的代码
#演示代码如下 ：
try:
    print(1 + 'a')
except:
    print('主代码运行失败')
#在具体项目实战中，也常常会用到try/except异常处理语句。注意不要过度使用try/except异常处理语句，因为有时需要利用程序的报错信息来定位出错的地方。
