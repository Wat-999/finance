import pymysql
db = pymysql.connect(host='127.0.0.1' #   在操作数据库时，会定义conn变量，即connect()，表示建立与数据库的连接。
,user='root' # 用户名
,passwd='123456' # 密码
,port=3306 # 端口，默认为3306
,db='sys' # 数据库名称
,charset='utf8' # 字符编码
)

company = '阿里巴巴'   #为筛选条件

cur = db.cursor()   #获取会话指针，用来调用sql语句
sql = 'DELETE FROM test WHERE company = %s'  #编写sql语句
cur.execute(sql, company)  #执行sql语句
db.commit()  #提交修改，这一行必需写，因为改变了数据表的结构
cur.close()   #关闭会话指针
db.close()     #关闭数据库连接