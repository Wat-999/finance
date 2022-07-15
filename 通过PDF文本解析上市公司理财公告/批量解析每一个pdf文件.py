import pdfplumber
import os

# 1.遍历文件夹中的所有PDF文件
file_dir = r'/Users/macbookair/Desktop/数据分析/书本配套资料及电子书/python/Python金融/0.《Python金融》最新配套源代码文件（2020-12-07完善）/第10章源代码汇总/演示文件夹'
# 也可以改成你自己需要遍历的文件夹绝对路径，例如r'E:\演示文件夹'，这里用的相对路径，也即代码文件所在文件夹下面的内容
file_list = []
for files in os.walk(file_dir):  # 遍历该文件夹及其里面的所有子文件夹
    for file in files[2]:
        if os.path.splitext(file)[1] == '.pdf' or os.path.splitext(file)[1] == '.PDF':# 检查文件后缀名,文件后缀名有可能是小写
            file_list.append(file_dir + '/' + file)  #file_list列表中元素都是文件名，在文本解析时为来调用pdf文件，还需要给文件名加上文件夹路径
print(file_list)

# 2.PDF文本解析和内容筛选
pdf_all = []
for i in range(len(file_list)):
    pdf = pdfplumber.open(file_list[i])
    pages = pdf.pages  #通过pages属性获取所有页的信息，此时pages是一个列表
    text_all = []
    for page in pages:  # 遍历pages中每一页的信息
        text = page.extract_text()  # 提取当页的文本内容
        text_all.append(text)  # 通过列表.append()方法汇总每一页内容
    text_all = ''.join(text_all)  # 把列表转换成字符串
    # print(text_all)  # 打印全部文本内容
    pdf.close()

    # 通过正文进行筛选
    if ('自有' in text_all) or ('议案' in text_all) or ('理财' in text_all) or ('现金管理' in text_all):
        pdf_all.append(file_list[i])
print(pdf_all)  # 打印筛选后的PDF列表

# # 3.筛选后文件的移动
for pdf_i in pdf_all:
    newpath = r'//Users/macbookair/Desktop/数据分析/书本配套资料及电子书/python/Python金融/0.《Python金融》最新配套源代码文件（2020-12-07完善）/第10章源代码汇总/筛选/' + pdf_i.split('/')[-1]
    # 这边这个移动到的文件夹一定要提前就创建好！
    os.rename(pdf_i, newpath)  # 执行文件移动操作

print('PDF文本解析及筛选完毕！')

