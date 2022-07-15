#数据乱码的处理
#有些网页的源代码爬取出来会出现中文乱码，即源代码里的中文变成里杂乱的符号，虽然中文乱码的情况较少，
#但是一旦出现就难以进行数据读取。这里以百度为例（为演示编码知识先不加headers，其实很多网站不加headers也能爬取到一些内容）
import requests
url = 'https://www.baidu.com'
res = requests.get(url).text
print(res)
#从运行结果可以看到，爬取到的源代码里有很多乱码，没有我们所需要的中文内容

#编码分析
#在解决乱码问题之前，先分析一下python获得的网页源代码的编码方式，以及网页实际的编码方式，看看两者是否不同
#首先通过requests.get(url).encoding查看python获得的网页源代码的编码方式
import requests
url = 'https://www.baidu.com'
code = requests.get(url).encoding
print(code)   #获得的网页源代码的编码方式为ISO-8859-1
#再来查看网页实际的编码方式：在浏览器中打开网页后按F12键，打开 开发者工具，展开最上上方的<head>标签(<head>标签主要用来存储编码方式、网站标题等信息）
#其中<meta>标签里的charset参数存储的便是网页实际的编码方式，可以看到网页实际的编码方式为utf-8，这与python获取到的ISO-8859-1编码方式不一致
#utf-8，ISO-8859-1都是文本的编码方式，其中utf-8支持中文编码，而ISO-8859-1属于单字节编码，应用于英文系列，无法表示中文字符，这也是python获取的内容出现中文乱码的原因
#此时就需要通过重新编码及解码来解决问题

#重新编码及解码
#编码是指把文本字符串转换为二进制字符(由英文字母和数字组成的原始字符），解码则是指把二进制字符转换为文本字符串
#通过重新编码及解码的方式可以解决乱码问题
res = requests.get(url).text
res = res.encode('ISO-8859-1').decode('utf-8')
#上述代码首先通过encode()函数进行编码，将获取的ISO-8859-1的中文内容转换为二进制字符，然后通过docode()函数解码，把二进制字符转换为网页的实际编码方式utf-8
#这样就把python获取的网页源代码的编码方式变成网页实际的编码方式，从而解决乱码问题。
#并且发现不加headers也能获取一些源代码，如果加上headers则能获取更多的网页源代码
#除来utf-8编码外，国内网页常见的编码方式还有gbk编码，该编码方式也是支持中文的。
#如果通过python获取的网页源代码的编码方式为ISO-8859-1，而网页实际的编码方式为gbk，则可用如下的代码进行处理，其实就是把前面代码中的utf-8换诚gbk
res = requests.get(url).text
res = res.encode('ISO-8859-1').decode('gbk')
#需要注意的是，如果网页实际的编码方式为gbk，而在使用decode()函数解码时设置为utf-8，则会报错。

#知识点  encode()函数和decode()函数
#encode()函数的功能是把字符串装换为原始的二进制字符
res = '华小智'   #中文字符串
res = res.encode('utf-8')
print(res)
#输出结果如下：b'\xe5\x8d\x8e\xe5\xb0\x8f\xe6\x99\xba'可以看到encode()函数将一个字符串转换为来二进制的bytes类型的数据

#decode()函数的功能是把二进制字符串转换为字符串
res = b'\xe5\x8d\x8e\xe5\xb0\x8f\xe6\x99\xba'
res = res.decode('utf-8')
print(res)
#输出结果为华小智  之前所写的res.encode('ISO-8859-1').decode('utf-8')，就是先通过encode('ISO-8859-1')将ISO-8859-1编码方式的
#字符串转换成二进制字符，再通过decode('utf-8')把二进制字符转换成网页实际的编码方式utf-8

#解决乱码问题的经验方法
#方法1：对于大部分网站，可以先尝试常规代码（为来演示编码知识，先不加headers和timeout）
res = requests.get(url).text

#方法2：如果方法1爬取到的内容是乱码，可以试试下面的代码
res = requests.get(url).text
res = res.encode('ISO-8859-1').decode('gbk')

#方法3如果方法2爬取到的内容也是乱码报错，可以再试试下面的代码
res = requests.get(url).text
res = res.encode('ISO-8859-1').decode('utf-8')
#根据众多项目实战经验，导致乱码的大部分原因都是由于python获取的内容是ISO-8859-1编码方式，而网页的实际编码方式是gbk或utf-8
#通过逐个尝试上述3种方法，就可以解决大多数的乱码问题
#如果不想逐个尝试，可以通过try/except语句把三种方法整合到一起
res = requests.get(url).text
try:
    res = res.encode('ISO-8859-1').decode('utf-8')   #方法3
except:
    try:
        res = res.encode('ISO-8859-1').decode('gbk')  #方法2
    except:
        res = res   #方法1
#上述代码到思路其实是让程序来帮你尝试：先在第一个try里尝试方法3，如果失败，就尝试第一个except里第二个try的方法二，如果也失败了，就尝试第2个except里的方法一
#这样就自动把3个方法都尝试里一遍。注意不要把方法1放到第一个try里，因为即使是乱码也不会报错，导致不会执行下面的代码，
#而方法2和方法3如果不成功就会报错，从而可以执行下面的except中的代码。这种方法有一定通用性，不过代码有点不够简洁。