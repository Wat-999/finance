import smtplib
from email.mime.text import MIMEText
user = '924734143@qq.com'
pwd = 'gurddndpximybfbg'
to = '1254624823@qq.com'  # 可以设置多个收件人，英文逗号隔开，如：'***@qq.com, ***@163.com'
# 1.连接数据库 提取所有今天的"阿里巴巴"的新闻信息
import pymysql
import time
db = pymysql.connect(host='127.0.1', port=3306, user='root', password='123456', database='sys', charset='utf8')
company = '阿里巴巴'
today = time.strftime("%Y-%m-%d")  # 这边采用标准格式的日期格式

cur = db.cursor()  # 获取会话指针，用来调用SQL语句
sql = 'SELECT * FROM article WHERE company = %s AND date = %s AND score < 0'
cur.execute(sql, (company, today))
data = cur.fetchall()  # 提取所有数据，并赋值给data变量  这是获取到data是一个元组(元组可以理解为一个不可修改到列表）
print(data)
db.commit()  # 这个其实可以不写，因为没有改变表结构
cur.close()  # 关闭会话指针
db.close()  # 关闭数据库链接

# 2.利用从数据库里提取的内容编写邮件正文内容
mail_msg = []
mail_msg.append('<p style="margin:0 auto">尊敬的小主，您好，以下是今天的舆情监控报告，望查阅：</p>')  # style="margin:0 auto"用来调节行间距
mail_msg.append('<p style="margin:0 auto"><b>一、阿里巴巴舆情报告</b></p>')  # 加上<b>表示加粗
for i in range(len(data)):
    href = '<p style="margin:0 auto"><a href="' + data[i][2] + '">' + str(i+1) + '.' + data[i][1] + '</a></p>'
    #创建一个空列表mail_msg来存储href中构造到HTML代码，其基本框架是<a href=" 网址 "> 标题 </a>,之所以在两侧加上<p>和</p>是为来自动分段。
    #构造时通过字符串拼接到方式把提取到标题和网址连在一起，"注意不要漏写<a href="' + data[i][2] + '">'两处中到双引号，这个双引号不是用于字符串的拼接
    #而是HTML代码中定义链接的标准格式的要求(网址两侧需要有引号)。这里用来双引号而不是单引号，是因为字符串最外面已经用来单引号。
    #虽然python中单引号、双引号没有本质区别，但要嵌套使用引号时，内层和外层但引号形式要不同，否则会导致字符串提前结束，拼接失败
    mail_msg.append(href)

mail_msg.append('<br>')  # <br>表示换行
mail_msg.append('<p style="margin:0 auto">祝好</p>')  #margin:0表示边距(即修改邮件正文行距)，0表示上下边距为0；auto表示自动调整左右边距
mail_msg.append('<p style="margin:0 auto">华小智</p>')
mail_msg = '\n'.join(mail_msg)
#然后通过'连接字符'.join(列表名)的方式把mail_msg列表转换成字符串形式，因为最中要在邮件里展示的是一个字符串而不是一个列表。这里用换行符'\n'
#作为连接符，是为来在使用print()函数打印输出结果时更加美观。其实不加换行符直接写''.join(mail_msg)也可以，因为<p></P>已经实现了自动分段
print(mail_msg)

# 3.添加正文内容
msg = MIMEText(mail_msg, 'html', 'utf-8')

# 4.设置邮件主题、发件人、收件人
msg["Subject"] = "华小智舆情监控报告"
msg["From"] = user
msg["To"] = to

# 5.发送邮件
s = smtplib.SMTP_SSL('smtp.qq.com', 465)  # 选择qq邮箱服务，默认端口为465
s.login(user, pwd)  # 登录qq邮箱
s.send_message(msg)  # 发送邮件
s.quit()  # 退出邮箱服务
print('Success!')
