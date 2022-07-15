#本节将遍历一个文件夹里所有的理财公告pdf文件，然后通过pdf文本解析对理财公告进行深度筛选，获取符合要求的理财公告，为寻找合适的资金方(投资方)做准备

#遍历文件夹里所有的pdf文件
import os    #引用os库，为之后使用walk()函数遍历文件夹做准备
file_dir = r'/Users/macbookair/Desktop/数据分析/书本配套资料及电子书/python/Python金融/0.《Python金融》最新配套源代码文件（2020-12-07完善）/第10章源代码汇总/演示文件夹'
#指定文件夹路径
for files in os.walk(file_dir):  #遍历指定文件夹下的所有子文件及子文件夹里的所有文件信息，如果没有子文件夹，就只循环一遍，获取到该指定文件夹下的所有信息
    print(files[2])
#其中files[0]表示母文件夹信息，files[1]表示各个子文件夹信息，files[2]表示母文件夹和子文件夹里的各个文件信息，一般用files[2]来获取文件信息

#获取到文件名后，还需要判断文件后缀名是否为".pdf",如下代码可以获得文件后缀名
os.path.splitext(文件名)[1]    #splitext()函数对文件名进行切割，切割后变成文件名和后缀名
#获得文件后缀名后，即可通过if判断语句进行文件后缀名判别
import os    #引用os库，为之后使用walk()函数遍历文件夹做准备
file_dir = r'/Users/macbookair/Desktop/数据分析/书本配套资料及电子书/python/Python金融/0.《Python金融》最新配套源代码文件（2020-12-07完善）/第10章源代码汇总/演示文件夹'
#指定文件夹路径
for files in os.walk(file_dir):  #遍历该文件夹及其下所有的子文件夹
    for file in files[2]:    #遍历每个文件夹里的所有文件
        if os.path.splitext(file)[1] == '.PDF' or os.path.splitext(file)[1] == '.pdf':     #检查文件后缀名,文件后缀名有可能是小写
            print(file)

#把这些pdf文件对文件名筛选出来之后，还需要把它们都放到一个列表里，方便之后批量解析时调用，可以通过一个空列表和列表对append()函数来完成
file_list = []
for files in os.walk(file_dir):
    if os.path.splitext(file)[1] == '.PDF' or os.path.splitext(file)[1] == '.pdf':  # 检查文件后缀名,文件后缀名有可能是小写
        file_list.append(file)
        print(file_list)
#打印结果，可以看到其中只含有pdf文件
#file_list列表中元素都是文件名，在文本解析时为来调用pdf文件，还需要给文件名加上文件夹路径。(windows)例如，需要把"信托购买报告A.PDF"改成"文件夹路径\\信托信托购买报告A.PDF。
#可以通过字符串拼接对方式加上文件夹路径，代码如下：
file_list.append(file_dir + '/' + file)  #mac写法一个/
#这里有一个之前也强调过的注意点：字符串拼接时一定要用两个反斜杠来拼接。因为一个反斜杠加引号'\'是有特殊含义的，用在这里会导致程序报错，而使用两个反斜杠可以取消反斜杠的含义

#完整代码如下

import os    #引用os库，为之后使用walk()函数遍历文件夹做准备
file_dir = r'/Users/macbookair/Desktop/数据分析/书本配套资料及电子书/python/Python金融/0.《Python金融》最新配套源代码文件（2020-12-07完善）/第10章源代码汇总/演示文件夹'
file_list = []
for files in os.walk(file_dir):  # 遍历该文件夹及其里面的所有子文件夹
    for file in files[2]:        #遍历母文件夹和子文件夹里的各个文件信息
        if os.path.splitext(file)[1] == '.pdf' or os.path.splitext(file)[1] == '.PDF':
            file_list.append(file_dir + '/' + file)
print(file_list)