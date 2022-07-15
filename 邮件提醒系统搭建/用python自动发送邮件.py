#QQ邮箱发送邮件
import smtplib  # 引入两个控制邮箱发送邮件的库
from email.mime.text import MIMEText

user = '924734143@qq.com'  # 发件人邮箱
pwd = 'gurddndpximybfbg'  # 邮箱的SMTP密码，
to = '1254624823@qq.com'  # 可以设置多个收件人，英文逗号隔开，如：'***@qq.com, ***@163.com'

# 1.邮件正文内容
msg = MIMEText('测试邮件正文内容')

# 2.设置邮件主题、发件人、收件人
msg['Subject'] = '测试邮件主题!'  # 邮件的标题
msg['From'] = user  # 设置发件人
msg['To'] = to  # 设置收件人

# 3.发送邮件
s = smtplib.SMTP_SSL('smtp.qq.com', 465)  # 选择qq邮箱服务，默认端口为465
s.login(user, pwd)  # 登录qq邮箱
s.send_message(msg)  # 发送邮件
s.quit()  # 退出邮箱服务
print('Success!')
#实战中需要修改的就是发件人信息、收件人信息、邮箱的SMTP授权码，以及邮件的正文内容和邮件主题，这里讲一下如何SMTP授权码。它并不是qq邮箱的登录密码，
#而是一个程序自动发送邮件所需的授权码。
#获取步骤如下：
#1登录qq邮箱，单击顶部的设置链接，然后单击账户标签
#2在账户选项卡中向下滚动，直到看到"POP3/SMTP服务"右侧的开启链接
#3单击开启链接后，会有一个验证保密的过程。按照页面的说明，向指定号码发送指定内容的手机短信，发送完毕后单击页面中的"我已发送按钮"，会弹出一个框，里面
#就包含SMTP授权码，把它复制存储起来，方便以后调用
#获得自己qq邮箱的SMTP授权码后，便可以设置代码里的发件人、授权码、及收件人，然后运行程序。
#网易163邮箱发送邮件
import smtplib
from email.mime.text import MIMEText
user = 'hjlving@163.com'  # 发件人，这里为163邮箱了
pwd = 'PVREFTQPBHSMUQKI'  # 163邮箱的SMTP授权码
to = 'hjlsing@126.com'  # 可以设置多个收件人，英文逗号隔开，如：'***@qq.com, ***@163.com'

# 1.邮件正文内容
msg = MIMEText('测试邮件正文内容')

# 2.设置邮件主题、发件人、收件人
msg['Subject'] = '测试邮件主题!'
msg['From'] = user
msg['To'] = to

# 3.发送邮件
s = smtplib.SMTP_SSL('smtp.163.com', 465)  # 选择163邮箱服务，默认端口为465
s.login(user, pwd)  # 登录163邮箱
s.send_message(msg)  # 发送邮件
s.quit()
print('Success!')