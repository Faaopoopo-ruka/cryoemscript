# # #Author：Alex.Zhang
# from wordcloud import WordCloud
# # # 获取文本词排序，可调整 stopwords
# # process_word = WordCloud.process_text(wc,text)
# # sort = sorted(process_word.items(),key=lambda e:e[1],reverse=True)
# # print(sort[:50]) # 获取文本词频最高的前50个词
# # # 结果
# # stopwords = set(STOPWORDS)
# # stopwords.add('one')
# with open("2.txt" ,encoding="utf-8")as file:
#     #1.读取文本内容
#     text=file.read()
#     #2.设置词云的背景颜色、宽高、字数
#     wordcloud=WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",
#     background_color="black",width=600,
#     height=300,max_words=50).generate(text)
#     #3.生成图片
#     image=wordcloud.to_image()
#     #4.显示图片
#     image.show()
# from wordcloud import WordCloud
# import jieba
# # #1.将字符串切分为单个字符
# def chinese_jieba(text):
#     wordlist_jieba=jieba.cut(text)
#     space_wordlist=''.join(wordlist_jieba)
#     return  space_wordlist
# with open("2.txt" ,encoding="utf-8")as file:
#     text=file.read()
#     text=chinese_jieba(text)
#     wordcloud = WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",
#                           background_color="black", width=600,
#                           height=300, max_words=50,min_font_size=8).generate(text)
#     wordcloud.to_file('110.png')
#     image=wordcloud.to_image()
#     image.show()

# # import os
# # from os import path
# # import numpy as np
# # from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
# # from PIL import Image
# # from matplotlib import pyplot as plt
# # from scipy.misc import imread
# # import random
#
# # def wc_english():
# #     # 获取当前文件路径
# #     d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
# #     # 获取文本text
# #     with open("2.txt" ,encoding="utf-8")as file:
# #         #1.读取文本内容
# #         text=file.read()
# #     # 读取背景图片
# #     #     #2.设置词云的背景颜色、宽高、字数
# #     #     wordcloud=WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",
# #     #     background_color="black",width=600,
# #     #     height=300,max_words=50).generate(text)
# #     # 设置英文停止词
# #     stopwords = set(STOPWORDS)
# #     stopwords.add( 'nucleosome' )
# #     stopwords.add( 'using' )
# #     stopwords.add( 'peformed' )
# #     stopwords.add( 'stored' )
# #     stopwords.add( 'nucleosome' )
# #     aa=['containing','purified','PilTGm','described','minutes','followed',
# #         'et','al','used']
# #     for i in aa:
# #         stopwords.add(i)
# #     wc = WordCloud(
# #         margin = 2, # 设置页面边缘
# #         scale = 4,
# #         max_words = 150, # 最多词个数
# #         min_font_size = 4, # 最小字体大小
# #         width=1024,
# #         height=1024,
# #         stopwords = stopwords,
# #         random_state = 42,
# #         background_color = 'white', # 背景颜色
# #         max_font_size = 150, # 最大字体大小
# #         )
# #     # 生成词云
# #     wc.generate_from_text(text)
# #     # 等价于
# #     # wc.generate(text)
# #     # 根据图片色设置背景色
# #
# #     #存储图像
# #     wc.to_file('1900pro1.png')
# #     # 显示图像
# #     plt.imshow(wc,interpolation='bilinear')
# #     plt.axis('off')
# #     plt.tight_layout()
# #     plt.show()
# # wc_english()
from wordcloud import WordCloud

import matplotlib.pyplot as plt #绘制图像的模块

import jieba #jieba分词

path_txt='2.txt'

f = open(path_txt,'r',encoding='UTF-8').read()

# 结巴分词，生成字符串，wordcloud无法直接生成正确的中文词云

cut_text = " ".join(jieba.cut(f))

wordcloud = WordCloud(

#设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的

font_path="C:/Windows/Fonts/simfang.ttf",

#设置了背景，宽高

background_color="white",width=1000,height=880).generate(cut_text)

wordcloud.to_file('119.png')
plt.imshow(wordcloud, interpolation="bilinear")

plt.axis("off")

plt.show()