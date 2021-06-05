#Author：Alex.Zhang
import synonyms
import jieba
import random
from wordcloud import WordCloud
class Paper(object):
    def __init__(self):
        pass
    def generate(self):
        b = ''
        with open( '222.txt' , 'r' , encoding='utf-8' ) as f:
            for line in f:
                a = line.strip()
                b += a
        text=jieba.cut(b)
        content1 = list( text )
        num=random.randint(0,1)
        for i in range(len(content1)):
            try:
                nearby=synonyms.nearby( content1[i] )
                newvoc=nearby[0][1]
                content1[i]=newvoc
            except IndexError:
                pass
            continue
        newpaper = ''.join( content1 )
        print(newpaper)


    #1.读取文章形成字符串
    #2.jieba分词生成列表
    #3.取出其中的词进行替换
    #4.把词放回去
    #5.把列表重新变成字符串
if __name__=='__main__':
    papa=Paper()
    papa.generate()