# 快捷键
# 如果要减小缩进量，可以按快捷键shift+tab。
# 如果要同时对多行代码调整缩进量，可以选择多行代码，按tab键统一增加缩进量，再按shift+tab统一减小缩进量
# 在pycharm中添加注释的快捷键是command+/，选择多行代码后按注释快捷键，可以将选中的代码批量转换为注释
#1.1数据类型：数字与字符串
# 数字和字符串的核心知识点是需要知道1和'1'是两种不同的数据类型。前者是一个数字，可以进行加减乘除；
# 而后者则是一个字符串，也就是常说的文本类容。字符串的最大特点就是在它的两旁有单引号或双引号
#a = '我是一个字符串'
# 不同的数据类型是不能相互运算的，例如：
#a = 1 + '1'
#print(a)  #会报错unsupported operand type(s) for +: 'int' and 'str'

#用type()函数可以显示变量的类型
a = 1
print(type(1))  #数字类型除量int格式外，还有float格式(浮点数格式，即小数格式）

# 通过str()函数可以把数字转换为字符串
a = 1
b = str(a)
c = b + '1'
print(c)  #可以看到实现量字符串拼接的结果

#通过int()函数可以把字符串转换成数字
a = '1'
b = int(a)
c = b + 1
print(c)

#1.2数据类型：列表与字典、元组与集合
# 列表：列表就像一个容器，可以将不同的数据存储到里面并进行调用。例如，一个班级里有5名学生，需要有一个容器把他们的姓名放在一起，可以采用如下的列表格式：
#claas1 = ['丁一', '王二', '张三', '李四', '王五']
# 其中列表的格式为：列表名 = [元素1， 元素2，～～～～]
# 列表里的元素可以是字符串，也可以是数字，甚至可以是另外一个列表，下面的列表就含有三种元素：数字1、字符床'123'、列表[1,2,3]
# a = [1, '123', [1, 2, 3]]
# 利用for循环语句可以遍历列表中的所有元素
claas1 = ['丁一', '王二', '张三', '李四', '王五']
for i in claas1:
    print(i)

#统计列表的元素个数：有时需要统计列表里一共有多少个元素(又叫获取列表的长度),可以使用len()函数：格式为len(列表名)
a = len(claas1)
print(a)
#调取列表的单个元素：通过在列表名之后加上"[序号]"调取单个元素
a = claas1[1]
print(a)

#列表切片
#如果想选取列表中的几个元素，如选取上述claas1中的第2～4个元素，就要用到"列表切片"的方法，一般格式为：列表名[序号1：序号2]。
#其中序号1可以取到，而序号2则取不到，俗称"左闭右开'。
claas1 = ['丁一', '王二', '张三', '李四', '王五']
a = claas1[1:4]
print(a)

#有时不确定序号1或序号2，可以采用只写一个序号的方式
claas1 = ['丁一', '王二', '张三', '李四', '王五']
a = claas1[1:]  #选取第2个元素至最后一个元素
b = claas1[-3:]  #选取倒数第3个元素到最后一个元素
c = claas1[:-2]  #选取倒数第2个元素前的所有元素  注意左闭右开

#添加列表元素：使用append()函数可以给列表添加元素
score = []
score.append(80)   #通过append()函数给列表添加一个元素
print(score)

#列表与字符串之间的转换：列表与字符串之间的转换在文本筛选中有很大的作用。
#例如，要把列表claas1转换成一个字符串'丁一，王二，张三，李四，王五'，可以用'连接符'.join(列表名)
#其中，引号(单引号，双引号皆可)中的内容是字符串之间的连接符，如"，""；"等，所以，若要把claas1转换成一个用逗号连接的字符串，代码为：','.join(claas1)
claas1 = ['丁一', '王二', '张三', '李四', '王五']
a = ','.join(claas1)
print(a)
#如果把逗号换成空格，那么输出的就是'丁一 王二 张三 李四 王五'

#字符串转为列表主要用的是split()函数，括号里的内容为分割符
a = "hi hello world"
print(a.split(' '))  #注意这里使用的分割符号为文字之间的空格

#2.字典：是另一种数据存储的格式，例如，claas1里的每个人都有一个数学考试分数，想把他们的姓名和分数一一匹配到一起，那么就需要用字典来存储数据
#字典的基本格式：字典名 = {键1：值1，键2：值2，～～～～～～}
#在字典中，每个元素都有两个部分(而列表中每个元素只有一个部分)，前一个部分称为键，后一个部分称为值，中间用冒号相连。
#键相当于一把钥匙，值相当于一个箱子，一把钥匙对应一个箱子。那么对于class1里的每个人来说，一个人的姓名对应一个分数，相应的字典写法如下：
claas1 = {'丁一': 85, '王二': 95, '张三': 75, '李四': 65, '王五': 55}
#如果要提取字典中的某一个元素的值，可以通过如下的格式实现： 字典名['键名']
score = claas1['王二']
print(score)
#如过想把每个人的姓名和分数打印出来
claas1 = {'丁一': 85, '王二': 95, '张三': 75, '李四': 65, '王五': 55}
for i in claas1:
    print(i + ':' + str(claas1[i]))
#这里i是字典里键，也就是"丁一"，"王二"等内容，claas1[i]输出的就是值，即这些人的分数。因为分时为数字格式，在进行字符串拼接时需要通过str()函数进行转换

#另一种遍历字典的方法是通过字典的items()函数
claas1 = {'丁一': 85, '王二': 95, '张三': 75, '李四': 65, '王五': 55}
a = claas1.items()
print(a)
#通过items()函数返回的是可遍历的(键，值)元组数组

#除了列表和字典外，还有两种存储内容的方式：元组(tuple)和集合(set)
#元组的定义和使用方法与列表非常类似，区别在于列表的符号中括号[]，而元组的符号是小括号()，并且元组中的元素不可修改
a = ('丁一', '王二', '张三', '李四', '王五')
print(a[1:3])

#集合是一个无序不重复的序列，和列表也比较类似，用于存储不重复数据。通过大括号{}或set()函数创建集合，演示代码如下：
a = ['丁一', '王二', '张三', '李四', '王五','丁一', '王二', '张三', '李四', '王五']
print(set(a))   #可以看到通过set()函数获得了一个集合，删除了重复的内容
#相对于列表和字典，元组和集合用得较少

