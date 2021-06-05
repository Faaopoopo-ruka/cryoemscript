from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
import pandas as pd
stopwords = set(stopwords.words('english') + list(punctuation))
max_cut = 0.9
min_cut = 0.1

"""
计算出每个词出现的频率
word_sent 是一个已经分好词的列表
返回一个词典freq[],
freq[w]代表了w出现的频率
"""


def compute_frequencies(word_sent):
    """
    defaultdict和普通的dict
    的区别是它可以设置default值
    参数是int默认值是0
    """
    freq = defaultdict( int )

    # 统计每个词出现的频率
    for s in word_sent:
        for word in s:
            # 注意stopwords
            if word not in stopwords:
                freq[word] += 1
    print(freq)
    # 得出最高出现频次m
    m = float( max( freq.values() ) )
    print(m)
    # 所有单词的频次统除m
    for w in list( freq.keys() ):
        freq[w] = freq[w] / m
        if freq[w] >= max_cut or freq[w] <= min_cut:
            del freq[w]
    # 最后返回的是
    # {key:单词, value: 重要性}
    return freq


def summarize(text , n):
    """
    用来总结的主要函数
    text是输入的文本
    n是摘要的句子个数
    返回包含摘要的列表
    """

    # 首先先把句子分出来
    sents = sent_tokenize( text )


    # 然后再分词
    word_sent = [word_tokenize( s.lower() ) for s in sents]
    # freq是一个词和词重要性的字典
    #天秀行列转置
    freq = compute_frequencies( word_sent )
    ls = pd.DataFrame(freq, index=[0])
    aa=ls.stack()
    aa = aa.unstack( 0 )
    aa = aa.to_csv( 'labels.csv' , index=True )
    print(freq)
    # ranking则是句子和句子重要性的词典
    ranking = defaultdict( int )
    for i , word in enumerate( word_sent ):
        for w in word:
            if w in freq:
                ranking[i] += freq[w]
    sents_idx = rank( ranking , n )
    print(ranking)
    print(sents_idx)
    return [sents[j] for j in sents_idx]


"""
考虑到句子比较多的情况
用遍历的方式找最大的n个数比较慢
我们这里调用heapq中的函数
创建一个最小堆来完成这个功能
返回的是最小的n个数所在的位置
"""


def rank(ranking , n):
    return nlargest( n , ranking , key=ranking.get )

if __name__ == '__main__':
    with open("2.txt", "r",encoding='utf-8') as myfile:
        text = myfile.read().replace('\n','')
    res = summarize(text, 5)
    for i in range(len(res)):
        print(res[i])
# fin = open('news.txt') #the txt is up
# #to you
# lines=fin.readlines()
# fin.close()
# '''transform the article into word list
# '''
# def words_list():
#   chardigit='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 '
#   all_lines = ''
#   for line in lines:
#     one_line=''
#     for ch in line:
#       if ch in chardigit:
#         one_line = one_line + ch
#     all_lines = all_lines + one_line
#   return all_lines.split()
# '''calculate the total number of article list
# s is the article list
# '''
# def total_num(s):
#   return len(s)
# '''calculate the occurrence times of every word
# t is the article list
# '''
# def word_dic(t):
#   fre_dic = dict()
#   for i in range(len(t)):
#     fre_dic[t[i]] = fre_dic.get(t[i],0) + 1
#   return fre_dic
# '''calculate the occurrence times of every word
# w is dictionary of the occurrence times of every word
# '''
# def word_fre(w):
#   for key in w:
#     w[key] = w[key] / total
#   return w
# '''sort the dictionary
# v is the frequency of words
# '''
# def word_sort(v):
#   sort_dic = sorted(v.items(), key = lambda e:e[1])
#   return sort_dic
# '''This is entrance of functions
# output is the ten words with the largest frequency
# '''
# total = total_num(words_list())
# print(word_sort(word_fre(word_dic(words_list())))[-10:])
