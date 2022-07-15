#本节将通过Tushare库调用股票历史数据，计算券商分析师评级后股票一段时间内的价格涨跌幅，
#从而评估分析师的预测准确度。这里选取分析师预测之后30天内的股票涨跌幅作为判断标准。

import pandas as pd
df = pd.read_excel('/Users/macbookair/Desktop/数据分析/书本配套资料及电子书/python/Python金融/0.《Python金融》最新配套源代码文件（2020-12-07完善）/第12章源代码汇总/分析师评级报告.xlsx',
                   dtype={"股票代码": str})
#需要注意的是，"股票代码"列的值是内容为一串数字的字符串，在读取时要利用dtype参数把该列的数据类型设置为str(字符串类型),否则pandas库会默认将它读取成数值类型
#导致以0开头的股票代码在读取后丢失开头的0。例如，万科集团的股票代码"00002"会被读取成"2"，导致之后通过Tushare库查询股票代码失败。

#删除重复行和空行
#有时数据表里可能有一些重复行或大量空值
df = df.drop_duplicates()  #删除重复行
df = df.dropna(thresh=5)  #阀值参数thresh=5，表示 如果该行的非空值少于5个，则将该行删除

#连接"研究机构"和分析师列作为一个整体名称
df['研究机构-分析师'] = df.apply(lambda x: x['研究机构'] + '-' + x['分析师傅'], axis=1)
#其含义是对每一行取"研究机构"和"分析师"这两列的值，并用"-"号将两个字符串连接起来，组成一个新的列，axis=1则表示按行的方向进行数据选择
#还有一种更简单的方法来进行两列数据的字符串拼接，代码如下：
df['研究机构-分析师'] = df['研究机构'] + '-' + df['分析师傅']

#选取需要的列
columns = ['股票名称', '股票代码', '研究机构-分析师', '最新评级', '评级调整', '报告日期']
df = df[columns]

#筛选日期
#因为是以预测之后30天内的股票涨跌幅作为判断标准，如果报告日期距当前日期不满30天，就没有足够时长的交易数据，所以需要将30天内的股票数据 剔除
import datetime
today = datetime.datetime.now()  #获取当前日期，返回一个datetime对象
t = today - datetime.datetime(days=30)   #datetime.datetime(days=30)表示一个30天的时间差。
#用当前日期today减去这个时间差就是30天前的日期，将它赋值给变量t，作为日期筛选的阀值
t = t.strftime('%Y-%m-%d') #用strftime()函数将datetime对象转换成对应的字符串格式，这里需要将t转换成和表格中"报告日期"列相同的日期格式
#和strftime()函数相对应的是strptime()函数，作用是将字符串格式的日期转换成datetime对象
df = df[df['报告日期'] < t]  #进行日期筛选

#数据预处理完整代码如下：
import pandas as pd
import datetime

#读取数据，并删除重复及空值行
df = pd.read_excel('/Users/macbookair/Desktop/数据分析/书本配套资料及电子书/python/Python金融/0.《Python金融》最新配套源代码文件（2020-12-07完善）/第12章源代码汇总/分析师评级报告.xlsx',
                   dtype={"股票代码": str})#需要注意的是，"股票代码"列的值是内容为一串数字的字符串，在读取时要利用dtype参数把该列的数据类型设置为str(字符串类型),
df = df.drop_duplicates()  #删除重复行
df = df.dropna(thresh=5)  #阀值参数thresh=5，表示 如果该行的非空值少于5个，则将该行删除

#列拼接，并选取需要的列
df['研究机构-分析师'] = df['研究机构'] + '-' + df['分析师傅'] #列字符串数据拼接
columns = ['股票名称', '股票代码', '研究机构-分析师', '最新评级', '评级调整', '报告日期']  #选取需要的列
df = df[columns]

#日期筛选
today = datetime.datetime.now()  #获取当前日期，返回一个datetime对象
t = today - datetime.datetime(days=30)   #datetime.datetime(days=30)表示一个30天的时间差。
#用当前日期today减去这个时间差就是30天前的日期，将它赋值给变量t，作为日期筛选的阀值
t = t.strftime('%Y-%m-%d') #用strftime()函数将datetime对象转换成对应的字符串格式，这里需要将t转换成和表格中"报告日期"列相同的日期格式
#和strftime()函数相对应的是strptime()函数，作用是将字符串格式的日期转换成datetime对象
df = df[df['报告日期'] < t]  #进行日期筛选