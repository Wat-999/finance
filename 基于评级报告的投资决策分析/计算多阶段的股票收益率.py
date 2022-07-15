import datetime
import tushare as ts
import pandas as pd

# 1. 数据预处理
# 读取数据、删除重复及空值行
df = pd.read_excel('分析师评级报告.xlsx', dtype={'股票代码': str}) # 注意设置dtype参数，让股票代码以字符串格式读进来
df = df.drop_duplicates()  # 删除重复行
df = df.dropna(thresh=5)  # 删除空值行，thresh=5表示非空值少于5个则删除，本案例因为没有空值行，其实可以不写

# 列拼接、选取合适的列
df['研究机构-分析师'] = df['研究机构'] + '-' + df['分析师']
columns = ['股票名称', '股票代码', '研究机构-分析师', '最新评级', '评级调整', '报告日期']
df = df[columns]

# 定义函数，可以批量获取多阶段的收益率
def fenxi(length):  # 其中length代表时长，如果length=10，则表示10天前
    df_use = df[0:100]  # 这里为了演示，选取了100行数据，如果想获取全部内容，可以改成df_use = df

    # 日期筛选
    today = datetime.datetime.now()
    t = today - datetime.timedelta(days=length)  # 这里设置选取日期的阈值
    t = t.strftime('%Y-%m-%d')
    df_use = df_use[df_use['报告日期'] < t]

    rate = []
    for i, row in df_use.iterrows():
        code = row['股票代码']
        analysist_date = row['报告日期']

        # 1.获取开始日期，也即第二天
        begin_date = datetime.datetime.strptime(analysist_date, '%Y-%m-%d')
        begin_date = begin_date + datetime.timedelta(days=1)
        begin_date = begin_date.strftime('%Y-%m-%d')

        # 2.获取结束日期，也即第三十天
        end_date = datetime.datetime.strptime(analysist_date, '%Y-%m-%d')
        end_date = end_date + datetime.timedelta(days=length)  # 这里设置相隔的时间
        end_date = end_date.strftime('%Y-%m-%d')

        # 3.通过Tushare库计算股票收益率
        ts_result = ts.get_hist_data(code, begin_date, end_date)
        if ts_result is None or len(ts_result) < 10:  # 防止股票没有数据
            return_rate = 0
        else:
            # 防止出现一字涨停现象
            if ts_result.iloc[-1]['low'] == ts_result.iloc[-1]['high'] and abs(ts_result.iloc[-1]['p_change'] - 10.0) < 0.1:
                return_rate = 0
            else:
                start_price = ts_result.iloc[-1]['open']
                end_price = ts_result.iloc[0]['close']
                return_rate = (end_price / start_price) - 1.0
        rate.append(return_rate)

    df_use[str(length) + '天收益率'] = rate  # 这里设置要添加的列
    # 导出为Excel文件
    df_use.to_excel(str(length) + '天收益率-测试.xlsx')  # 生成Excel文件
    return df_use  # 返回值为df_use，这样下面的fenxi(i)就有内容了，可以做进一步的处理


# 上面写的是df_use = df[0:100]  # 这里为了演示，选取了100行数据，如果想获取全部内容，可以改成df_use = df
length = [10, 30]  # 这里为了演示，只获取10天和30天的收益率，需要的话可以将其设置为[10, 30, 60, 90, 180]
for i in length:
    fenxi(i)
    print(fenxi(i))
# 如果让你使用Tushare pro，可以查看www.huaxiaozhi.com上的教程，如果Tushare普通还能获取结果，不用pro也无所谓



# 12.4.3-2 多阶段数据合及导出 by 王宇韬 & 房宇亮
# =============================================================================

import pandas as pd

# 1. 读取数据
a = pd.read_excel('10天收益率.xlsx')
b = pd.read_excel('30天收益率.xlsx')
c = pd.read_excel('60天收益率.xlsx')
d = pd.read_excel('90天收益率.xlsx')
e = pd.read_excel('180天收益率.xlsx')

# 2.合并数据
f = pd.merge(a, b)
g = pd.merge(f, c)
h = pd.merge(g, d)
i = pd.merge(h, e)
'''其中merge()函数会默认以共同的列进行拼接，同时选择内（inner）连接，也即取两表共有的内容，这样会导致前几张表格的数据被剔除掉，
因为有的股票还没有180天收益率的数据。如果想取并集的话，也即把所有数据都获取的话，可以在merge()函数中设置how参数为outer。'''

# 3.删除可能出现的重复值
i = i.drop_duplicates()

# 4.导出为Excel
i.to_excel('多阶段收益率.xlsx')

print(i)
print('多阶段收益率完成！')




