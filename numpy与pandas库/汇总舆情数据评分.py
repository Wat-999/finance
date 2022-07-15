#根据时间序列遍历数据库
#获取到日期的列表后，便可以结合数据库知识访问数据库，通过for循环遍历每天的舆情数据，对每条新闻的评分进行汇总。
#这里将每天评分存储到score_dict这个字典当中
import pymysql
import datetime
import pandas as pd

#连接数据库
db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', port=3306, db='sys', charset='utf8')

#设定参数
company = '腾讯'  #选定公司
date_list = list(pd.date_range('2022-05-06', '2022-05-10'))  #生成一个时间区间的序列
for i in range(len(date_list)):
    date_list[i] = datetime.datetime.strftime(date_list[i], '%Y-%m-%d')  #将时间戳转换成%Y-%m-%d格式日期
    # 也可以这样写：date_list[i] = date_list[i].strftime('%Y-%m-%d')
print(date_list)

#编写sql语句
cur = db.cursor()  #获取会话指针，用来调用sql语句
sql = 'SELECT * FROM article WHERE company = %s AND date = %s'

#遍历date_list中的日期，获取每天的评分并存储到字典score_dict中
score_dict = {}  #定义分数的字典，用以存储每日分数
for d in date_list:
    cur.execute(sql, (company, d))  #执行sql语句
    data = cur.fetchall()  #提取所有数据并赋值给变量data
    score = 100
    for i in range(len(data)):
        score += data[i][5]  #对该公司当天每条新闻的评分进行求和  data[i]表示遍历每条新闻的数据，因为评分是每条新闻数据的第6个元素，所以通过data[i][5]获取单条新闻的评分
    score_dict[d] = score
print(score_dict)
db.commit()  #更新数据表，如果对数据表没有修改，可以不写这行
cur.close()  #关闭会话指针
db.close()  #关闭数据库连接
