import pymysql
import time

# 连接数据库
db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', port=3306, db='sys', charset='utf8')

# 设定参数
company = '百度'   # 选定公司
today = time.strftime("%Y-%m-%d")  # 设置当天日期

#  编写SQL
cur = db.cursor()  # 获取会话指针，用来调用SQL语句
sql = 'SELECT * FROM article WHERE company = %s AND date = %s'  # 如果想获取全部信息，可以把AND后面的筛选条件去掉
cur.execute(sql, (company, today))
data = cur.fetchall()  # 提取所有数据并赋值给data变量
# 计算当日评分
score = 100
for i in range(len(data)):
    score += data[i][5]  # 合并该公司当天每条新闻分数

db.commit()  # 更新表单，如果对数据表没有修改，可以不写这行
cur.close()  # 关闭会话指针
db.close()  # 关闭

print(company + '的今日舆情评分为：' + str(score))

