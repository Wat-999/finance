#将舆情数据评分存入数据库
#要将舆情数据评分存入数据库，首先需要创建数据表，然后编写相应的代码
#1.查询数据，为之后的数据去重准备
sql_1 = 'SELECT * FROM article WHERE company =%s'  # 按公司名称选取数据
cur.execute(sql_1, company)       # 执行sql语句，选取公司名称为company的数据
data_all = cur.fetchall()         # 提取所有数据
title_all = []                    # 创建一个空列表用来存储新闻标题
for j in range(len(data_all)):     #遍历提取到的数据
    title_all.append(data_all[j][1])  #将数据中的新闻标题存入列表