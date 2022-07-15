#异常处理实战
import time

companys = ['阿里巴巴', '万科集团', '百度集团', '腾讯', '京东', '华能信托']
for i in companys:
    try:
        baidu(i)
        print(i + '百度新闻爬取成功')
    except:
        baidu(i)
        print(i + '百度新闻爬取失败')
#如果baidu()函数出现异常，例如在爬取'万科集团'的信息时出现了一个异常的网页结构，就不会因为程序异常而终止整个程序的运行
#而会执行except后的操作，打印输出"万科集团百度新闻爬取失败"

#24小时实时爬取实战
#现在已经可以进行批量爬取并通过异常处理来避免程序中断，倘若要24小时不间断地进行实时爬取，就需要while语句构造一个永久循环
while True:
    companys = ['阿里巴巴', '万科集团', '百度集团', '腾讯', '京东', '华能信托']
    for i in companys:
        try:
            baidu(i)
            print(i + '百度新闻爬取成功')
        except:
            baidu(i)
            print(i + '百度新闻爬取失败')
#这样程序就会24小时不间断地运行下去，而且因为加上来了异常处理语句，就算出现异常信息，整个程序的运行也不会中断
#如果不需要不间断地运行，而是每隔一定时间运行一次，可以引用time库，然后使用time.sleep()函数来达到目的
import time
while True:
    companys = ['阿里巴巴', '万科集团', '百度集团', '腾讯', '京东', '华能信托']
    for i in companys:
        try:
            baidu(i)
            print(i + '百度新闻爬取成功')
        except:
            baidu(i)
            print(i + '百度新闻爬取失败')
    time.sleep(10800)  #括号里的数字单位是秒，即休息10800秒，也就是休息3小时
#这样for循环执行完一遍后，就会自动休息3小时再执行，注意time.sleep(10800)不要写到for循环里去，
#它和for语句的缩进量相同，因为是要等for循环执行完来，才执行time.sleep()


