#-*-coding:utf-8 -*-
#Author：Alex.Zhang  一行代码不应该超过80个字符
#with语句,自动打开关闭
'''''
with open('linux','r',encoding='utf-8') as f,\
        open('linux1','r',encoding='utf-8') as d:#这种写法更好一点
    for line in f:
        print(line)
    for line in d:
        print(line)
'''
''''''
s='你好'
s_utf8=s.encode()
s_gbk=s.encode('gbk')
gbk_UTF8=s_gbk.decode('gbk').encode('utf8').decode('utf-8')
print(s)
print(s_gbk)
print(s_utf8)
print(gbk_UTF8)


