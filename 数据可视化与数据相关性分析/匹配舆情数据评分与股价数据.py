import pandas as pd
import tushare as ts

# 1 保存股价数据
#pro = ts.pro_api('bfecb1437a0b3b94122ed3b30e9c905e9c4802501a8890f3df2457ed')      #ts.pro_api(注册获得token填在这里)
#data  = pro.daily(ts_code='000002.SZ', start_date='2018-09-01', end_date='2018-12-01')  #股票接口爬取
#data.to_excel('share.xlsx')  # 存储到本地的share.xlsx
#print('数据保存成功')

# 2 匹配估计与舆情评分
score = pd.read_excel('/Users/macbookair/Desktop/数据分析/书本配套资料及电子书/python/Python金融/0.《Python金融》最新配套源代码文件（2020-12-07完善）/第7章源代码汇总/score.xlsx')  # 读取评分数据
share = pd.read_excel('/Users/macbookair/Desktop/数据分析/书本配套资料及电子书/python/Python金融/0.《Python金融》最新配套源代码文件（2020-12-07完善）/第7章源代码汇总/share.xlsx')  # 读取股价数据
share = share[['date', 'close']]  # 只需要股价数据里的日期和收盘价
data = pd.merge(score, share, on='date', how='inner')  # 数据合并，
#on参数为"date"使两张表按日期对齐，设置how参数为"inner"，指定取交集的连接方式，只保留公有部分，share表中没有的日期被剔除。
#这样就一次性完成了数据的剔除与合并。因为merge()函数默认按公共列以取交集的方式连接，所以也可以写成data = pd.mergr(score, share)
data = data.rename(columns={'close': 'price'})  # close列重命名为price;rename修改列名
data.to_excel('data.xlsx', index=False)  # 将结果导出为Excel文件
print('数据合并成功')

