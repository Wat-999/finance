import datetime
import pandas as pd
import matplotlib.pyplot as plt

# 设置中文格式为黑体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
data = pd.read_excel('data.xlsx')

#  把日期由string字符串格式转为timestamp时间戳格式，方便坐标轴显示
d = []
for i in range(len(data)):
    d.append(datetime.datetime.strptime(data['date'][i], '%Y-%m-%d'))
data['date'] = d  # 将原来的date那一列数据换成新生成的时间戳格式日期

#  数据可视化并设置双坐标轴
plt.plot(data['date'], data['score'], linestyle='--', label='分数')
plt.xticks(rotation=45)  # 设置x轴刻度显示角度
plt.legend(loc='upper left')  # 分数的图例设置在左上角
plt.twinx()  # 设置双坐标轴
plt.plot(data['date'], data['price'], color='red', label='价格')
plt.xticks(rotation=45)    # 设置x轴刻度显示角度
plt.legend(loc='upper right')  #价格的图例设置在右上角
plt.show()

