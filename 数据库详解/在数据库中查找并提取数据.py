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
sql = 'SELECT * FROM test WHERE company = %s'  #编写sql语句
cur.execute(sql, company)  #执行sql语句
data = cur.fetchall()  #提取所有数据，并赋值给变量data
print(data)
db.commit()  #提交修改，这一行其实可以不写，因为没有改变数据表的结构
cur.close()   #关闭会话指针
db.close()   #关闭数据库连接
#此时已经把所有company(公司名称)为"阿里巴巴"的数据都提取出来了。从包围内容的符号()可以看出，提取的数据以元组的形式存在
#元组和列表非常类似，区别只是包围的符号不同，并且元组中的元素不可修改，所以可以借用列表的知识来进一步处理元组。
#例如，要提取每条新闻的标题，可以在上面的代码之后写如下代码
for i in range(len(data)):
    print(data[i][1])
#与提取列元素的方法一样，通过data[i]提取大元组里的小元组的信息，data[0]就是第一个小元组('阿里巴巴'，'标题1'，'链接1'，'日期1'，'来源1'）
#若要提取这个小元组里的标题(标题是小元组的第2个元素），可以利用data[0][1]完成。结合for循环语句就可以提取到每条新闻的标题了。

#如果筛选条件不止一个，例如，要通过company(公司名称）和title(标题）2个筛选条件来提取数据
sql = 'SELECT * FROM text where company = %s AND title = %s'
cur.execute(sql, (company, title))   #执行sql语句
#sql语句中有2个筛选条件并通过'AND'来连接，利用cur.execute()函数执行sql语句时就要传入2个参数，这两个参数同样需要用括号包围起来，写成(company,title)
#如果有更多筛选条件，可以模仿上述形式添加

