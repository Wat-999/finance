#在python中实现定时任务的两种方法：第一种是利用while True循环配合time.sleep()函数来实现，其代码简单，但是效果比较粗糙，仅供学习
#第二种则是利用Schedule库来实现，效果会更加精确

#利用while True循环实现每天定时发送邮件
import smtplib
import time
from email.mime.text import MIMEText
usre = 'qq号码'
pwd = '你自己的SMTP授权码'
to = '收件人的邮箱'

while True:
    #这里省略的是提取数据及发送邮件的代码

    time.sleep(86400)   #一天共86400秒
#使用 while True可一直执行提取数据及发送邮件的代码，time.sleep(86400)用于在提取数据及发送邮件后等待86400秒(及一天的秒数)。
#例如，在下午5点运行上述代码，那么第二天下午5点就会自动在此执行该代码，从而实现每天发送。这个方法的缺陷在于程序运行需要时间，所以会有延迟，
#导致每天的发送时间并不精确，只适合对时间精确度没有太高要求的场合

#利用Schedule库实现每天定时发送邮件(schedule是时刻表的意思）
#schedule库的使用并不复杂，需要和一个定义好的函数相配合。下面以每天中午12点打印输出"该吃饭啦"为例
import schedule
import tie

def eating():
    print("该吃饭啦")

schedule.every().day.at("12:00").do(eating)  #中at后的括号里是执行时间，do后的括号里是需要执行的函数

while True:
    schedule.run_pending() #为运行所有可以运行的schedule任务
    time.sleep(10)  #让schedule任务运行完后休息10秒钟在检测是否有可以运行的任务
#上述代码定义一个名为eating的函数，该函数没有参数，功能为打印输出"该吃饭啦"，然后让程序每天中午12：00执行eating()函数，核心代码如下：
#schedule.every().day.at("12:00").do(eating)，其中at后的括号里是执行时间，do后的括号里是需要执行的函数

#定义里执行时间和函数后，还需要通过while True让程序一直运行。schedule.run_pending()的含义为运行所有可以运行的schedule任务，
#time.sleep(10)是让schedule任务运行完后休息10秒钟在检测是否有可以运行的任务，也可以直接写成time.sleep(1)。在上述代码中，
#当到里每天的12：00时，就会检测到可执行的schedule任务——运行eating()函数，并执行该任务


#除里每天定时执行任务，schedule库还可以执行其他类型的定时任务，例如，每隔10分钟执行一次任务、每隔一小时执行一次任务、每周一的12：00执行一次任务
import schedule
import time
def eating():
    print("该吃饭呢")

#每隔10分钟执行一次任务
schedule.every(10).minutes.do(eating)

#每隔1小时执行一次任务
schedule.every().hour.do(eating)

#每周一的12：00执行一次任务
schedule.every().monday.at('12:00').do(eating)

while True:
    schedule.run_pending()
    time.sleep(10)

#如果函数带有参数，可以把参数写到do后面的括号里的函数名称后面，代码如下
import schedule
import time


def eating(name):
    print(name + "该吃饭呢")

name = "华小智"

# 每周一的12：00执行一次任务
schedule.every().monday.at('12:00').do(eating, name)

while True:
    schedule.run_pending()
    time.sleep(10)