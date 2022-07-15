import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

x = np.arange(0, 10, 0.2)  # 生成0-10的一维数组，间隔为0.2
y1 = 3 * x + 5
# y2在y1的基础上进行-5和5之间随机实数波动
y2 = []
for i in y1:
    y2.append(i + random.uniform(-5, 5))

plt.plot(x, y1, color='r', label='y1')
plt.plot(x, y2, linestyle='--', label='y2')
plt.legend(loc='upper left')
plt.show()


corr = pearsonr(y1, y2)
print('相关系数r值为' + str(corr[0]) + '，显著性水平P值为' + str(corr[1]));


# 读取数据
data = pd.read_excel('data.xlsx')
# 相关性分析
corr = pearsonr(data['score'], data['price'])
print('相关系数r值为' + str(corr[0]) + '，显著性水平P值为' + str(corr[1]))

