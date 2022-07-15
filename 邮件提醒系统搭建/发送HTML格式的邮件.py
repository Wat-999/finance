import smtplib
from email.mime.text import MIMEText
user = '你自己的qq号@qq.com'
pwd = '你自己的SMTP授权码'
to = '你自己设置的收件人邮箱'  # 可以设置多个收件人，英文逗号隔开，如：'***@qq.com, ***@163.com'

# 1.编写邮件正文内容
mail_msg = '''
<p>这个是一个常规段落</p>
<p><a href="https://www.baidu.com">这是一个包含链接的段落</a></p>
'''
msg = MIMEText(mail_msg, 'html', 'utf-8')
#MIMEText括号里的参数中，第一个参数mail_msg指定邮件正文内容，第2个参数'html'表示邮件正文内容是按照HTML格式显示的，第3个参数'utf-8用来声明中文编码方式
#在给mail_msg赋值时，用3个单引号来包围HTML代码。其中三个单引号用于包围注释内容，但这里由于字符串中存在换行，所以也要用三个单引号来包围

# 2.设置邮件主题、发件人、收件人
msg['Subject'] = '测试邮件主题!'
msg['From'] = user
msg['To'] = to

# 3.发送邮件
s = smtplib.SMTP_SSL('smtp.qq.com', 465)  # 选择qq邮箱服务，默认端口为465
s.login(user, pwd)  # 登录qq邮箱
s.send_message(msg)  # 发送邮件
s.quit()  # 退出邮箱服务
print('Success!')   #运行结果，单击邮件正文但第2行字，即可跳转到百度首页


#发送邮件附件
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
user = '924734143@qq.com'
pwd = 'gurddndpximybfbg'
to = '1254624823@qq.com'  # 可以设置多个收件人，英文逗号隔开，如：'***@qq.com, ***@163.com'

# 1.设置一个可以添加正文和附件的msg
msg = MIMEMultipart()

# 2.先添加正文内容，设置HTML格式的邮件正文内容
mail_msg = '''
<p>这个是一个常规段落</p>
<p><a href="https://www.baidu.com">这是一个包含链接的段落</a></p>
'''
msg.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 3.再添加附件，这里的文件名可以有中文，但下面第三行的filename不可以为中文
att1 = MIMEText(open('/Users/macbookair/Desktop/简历/背景调查清单—贺积龙.xlsx', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 下面的filename是在邮件中显示的名字及后缀名
att1.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', '背景调查清单—贺积龙.xlsx'))  # 2020更新
msg.attach(att1)
#若想发送多个附件，只需要把添加附件的代码重复几遍并修改相关内容。
#例如，把上面代码中的att1换成att2，然后修改文件路径
# 4.设置邮件主题、发件人、收件人
msg['Subject'] = '测试邮件主题!'
msg['From'] = user
msg['To'] = to

# 5.发送邮件
s = smtplib.SMTP_SSL('smtp.qq.com', 465)
s.login(user, pwd)
s.send_message(msg)  # 发送邮件
s.quit()
print('Success!')
