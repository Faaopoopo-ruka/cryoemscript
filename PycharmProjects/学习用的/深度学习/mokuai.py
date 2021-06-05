#Author：Alex.Zhang
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
import jieba
# dict=DictVectorizer()
# aa=dict.fit_transform({'铜网':"GIG",'温度':100})
# print(dict.get_feature_names())
# print(aa)
vector=TfidfVectorizer()
a='博客园是一个面向开发者的知识分享社区。自创建以来,博客园一直致力并专注于为开发者打造一个纯净的技术交流社区,推动并帮助开发者通过互联网分享知识,从而让更多'
b='所有文章首发于我的个人博客和博客园。'
c1=jieba.cut(a)
l1=list(c1)
s1=' '.join(l1)
print(s1)
res=vector.fit_transform([s1])
print(vector.get_feature_names())
# print(res.toarray())