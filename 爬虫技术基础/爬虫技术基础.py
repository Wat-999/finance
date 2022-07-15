#正则表达式
import re   #导入正则表达式库
content = 'hello 123 world'
result = re.findall('\d\d\d', content)  # findall函数的功能是在原始文本中寻找所有符合匹配规则的文本内容re.findall(匹配规则, 原始文本)
#匹配规则是一个由特定符号组成的字符串，上述中使用的匹配规则中'\d'就是一个特定符号，表示匹配一个数字，那么'\d\d\d'就表示匹配3个数字
#所以re.findall('\d\d\d', content) 就是在content中寻找连续的3个数字
#注意findall函数得到的是一个列表，而不是字符串或数字
print(result);

import re
content = 'Hello 123 world 456 华小智Python基础教学135'
result = re.findall('\d\d\d',content)
print(result)

# 注意获取到的是一个列表
print(result[0])
print(result[1])
print(result[2])

# 更简单的遍历方法，其中len表示列表长度，range(n)表示0到n-1
for i in range(len(result)):
    print(result[i])


#正则表达式匹配规则
#符号                 功能说明
#\d         匹配1个数字字符
#\w         匹配1个字母、数字或下画线字符
#\s         匹配1个空白字符，如换行符、制表符、普通空格等
#\S         匹配1个非空白字符
#\n         匹配一个换行符，相当于按一次enter键
#\t         匹配1个制表符，相当于按一次Tab键或按8次空格键
#.          匹配1个任意字符，换行符除外
#*          匹配0个或多个表达式
#+          匹配1个或多个表达式
#？         非贪婪限定符，常与.和*配合使用
#()         匹配括号内的表达式，也表示一个组
#将这些符号组合起来，就能得到千变万化的匹配规则。不过在金融数据挖掘与分析实战中大部分情况下需要用到的只有两种：(.*?)与.*?

#正则表达式基础2——非贪婪匹配之(.*?)
#'.'表示除了换行符外的任意字符，'*'表示0个或多个表达式。将'.'和'*'合在一起组成的匹配规则'.*'称为贪婪匹配，之所以叫贪婪匹配，
#是因为会匹配到过多的内容。如果再加上一个'？'构成'.*？'，就变成了非贪婪匹配，它能比较精确地匹配到想要的内容。

#简单来说(.*?)用于获取文本a和文本B之间的内容，并不需要知道它的确切长度及格式，但是需要知道它在哪两个内容之间使用格式：文本A(.*?)文本B
#下面结合findall函数和非贪婪匹配(.*?)进行文本提取的演示
import re
res = '文本A百度新闻文本B'
source = re.findall('文本A(.*?)文本B', res)
print(source);

#在实战中,一般不把匹配规则直接写到findall括号里，而是拆成两行来写，先写匹配规则，在写findall语句。原因是有时匹配规则较长，分开写比较清晰
import re
res = '文本A百度新闻文本B, 新闻标题文本A新浪财经文本B，文本A搜狗新闻文本B新闻网站 '  #匹配文本
p_source = '文本A(.*?)文本B'   #写匹配规则并将其赋值
source = re.findall(p_source, res)
print(source)

#正则表达式基础3——非贪婪匹配之.*？
#(.*?)用于获取文本A与文本B之间的内容，.*?是用于代替文本C与文本D之间的所有内容。之所以用.*?，是因为文本C和文本D之间的内容经常变动或没有规律
#无法写到匹配规则里；或者文本C与文本D之间的内容较多，我们不想写到匹配规则里，.*?的使用格式：文本C.*?文本D
import re
res = '<h3>文本C<变化的网址>文本D新闻标题</h3>'
p_title = '<h3>文本C.*?文本D(.*?)</h3>'
title = re.findall(p_title, res)
print(title);
#文本c和文本d之间为变化的网址，用.*/?代表，需要提取的是文本D</h3>之间的内容，用(.*?)代表

import re
res = '<h3 class="c-title"><a href="网址" data-click="{一堆英文}"><em>阿里巴巴</em>代码竞赛现全球首位AI评委 能为代码质量打分</a>'
p_title = '<h3 class="c-title">.*?>(.*?)</a>'
title = re.findall(p_title, res)
print(title)
#p_title = '<h3 class="c-title">.*?>(.*?)</a>'  匹配规则解读
#<h3 class="c-title">  注释属于文本A
#.*?>   注释用于填充我们不关系的内容
#(.*?)  注释此处为新闻标题，也就是我们关心的内容
#</a>   注释文本B
#其中文本A、文本B及(.*?)的作用是定位到我们关心的内容——新闻标题。而文本A中的.*?则代表在<h3 class="c-title">和>之间我们不关心的内容
#同理获取新闻链接，<h3 class="c-title"><a href="相当于文本A，右边的双引号"相当于文本B
p_href = '<h3 class="c-title"><a href="(.*?)"'
href = re.findall(p_href, res)
print(href)
#以上的演示代码都没有考虑换行的情况，但实际的网页源代码里存在很多换行，而(.*?)和.*?无法自动匹配换行，如遇到换行就不会继续匹配换行之后的内容了就需要用到修饰符re.s

#正则表达式基础4——自动考虑换行的修饰符re.S
#修饰符有很多，最常用的是re.S，其作用是在使用findall()查找时，可以自动考虑到换行的影响，使得.*?可以匹配换行，使用格式：re.findall(匹配规则，匹配文本，re.S)
import re
res = '''文本A
      百度新闻文本B'''
p_source = '文本A(.*?)文本B'
source = re.findall(p_source, res, re.S)
print(source)
#由于文本A和文本B之间有换行，如果在findall后的括号中不写re.S，则获取不到内容，因为(.*?)匹配不了换行。之前讲过3个单引号'''一般用来注释，
#而这里用来将带有换行的文本框起来

#从百度新闻网页源代码中提取新闻标题和链接
import re
res = '''<h3 class="c-title">
 <a href="https://baijiahao.baidu.com/s?id=1631161702623128831&amp;wfr=spider&amp;for=pc"
    data-click="{
      一堆我们不关心的英文
      }"
                target="_blank"
    >
      <em>阿里巴巴</em>代码竞赛现全球首位AI评委 能为代码质量打分
    </a>
'''

p_href = '<h3 class="c-title">.*?<a href="(.*?)"'
#在<h3 class="c-title">加了一个.*?,这是因为这里的网页源代码存在换行，所以<h3 class="c-title">后面其实是有换行符和一些空格的，
#因此要用.*?填充这些并不需要的换行符和空格
p_title = '<h3 class="c-title">.*?>(.*?)</a>'
href = re.findall(p_href, res, re.S)   #加re.S使.*?能够匹配换行
title = re.findall(p_title, res, re.S)
print(href)
print(title)

# 清除换行符号
for i in range(len(title)):
    title[i] = title[i].strip() #strip()函数主要的作用是删除空白字符(包括换行"\n"和空格字符""）
print(title)

#正则表达式基础5——知识点补充
#sub()函数中sub是英文substitute(替换）的缩写，其格式为：re.sub(需要替换的内容，替换值，原字符串）。主要用于清洗正则表达式获取到的内容
#如之前获取到的无效内容新闻标题：['<em>阿里巴巴</em>代码竞赛现全球首位AI评委 能为代码质量打分']
#其中<em>和</em>并不是我们需要的内容。通过如下代码将其替换为空值，及将其删除。注意代码中的title是一个列表，虽然只有一个元素
#但也要用title[0]才能获得其中的字符串,然后才可以使用sub()函数进行清洗

import re
title = ['<em>阿里巴巴</em>代码竞赛现全球首位AI评委 能为代码质量打分']
title[0] = re.sub('<em>', '', title[0])
title[0] = re.sub('</em>', '', title[0])
print(title[0])
#这里采用的替换方式类似于replace()函数，即依次替换特定的字符串。这种方式的缺点是得为每一个替换的字符串写一行替换代码，工作量就会很大
#此时可以观察要替换的字符串，如果它们有类似的格式，就可以用sub()函数通过正则表达式进行批量替换。
import re
title = ['<em>阿里巴巴</em>代码竞赛现全球首位AI评委 能为代码质量打分']
title[0] = re.sub('<.*?>', '', title[0])  #'<.*?>'由于.*?用于代表文本C和文本D之间的所有内容，所以<.*?>就表示任何<xxxx>形式的内容
print(title[0])

#中括号[]的用法
#中括号最主要的功能是使中括号里的内容不再有特殊含义。在正则表达式里，".""*""?"等符号都有特殊含义，但是如果想定位的就是这些符号，
#就需要用中括号。例如，想把字符串里所有的"*"号都替换成空值
company = '*华能信托'
company1 = re.sub('[*]', '', company)
print(company1)