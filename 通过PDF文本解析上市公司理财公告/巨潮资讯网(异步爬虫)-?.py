import requests
import os
import aiohttp
import asyncio
import aiofiles
# 设置请求头
headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (Krow, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
# 创建一个目录用来存储pdf文件
path = '/Users/macbookair/Desktop//股票信息/'
if not os.path.exists(path):
    os.mkdir(path)
    print('文件夹创建成功')
def search():
    """
    搜索函数
    :return: 返回搜索结果并筛选信息
    """
    # 输入搜索关键字
    while True:
        key = input('请输入关键字: ')
        # 设置params参数
        params = {
            'keyWord': key,
            'maxNum': 10}
        url = 'http://www.cninfo.com.cn/new/information/topSearch/query'
        # 发送post请求
        resp = requests.post(url, headers=headers, params=params)
        if resp.json() == []:
            print('该股票不存在请重新输入: ')
            continue
        else:
            break
    # 过滤A股
    search_list = []
    for r in resp.json():
        if r['category'] == 'A股':
            search_list.append(r)
    # 将每只股票写上对应序号
    search_dict = {'0': '再次按下enter键返回到搜索框'}
    num = 1
    for row in search_list:
        search_dict[str(num)] = row
        print('[序号:{}]名称:{}'.format(num, row['zwjc']))
        num += 1
	# 选择想要下载的股票序号
    while True:
        numbers = input('请输入你要选择的股票序号:')
        if search_dict.get(numbers) == None:
            print('你输入的股票序号不存在，请重新输入:')
        elif numbers == '0':
            print(search_dict[numbers])
            continue
        else:
            return search_dict[numbers]



def category(code,orgId):
    """
    分类函数对搜索到的股票信息进行分类筛选
    :param code: 股票代码
    :param orgId: 股票id
    :return: 返回股票报告pdf下载地址
    """
    # 定义分类字典
    category_dict = {'1': 'category_ndbg_szsh',
                     '2': 'category_bndbg_szsh',
                     '3': 'category_rcjy_szsh'}
    while True:
        number = input('请选择你要下载的股票信息分类（1年报 2半年报 3日常经营）: ')
        if number == '1':
            category_search = 'category_ndbg_szsh'
        elif number == '2':
            category_search = 'category_bndbg_szsh'
        elif number == '3':
            category_search = 'category_rcjy_szsh'
        elif category_dict.get(number) == None:
            print('没有你选择的类别，请重新输入')
            continue
        break
    # 深市股票：column : szse  plate : sz
    # 沪市股票: column : sse  plate : sh
    # 通过股票代码启示字符来判断该股票是深市还是沪市
    if str(code).startswith('0') or str(code).startswith('3'):
        column = 'szse'
        plate = 'sz'
    elif str(code).startswith('6'):
        column = 'sse'
        plate = 'sh'
    category_url = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
    # 选择时间段
    startime = input('请输入开始时间（例如:2017-01-01): ')
    endtime = input('请输入结束时间（例如:2019-01-01): ')
    # 搜索结果列表
    result_list = []
    # 搜索页码
    page_num = 1
    while True:
        # 设置data参数
        data = {
        'stock': '{},{}'.format(code, orgId),
        'tabName': 'fulltext',
        'pageSize': '30',
        'pageNum': '{}'.format(page_num),
        'column': column,
        'category': category_search,
        'plate': plate,
        'seDate':'{}~{}'.format(startime, endtime),
        'searchkey':'',
        'secid':'',
        'sortName':'',
        'sortType':'',
        'isHLtitle': 'true',
        }
        resp = requests.post(category_url, data=data, headers=headers)
        if resp.json()['announcements'] == None:
            print('该时间段里没有相关股票信息，请重新输入时间段: ')
            # 选择时间段
            startime = input('请输入开始时间（例如:2017-01-01): ')
            endtime = input('请输入结束时间（例如:2019-01-01): ')
            continue

        for row in resp.json()['announcements']:
            result_list.append([row['announcementTitle'], row['adjunctUrl']])
        # 同返回json数据里的hasMore参数来判断是否需要翻页
        if resp.json()['hasMore'] == 'true':
            page_num += 1
            continue
        # 已经获取所有的数据了结束循环
        break
    return result_list


async def download(name, url):
    """
    文件下载函数
    :param name: 文件名
    :param url: 文件下载地址
    :return:
    """
    download_url = 'http://static.cninfo.com.cn/{}'.format(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(download_url) as resp:
            file = await resp.content.read()
            async with aiofiles.open('{}{}.pdf'.format(path, name), 'wb')as f:
                await f.write(file)
                print('文件下载成功')

async def main():
    """
    主函数，调用其他函数来完成相关操作
    :return:
    """
    # 调用搜索函数，获取搜索结果列表
    search_result = search()
    # 股票代码和股票ID
    code, Id = search_result['code'], search_result['orgId']
    # 调用分类函数获取处理过后的结果列表
    detail_list = category(code, Id)
    # 将下载函数封装成task对象
    tasks = [asyncio.create_task(download(name=item[0], url=item[1])) for item in detail_list]
    # 协程对象进入事件循环
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
    print('所有文件下载完成！')

