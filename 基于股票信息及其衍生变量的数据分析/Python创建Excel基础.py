
import xlwings as xw
import matplotlib.pyplot as plt
import pandas as pd

# 新建一个Excel文件，并设置为不可见
app = xw.App(visible=False)  #visible设置参数为false，让excel程序窗口隐藏在后台运行
wb = app.books.add()      #wb就是新建的excel工作簿

# 创建新工作表
sht = wb.sheets.add('新工作表')
# 将A1单元格改为华小智
sht.range('A1').value = '华小智'

# 导入表格
df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
sht.range('A2').value = df

# 生成图片
fig = plt.figure()
x = [1, 2, 3]
y = [2, 4, 6]
plt.plot(x, y)
# 将产生的图片导入到Excel当中
sht.pictures.add(fig, name='图片1', update=True, left=500)

# 保存生成的Excel文件
wb.save(r'd:\华小智.xlsx')
wb.close()  # 退出工作簿
app.quit()  # 退出程序

print('生成Excel文件成功')
