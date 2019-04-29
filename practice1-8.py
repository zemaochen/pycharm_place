from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
d = path.dirname(__file__)                              #获取文件目录，__file__当前文件的上级目录
text = open(path.join(d, 'english.txt')).read()         #读取文件
wordcloud = WordCloud().generate(text)                  # 生成一个词云图像# 生成一个词云图像
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


