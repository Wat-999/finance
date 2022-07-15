#策略基本思路
#该策略的基本逻辑如下：成交量的大幅涨跌可能会带来价格的大幅涨跌。这是一个经验策略，当某只股票的当日成交量出现大幅上涨时，
#说明有很多人在关注这只股票，该股票属于活跃股，那么出现价格的大幅涨跌的可能性就较大，从历史交易经验来看也的确如此。
#那么这个经验策略是否具有科学性呢？这就需要通过量化手段来验证了。

#获取股票基本信息数据
import tushare as ts
pro = ts.pro_api('bfecb1437a0b3b94122ed3b30e9c905e9c4802501a8890f3df2457ed')      #ts.pro_api(注册获得token填在这里)
df = pro.daily(ts_code='000002.SZ', start_date='20190201', end_date='20190401')#pro.daily（'股票代码'，start='起始日期'， end='结束日期'）函数获取上市公司万科十年的股票日线级别的数据
#https://tushare.pro/user/token
#老接口支持获取分笔数据
df = ts.get_tick_data(stock_code, date=current_date, src='tt')   #获取分笔数据

#获取当天的前10分钟成交量信息：以万科A(股票代码：000002)为例  (老接口）
stock_code = '000002'   #设置股票代码
current_date = '2019-04-12'  #设置日期
#获取到的是万科A在2019年4月12日的每一笔交易信息，由于我们只需要前10分钟的交易信息，即9：40这一一时刻前（股市通常9：30开盘）的成交量信息
#所以下面通过pandas库提取前10分钟的数据

df = ts.get_tick_data(stock_code, date=current_date, src='tt')
df['time'] = pd.to_datetime(current_date + ' ' + df['time'])
#current_date的日期格式是字符串，但在用dataframe进行日期比较时，只能进行timestamp时间戳格式但日期比较，因此需要通过pd.to_datetime()函数
#将字符串格式的日期转换为timestamp时间戳格式的日期。原来的df['time']里的日期都是时分秒信息，所以这里还需要通过字符串拼接的方式来加上年月日信息
t = pd.to_datetime(current_date).replace(hour=9, minute=40)
#通过pd.to_datetime()函数将current_date转换为timestamp格式，此时默认的时分秒信息为00：00：00，然后通过replace()函数替换小时(hour)
#和分钟(minute)数据，将其设置成2019-04-12 09：40：00的时间戳格式并赋值给变量t(因为要提取的是前10分钟的数据，即09：40：00前的数据）
df_10 = df[df.time <= t] #筛选出前10分钟的数据
df_10.tail()  #用来获取表格的后5行  volume列即成交量，单位为手

#获取到前10分钟的分笔数据后，就可以通过sum()函数将每笔成交数据中的成交量求和，得到前10分钟的总成交量
vol = df_10.volume.sum()
#有读者可能会疑惑：为什么不直接通过ts.get_realtime_quotes('000002')调用前10分钟的实时数据来获取成交量，而是通过分笔数据进行求和统计？
#因为通过实时数据只能获取当天当时的信息，而通过分笔数据则能获取各个历史时期的各个时间段的信息，更便于对策略进行评估，该评估也称为策略回测

#获取多天的前10分钟成交量及每日基本行情信息
#除来单天的前10分钟成交信息，还需要获取多天的前10分钟成交信息来统计成交量的变化，以及每日开盘价及收盘价等基本信息

#首先Tushare库获取万科A从2019年2月1日到2019年4月1日的每日行情数据，代码如下：
import tushare as ts
import pandas as pd
stock_code = '00002'
stock_date = '万科A'
start_date = '2019-02-01'  #设置起始日期
end_date = '2019-04-01'    #设置终止日期
#时间区间内的股票k线图，用于提取开盘价等有用信息
stock_k = ts.get_hist_data(stock_code, start=stock_date, end=end_date)
#运行结果：其中open为开盘价，high为最高价，close为收盘价，low为最低价，volume为成交量，price_change为价格变化(今日收盘价-昨日收盘价),
#ma5为5日均线价格，v_ma5为5日均线成交量
#获得每日行情数据后，根据其日期索引并结合上一小节获取单日前10分钟交易数据的代码，获取各个日期的前10分钟交易数据，接着上面的代码补充如下内容：


#建立一个新的dataframe，用于存储当前股票信息
stock_table = pd.DataFrame()

#遍历日期索引，提取需要的数据
for current_date in stock_k.index:
    #通过loc选中k线图中对应current_date这一天的数据
    current_k_line = stock_k.loc[current_date]

    #提取这一天的前10分钟交易数据
    df = ts.get_tick_data(stock_code, date=current_date, src='tt')
    f['time'] = pd.to_datetime(current_date + ' ' + df['time'])
    # current_date的日期格式是字符串，但在用dataframe进行日期比较时，只能进行timestamp时间戳格式但日期比较，因此需要通过pd.to_datetime()函数
    # 将字符串格式的日期转换为timestamp时间戳格式的日期。原来的df['time']里的日期都是时分秒信息，所以这里还需要通过字符串拼接的方式来加上年月日信息
    t = pd.to_datetime(current_date).replace(hour=9, minute=40)
    # 通过pd.to_datetime()函数将current_date转换为timestamp格式，此时默认的时分秒信息为00：00：00，然后通过replace()函数替换小时(hour)
    # 和分钟(minute)数据，将其设置成2019-04-12 09：40：00的时间戳格式并赋值给变量t(因为要提取的是前10分钟的数据，即09：40：00前的数据）
    df_10 = df[df.time <= t]  # 筛选出前10分钟的数据
    df_10.tail()  # 用来获取表格的后5行  volume列即成交量，单位为手
    vol = df_10.volume.sum()   #通过sum()函数求和

    #将数据存储到字典中
    current_stock_info = {'名称': stock_name,
                          '日期': pd.to_datetime(current_date),
                          '开盘价': current_k_line.open,
                          '收盘价': current_k_line.close,
                          '股价涨幅': current_k_line.p_change,
                          '10分钟成交量': vol
                          }

    #通过append()函数增加新的一行，忽略索引
    stock_table = stock_table.append(current_stock_info, ignore_index=True)

    #通过set_index()函数将'日期'列设置为索引
    stock_table = stock_table.set_index('日期')  #打印结果里的"股价涨跌幅(%)"为百分数，

    #如果想调整列的顺序，可以使用如下代码：
    order = ['名称', '开盘价', '收盘价', '股价涨跌幅', '10分钟成交量']
    stock_table = stock_table[order]
