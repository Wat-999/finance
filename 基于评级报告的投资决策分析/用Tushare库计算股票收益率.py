#本小节通过tushare库获取历史股价数据，并根据历史股价数据计算30天内的股票收益率，计算公式：收益率=(结束日的收盘价格/开始日的开盘价格) - 1.0

#确定列开始日和结束日，就可以进行股票收益率的计算，演示代码如下：
import pandas as pd
import tushare as ts
pro = ts.pro_api('bfecb1437a0b3b94122ed3b30e9c905e9c4802501a8890f3df2457ed')      #ts.pro_api(注册获得token填在这里)
#在Tushare pro 数据接口里，股票代码参数都叫ts_code，每种股票代码都有规范的后缀
#pro.daily（'股票代码'，start='起始日期'， end='结束日期'）函数获取上市公司万科十年的股票日线级别的数据
ts_result = pro.daily(ts_code='000002.SZ', start_date='20090102', end_date='20190131')  #股票接口爬取
#ts_result = ts_result.sort_index(ascending=True)   #可以将时间顺序升序，
start_price = ts_result.iloc[-1]['open']
end_prince = ts_result.iloc[0]['close']
return_rate = (end_prince / start_price) - 1.0
print(return_rate)
ts_result.to_excel('gupiao.xlsx')  #导出excel数据
#通过pro.daily()函数可以获得历史行情数据，数据按日期由近到远排序，所以：开始日到开盘价格为ts_result.iloc[-1]['open']，即倒数第1行的open列
#结束日的收盘价格为ts_result.iloc[0]['close']，即第1行的close列

#上面的日期是固定的，然而分析师评级报告的发布日期并不确定，要根据该日期推算除第2天的日期(从第2天开始买股票)及第30天后的日期，
#则需要引用datetime库进行日期的推算。这里先来演示第2天的日期的推算，代码如下：
import datetime
analysist_date = '2019-01-01'  #分析师发布报告的日期
analysist_date = analysist_date.replace('-', '')  #用replace()函数替换成'20190101'
begin_date = datetime.datetime.strptime(analysist_date, '%Y%m%d')  #用strptime()函数将原来字符串格式日期转换成datetime.datatime格式的日期
begin_date = begin_date + datetime.timedelta(days=1)
#datetime.timedelta()函数为当前日期加上1天，其中days参数表示要加上的天数，如果是30则白噢是30天后，-1则表示昨天
begin_date = begin_date.strftime('%Y%m%d')#推算出的第二天日期通过strftime()函数由datetime.datetime格式转换成字符串格式

#同理，可以通过下面的代码推算第30天后的日期
begin_date = datetime.datetime.strptime(analysist_date, '%Y%m%d')  #用strptime()函数将原来字符串格式日期转换成datetime.datatime格式的日期
begin_date = begin_date + datetime.timedelta(days=30)
#datetime.timedelta()函数为当前日期加上1天，其中days参数表示要加上的天数，如果是30则白噢是30天后，-1则表示昨天
begin_date = begin_date.strftime('%Y%m%d')#推算出的第二天日期通过strftime()函数由datetime.datetime格式转换成字符串格式


#获得开始日和结束日后，就可以利用如下代码计算收益率：

import datetime
import tushare as ts
# 2.通过Tushare库计算股票收益率
df_use = df.iloc[0:100]  # 为了演示选取了前100行，想运行全部可写df_use = df
rate = []  # 创建一个空列表，用来存储每支股票的收益率

for i, row in df_use.iterrows():
    code = row['股票代码']
    analysist_date = row['报告日期']

    # 1.获取开始日期，也即第二天
    begin_date = datetime.datetime.strptime(analysist_date, '%Y-%m-%d')
    begin_date = begin_date + datetime.timedelta(days=1)
    begin_date = begin_date.strftime('%Y-%m-%d')

    # 2.获取结束日期，也即第三十天
    end_date = datetime.datetime.strptime(analysist_date, '%Y-%m-%d')
    end_date = end_date + datetime.timedelta(days=30)
    end_date = end_date.strftime('%Y-%m-%d')

    # 3.通过Tushare库计算股票收益率
    ts_result = ts.get_hist_data(code, begin_date, end_date)
    start_price = ts_result.iloc[-1]['open']
    end_price = ts_result.iloc[0]['close']
    return_rate = (end_price / start_price) - 1.0
    rate.append(return_rate)

df_use['30天收益率'] = rate  #添加列

#这里介绍一下iterrows()函数，它用来遍历dataframe的每一行，演示代码如下
for i, row in df_use.iterrows():
    print(i)
    print(row)
#上述代码中的i就是每一行的行索引号，row就是每一行的内容，该内容是一个一维结构series对象，通过row['股票代码']及row['报告日期']就可以提取相应内容
#上面计算每只股票收益率的代码里的变量row就是从df_use.iterrows()循环得到的

#作为演示，df_use只选取了前100行数据，如果要处理大批量数据，还有一些特殊情况需要考虑。例如，有时用tushare库可能获取不到数据，导致ts_result为空值
#这时就无法执行获取股票价格的代码，我们可以通过如下代码处理这种特殊情况：
    if ts_result is None or len(ts_result) < 5:  # 防止股票没有数据
        return_rate = 0
    else:
        start_price = ts_result.iloc[-1]['open']
        end_price = ts_result.iloc[0]['close']
        return_rate = (end_price / start_price) - 1.0
    #如果没有获取到数据，即ts_result为none，或者获取到的数据太少，即len(ts_result) < 5，那么就让return_rate = 0
    #如果获取到了数据，则执行计算收益率

#首先计算每个分析师所推荐股票的30天平均收益率
means = df_use.groupby('研究机构-分析师')[['30天收益率']].mean()  #注意用两层[[]]，这样获得的才是dataframe
#计算出各分析师所有预测股票的平均收益率后，还需要关心分析师的预测次数，可使用count()函数根据分组计数，也就统计出率分析师的预测次数
count = df_use.groupby('研究机构-分析师')[['30天收益率']].count()
#这里列名还是30天收益率，需要更改列名
count = count.rename(columns={'30天收益率': '预测次数'})
#通过rename()函数进行重命名时并没有改变原表格的结构，所以需要重新赋值，或者在rename()函数中设置inplace参数为True
#此时获得的means和count这两个dataframe有着同样的行索引，可以通过merge()函数或concat()函数，根据行索引将两个dataframe拼接到一起

#方法1——用merge()函数合并，注意要设置left_index和right_index参数，按行索引合并
df_final = pd.merge(means, count, left_index=True, right_index=True )

#方法2——通过concat()函数合并，注意要设置axis参数为1，进行横向合并
df_final = pd.concat([means, count], axis=1)

#用sort_values()函数对预测准确度进行排序，其不改变原表结构，所以需要设置inplace参数为true，或将其重新赋值给原表格
#这里选择的是设置inplace参数为true
df_final.sort_values(by='30天收益率', ascending=False, inplace=True)


