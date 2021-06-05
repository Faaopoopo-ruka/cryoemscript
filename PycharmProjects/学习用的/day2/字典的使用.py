
#Author：Alex.Zhang
info={'student1':'zhangyingbaobao','student2':'zhangyingxiaomao',
'student3':'zhangyingxiaokeai'}
print(info)
for i in info:
   print(i)
print(info['student1'])
info['student2']='xiaomao'
#info.pop('student1')  标准的随即删除
#print(info['student2'])
#print(info.popitem())#random delete

#print(info['student1'])
print(info.get('student2'))#安全的GET
print('student2' in info)# see
b={'student1':'zhangyingdabaobao',
   1:2,
   3:3}#如果有原有KEY值就会覆盖原值，如果没有就会创建新目录，非常好用
info.update(b)
c=dict.fromkeys(['g','h','f'],['none','stderr','stdin'])#分别赋值于字典中，很好用
c['g'][0]='stdout'#它们已经连在一起了


print(info)
print(c)
for i in info:
   print(i,info[i])#字典的循环，最好用
for k,v in info.items():
   print(k,v)


catalog={'one':{'1':['haha','heihei','fsdfd','ninin'],'436':['zhanmusi','james','lbj']},'two':{
'2':['niubi','frank','lip','mahone'],'3':'asd'}}
print(catalog)
print(catalog.values())
print(catalog.keys())
# print(catalog.pop('one'))
#
# catalog['two'][1]='woaizybb'
# print(catalog['two'])
# catalog.setdefault('56',{'www.baidu.com'})#创建一个新的字典子集，前面是key,中括号里是value
# print(catalog)
