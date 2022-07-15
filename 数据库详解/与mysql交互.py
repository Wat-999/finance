#先预定以一些变量
company = '公司'
title = '测试标题'
href = '测试链接'
source = '测试来源'
date = '测试日期'

#连接数据库
import pymysql
db = pymysql.connect(host='127.0.0.1' #   在操作数据库时，会定义conn变量，即connect()，表示建立与数据库的连接。
,user='root' # 用户名
,passwd='123456' # 密码
,port=3306 # 端口，默认为3306
,db='sys' # 数据库名称
,charset='utf8' # 字符编码
)

#插入数据
cur = db.cursor()   #获取会话指针，用来调用sql语句
sql = 'INSERT INTO test(company, title, href, date, source) VALUES (%s, %s, %s, %s, %s)' #编写slq语句
cur.execute(sql, (company, title, href, date, source))    #执行sql语句
db.commit()  #在改变数据表结构后，更新数据表
cur.close()  #关闭会话指针
db.close()   #关闭数据库连接

#占位符
#占位符的作用就是先占住一个一个固定的位置，之后再往里面添加内容。前面出现的%s可以理解为一个预留的座位，并且只有字符串类型的人才能坐。
#如果想插入一个整数类型的类容，那么这个%s就得换成%d，小数类型的内容则换成%f
a = '我的名字是%s' % ('华小智')
b = '我的名字是%s， 我的岁数是%d岁' % ('华小智，25')
print(a)
print(b)

#sql语句的多种写法
#方法1：我们通常会以如下方式编写sql语句，并在cur.execute()中传入相关参数。因为cur.execute()会把参数默认转换为字符串，所以在写占位符时都得用%s.
sql = 'INSERT INTO test(company,title,href,date,source) VALUES (%s,%s,%s,%s,%s)'
cur.execute(sql, (company, title, href, date, source))   #执行sql语句

#方法2：除了在execute()中传入参数外，还可以直接在编写sql语句时就把参数传进去，不过这中写法有几点要注意
company = '阿里巴巴'
title = '标题1'
sql = 'INSERT INTO test(company, title) VALUES (\'%s\',\'%s\') % (company, title)'  #写sql语句时已经把参数传进去了
cur.execute(sql)   #写cur.execute()时不再需要传入参数
#与上一个知识点中的占位符例子类似，相当于利用占位符%s做了字符串的拼接，构造了一个sql语句。
#注意此时要在%s前后加上引号，并且加上反斜扛构成\',取消引号的特殊含义(跟通过两个反斜杠\\取消单个反斜杠的特殊含义一样）
#这是因为sql语句在传入字符串时是需要假如引号的。拼接的sql语句如下所示：
#INSERT INTO test(company, title) VALUES ('阿里巴巴'， '标题1')
#如果不在%s前后加\'，则会拼接出如下所示的的sql语句，这样的字符串缺少引号的sql语句是不符合规范的，会导致程序报错。
#INSERT INTO test(company, title) VALUES (阿里巴巴,标题1)

#除了通过\'取消引号的特殊含义外，还有一种处理方式是联合使用双引号和单引号。之前一直强调在python中单引号和双引号没有本质区别，
#但是如果需要在引号中再次使用引号，它们就可以联合使用(因为双引号里不能再有双引号，单引号里也不能再有单引号，否则会导致字符串提前结束）
sql = "INERT INTO text(company,title) VALUES ('%s', '%s')" % (company, title)

#如果想传入整数类型的数据，就要用%d来占位，由于%d占位的是数字，所以不需要在前后\'来添加引号
score = 85
sql = 'INSERT INTO test(company,title,score) VALUES (\'%s\',\'%s\',%d) % (company,title,score)'

#方法3：除来使用占位符外，还可以直接使用字符拼接
sql =  'INSERT INTO test(company, title) VALUES (' + '\'' + company + '\'' + ',' + '\'' + company + '\'' + ')'
#其效果就是通过字符串拼接直接构造一个sql语句，和使用占位符的效果一样。不过这样的字符串拼接方式比较烦琐，而且也需要通过\'在字符串前后添加引号。
#所以在构造sql语句是，通常会用占位符来完成字符串拼接，且倾向于使用较为简洁的方法1