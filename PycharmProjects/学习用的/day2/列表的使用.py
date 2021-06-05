#Author：Alex.Zhang
names=['haha','adjf','adjaf','zhangying','zhangying',['alex','jack']]
print(len(names))
names[5][1]=50
import copy


print(names.index('haha'))#查找你想要查询的字符在列表中的位置
print(names[names.index('haha')])#多重变换
print(names.count('zhangying'))#查出在列表中有多少重复的内容
#names.sort()#给字符排序
print(names)
names.append('zhanghaonan')#可以添加列表中的内容
names.insert(1,'zybb')#插入相应的位置
names[1]='xiaokeai'#直接增添到相应的位置
del names[1]#删除
names.remove('haha')#删除
names.pop()#默认删除最后的一个
names.reverse()#倒序
print (names[0:3])#切片
print (names[-1])#最后一个
print (names[-3:-1])
print (names[-2:])
print (names[:3])
names.clear()#清空列表
name2=[1,2,3]
names.extend(name2)#names与name2组合在一起了
name3=names.copy()
names[2]='zydbb'
print(names)
print(name3)
for i in names:
    print(i)
print(names[0:-1])
