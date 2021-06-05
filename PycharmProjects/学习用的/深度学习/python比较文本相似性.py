#Author：Alex.Zhang
import difflib
import jieba
from sklearn.metrics import mean_squared_error
a='博客园是一个面向开发者的知识分享社区。自创建以来,博客园一直致力并专注于为开发者打造一个纯净的技术交流社区,推动并帮助开发者通过互联网分享知识,从而让更多'
b='博客园是一个面向开发者的知识分享社区。自创建以来,博客园一直致力并专注于为开发者打造一个纯净的技术交流社区,推动并帮助开发者通过互联网分享知识,从而让更多'
c1=jieba.cut(a)
l1=list(c1)
c2=jieba.cut(b)
l2=list(c2)
test=difflib.SequenceMatcher(a=l1, b=l2).quick_ratio()
print(test)
a=[1,2,3,4,6,8,9,7]
b=[1,2,3,4,6,8,9,7]
print(mean_squared_error(a,b))