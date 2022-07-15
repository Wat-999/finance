#要筛选爬取到的内容，可以if语句把不符合条件的内容都赋值为空字符串，这和第5章数据清洗及数据评分系统搭建中文本内容深度过滤
#例如，只要要日期2018年和2019年的内容，代码如下：
for i in range(len(title)):
    if '2018' in date[i] or '2019' in date[i]:    #2018和2019年的内容
        title[i] = title[i]
        href[i] = href[i]
        date[i] = date[i]
    else:
        title[i] = ''
        href[i] = ''
        date[i] = ''
    #这样不符合日期为2018年或2019年的内容都会被处理为空字符串，不过这些字符串仍然存在于title、href、date列表里，还需要清除。
    #我们利用while循环遍历这些列表，一旦发现有某个元素是空字符串，就用列表的remove()函数把这个元素删除
    while '' in title:
        title.remove('')
    while '' in href:
        href.remove()
    while '' in date:
        date.remove()

    #完整代码如下所示，只需要把该代码放到上一节的代码之后即可
    for i in range(len(title)):
        if '2018' in date[i] or '2019' in date[i]:      #2018和2019年的内容
            title[i] = title[i]
            href[i] = href[i]
            date[i] = date[i]
        else:
            title[i] = ''
            href[i] = ''
            date[i] = ''

    while '' in title:
        title.remove('')
    while '' in href:
        href.remove()
    while '' in date:
        date.remove()

    #利用同样的思路还能对标题进行清洗。如果标题里有某些不想要的关键词，如"保底""刚兑"等，我们就把它赋值为空值后删除，代码如下：
    for i in range(len(title)):
        if '保底' in title[i] or '刚兑' in title[i]:  #
            title[i] = title[i]
            href[i] = href[i]
            date[i] = date[i]
        else:
            title[i] = ''
            href[i] = ''
            date[i] = ''

    while '' in title:
        title.remove('')
    while '' in href:
        href.remove()
    while '' in date:
        date.remove()
#第45行到48行代码其实可以不写，因为如果没有触发if条件，原内容也不需要改变
#需要注意的是，在进行关键词筛选之前，一定要先进行数据清洗，因为未清洗的标题里有很多类似<.*?>的内容，这些内容会分割标题里的文本，
#导致if判断条件失效

