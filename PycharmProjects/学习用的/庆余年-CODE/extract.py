#Author：Alex.Zhang
import re,pickle,pprint
f=open('comments_1578730806.pkl','rb')

kk=pickle.load(f)
pprint.pprint(kk)
# pprint.pprint(kk)
# for i,k,in enumerate(range(10)):
#     l=kk[1]['data']['data'][0]['comments'][k]['text']
#     print(i,l)
# with open('123.txt','w',encoding='utf8') as f:
#     f.write(str(l))