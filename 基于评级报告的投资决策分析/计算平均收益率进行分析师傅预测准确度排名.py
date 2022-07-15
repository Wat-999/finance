import pandas as pd
import datetime
import time
import tushare as ts
import warnings
warnings.filterwarnings("ignore")  # 忽略警告信息，警告不是报错，不会影响程序执行

# 1. 数据预处理
# 读取数据、删除重复及空值行
df = pd.read_excel('/Users/macbookair/Desktop/数据分析/书本配套资料及电子书/python/Python金融/0.《Python金融》最新配套源代码文件（2020-12-07完善）/第12章源代码汇总/分析师评级报告.xlsx',
                   dtype={'股票代码': str}) # 注意设置dtype参数，让股票代码以字符串格式读进来
df = df.drop_duplicates()  # 删除重复行
df = df.dropna(thresh=5)  # 删除空值行，thresh=5表示非空值少于5个则删除，本案例因为没有空值行，其实可以不写

#修改日期格式
# t_list = []  #for循环选出需要数据，存为列表
# for i in df['报告日期']:
# 	i = str(i)
# 	t1 = time.strptime(i, "%Y-%m-%d")   #转换成datetime.datetime格式的日期
# 	t2 = time.strftime("%Y%m%d", t1)  #转换成字符串格式
# 	t_list.append(t2)
#
# df['报告日期'] = t_list  #将列表添加进原本的表格数据中


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

    # 3.通过Tushare库计算股票收益率 #老接口取数失效，采用新接口注意格式：直接用股票序号去匹配无效，格式为：00002.sz
    ts_result = ts.get_hist_data(code, begin_date, end_date)
    if ts_result is None or len(ts_result) < 5:  # 防止股票没有数据
        return_rate = 0
    else:
        start_price = ts_result.iloc[-1]['open']
        end_price = ts_result.iloc[0]['close']
        return_rate = (end_price / start_price) - 1.0
    rate.append(return_rate)

df_use['30天收益率'] = rate  # 该添加列的方式参考6.2.1小节

# 导出为Excel
df_use.to_excel('30天收益率.xlsx')

print(df_use)
print('30天收益率计算完毕！')
# 如果让你使用Tushare pro，可以查看www.huaxiaozhi.com上的教程，如果Tushare普通还能获取结果，不用pro也无所谓

