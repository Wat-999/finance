import pandas as pd  #(报错）
import jieba
import re
import matplotlib
import matplotlib.pyplot as plt

# 加载自定义词典
newdict_path = "./source/newdict.txt"  #报错
jieba.load_userdict(newdict_path)

# 加载停用词词典
stop_list = []
stopdict_path = './source/stopdict.txt'
with open(stopdict_path, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        stop_list.append(line[:-1])

data = pd.read_csv('./test.csv')
data['回答'] = data['回答'].apply(lambda x : x.replace('\n', ''))
data['回答'] = data['回答'].apply(lambda x : x.replace(' ', ''))
data['分词'] = data['回答'].apply(lambda x : [i for i in jieba.cut(x) if i not in stop_list])
data['创建时间'] = data['创建时间'].apply(lambda x : x[:10])


all_words = data['分词'].to_list()

word_dict = {}
for words in all_words:
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

from wordcloud import WordCloud
# 生成词云
def create_word_cloud(word_dict):
    # 支持中文, SimHei.ttf可从以下地址下载：https://github.com/cystanford/word_cloud
    wc = WordCloud(
        font_path="./source/SimHei.ttf",
        background_color='white',
        max_words=25,
        width=1800,
        height=1200,
    )
    word_cloud = wc.generate_from_frequencies(word_dict)
    # 写词云图片
    word_cloud.to_file("wordcloud2.jpg")
    # 显示词云文件
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

# 根据词频生成词云
create_word_cloud(word_dict)

