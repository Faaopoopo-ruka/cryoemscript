# #Author：Alex.Zhang
a=ascii(['a',2])
print(a)#这是个字符串
# b=bin(32)
# print(b)#把数字转成二进制
# def lal():     
#     pass
#
# print(callable(lal))
# c=bytearray('asdasd',encoding='utf-8')
# print(c[1])
# print(chr(100))#把数字的ascii的表转变,输入数字，转变字母,vice verse
#
# code='for i in range(10):print(i)'
# c=compile(code,'','exec')#compile编译字符，使字符可执行
# print(c)
# exec(c)#可执行
# t='1+2+6/8'
# print(eval(t))#eval可以直接执行字符
haha='''
import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield
       print("[%s]包子来了,被[%s]吃了!" %(baozi,name))
def producer():
    c = consumer('张莹宝宝')#这步就是告诉系统这是个生成器
    c2 = consumer('张浩楠爸爸')#这步就是告诉系统这是个生成器
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    a=['芝麻','西瓜','狐狸','小猫']
    for i in a:
        time.sleep(10)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)
producer()
'''
# qiji=compile(haha,'err.log','exec')#compile编译字符，使字符可执行
# print(exec(qiji))
# # print(eval(code))这个大字符不能用eval的方法去执行
# print(divmod(5,2))#相除并返回余数
# ac=lambda n:3 if n<4 else print(n)
# ac(4)
# res=filter(lambda n:n>5,range(10))# ac=lambda n:3 if n<4 else print(n)
# # ac(4)
# for i in res:
#     print(i)
# res=map(lambda n:n*n,range(17))
# print(res)
# for i in res:
#     print(i)
# import functools
# res=functools.reduce(lambda x,y:x*y,range(1,17))#reduce :累计所有值或者
# print(res)
# a=frozenset([1,54,45,45,454,54,])
# print(a)
# print(globals())
# print(hash('张莹')-hash('张浩楠'))
# print(hex(90))#z专程十六进制
# print(int(10.1))
# print(pow(4,5))
# asdas='afddf'
# print(repr(asdas))
# print(round(1.15))
# zidian={9:3,2:1,4:3,7:4}
# print(sorted(zidian.items(),key=lambda x:x[1]))
# a=[1,2,3,4]
# b=[5,6,7,8]
# zip(a,b)
# for i in zip(a,b):
#     print(i)
# # import generator
# __import__('generator')#iimport的另一种方式，只知道字符的时候
# print(exec(haha))
ac=lambda n:print(8)if n<4 else print(n)
ac(1)
a=[1,2,3,4]
b=[5,6,7,8]
zip(a,b)
for i,h in zip(a,b):
    print(i,h)
print(pow(4,5))
a=[1,2,3,4]
