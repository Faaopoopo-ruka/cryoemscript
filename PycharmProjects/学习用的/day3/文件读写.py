''''
#Author：Alex.Zhang
#data=open('linux',encoding='utf-8').read()#如果不用UTF-8，默认使用的是windows的gdk
#print(data)
#只能读或者只能写,a是可以在文件中添加内容的，否则源文件会被覆盖，r是读模式，但是在读模式下是不可以写入的，w是单纯的写模式，在
#写模式下，会重新写，把原文件覆盖或者是重新建一个新文件，从头写那种，下面的这个顺序不能变
#f=open('linux1','a',encoding='utf-8')#文件句柄（包括文件名，通过f这个变量去操作）
#f=open('linux1','r',encoding='utf-8')#文件句柄（包括文件名，通过f这个变量去操作）
f=open('linux1','w',encoding='utf-8')#文件句柄（包括文件名，通过f这个变量去操作）
f.write('\nAuthor：Alex.Zhangasdasd,\nwoaini')

f.close()
'''
'''
f=open('linux','r',encoding='utf-8')
for i in range(5):
    print( f.readline() )#打印前五行

'''
''''
f=open('linux','r',encoding='utf-8')
#print( f.readlines() )#readlins可以出列表
#for line in f.readlines():#可以打印出所有
 #   print(line.strip())
for index,line in enumerate (f.readlines()):
    if index==9:
        print('-------------------我是留缝--------------------')
        break
    print( line.strip() )

'''
#高效的循环方法
f=open('linux','r',encoding='utf-8')
count=0
for line in f:
    count+=1
    if count ==9:
        print('------------------------------------------------------woshilaidaoluande')
        continue
    print(line)








with












