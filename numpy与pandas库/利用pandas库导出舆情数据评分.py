#汇总舆情数据评分：这里以A股上市公司万科集团为例，整理出其从2018年9月1日到2018年12月1日之间（共三个月）每天的评分数据
#获取一段时间的时间序列：首先通过pandas库的date_range()函数生成一个2018年9月1日到2018年12月1日的时间序列，为之后批量从数据库调取评分数据做准备
import pandas as pd
date_list = pd.date_range('2018-09-01', '2018-12-01')
print(date_list)
#这里返回的结果是一个日期格式的时间索引序列，并不是一个常规的列表，所以还需要通过list()函数将其转换为常规的列表
date_list = list(pd.date_range('2018-09-01', '2018-12-01'))
print(date_list)
#此时返回的虽然是一个列表，但是里面的日期的类型确是Timestamp(时间戳)类型，为了用于之后数据库sql查询，必须将其转化为"%Y-%m-%d"格式的日期字符串
#这里通过datetime库对时间戳类型的日期进行转化
import datetime
for i in range(len(date_list)):
    date_list[i] = datetime.datetime.strftime(date_list[i], '%Y-%m-%d')
    #date_list[i] = data_list[i].strftime('%Y-%m-%d')  #两种效果等同
    print(date_list)
#其中strftime()函数可以将时间戳格式的日期转换成字符串格式，也可以按照如下写法来使用strftime()函数，两种方法效果是一样的
#date_list[i] = data_list[i].strftime('%Y-%m-%d')

#根据时间序列遍历数据库
#获取到日期的列表后，便可以结合数据库知识访问数据库，通过for循环遍历每天的舆情数据，对每条新闻的评分进行汇总。
#这里将每天评分存储到score_dict这个字典当中
import pymysql
import datetime
import pandas as pd

#连接数据库
db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', port=3306, db='sys', charset='utf8')

#设定参数
company = '万科'  #选定公司
date_list = list(pd.date_range('2022-05-06', '2022-05-10'))  #生成一个时间区间的序列
for i in range(len(date_list)):
    date_list[i] = datetime.datetime.strftime(date_list[i], '%Y-%m-%d')  #将时间戳转换成%Y-%m-%d格式日期

#编写sql语句
cur = db.cursor()  #获取会话指针，用来调用sql语句
sql = 'SELECT * FROM article WHERE company = %s AND date = %s'

#遍历date_list中的日期，获取每天的评分并存储到字典score_dict中
score_dict = {}  #定义字典，用于存储每天的评分
for d in date_list:
    cur.execute(sql, (company, d))  #执行sql语句
    data = cur.fetchall()  #提取所有数据并赋值给变量data
    score = 100
    for i in range(len(data)):
        score += data[i][5]  #对该公司当天前5条新闻的评分进行求和
    score_dict[d] = score
db.commit()  #更新数据表，如果对数据表没有修改，可以不写这行
cur.close()  #关闭会话指针
db.close()  #关闭数据库连接
print(score_dict)