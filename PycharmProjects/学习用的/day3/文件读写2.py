
#Author：Alex.Zhan
'''''
f=open('linux','r',encoding='utf-8')
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(10)#从第十个字符一直书写到行末
print(f.readline())
print(f.encoding)
print(f.fileno())
print(f.flush())#立即刷新，从缓存中刷到硬盘
print(f.buffer)
'''
f=open('linux','a',encoding='utf-8')
f.truncate(100)#截断文件中的内容，只剩十个字符
