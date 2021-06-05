#Author：Alex.Zhang
''''
这种方法虽然能同时读写，但是只能写道文章的最后面
f=open('linux1','r+',encoding='utf-8')#文件句柄（包括文件名，通过f这个变量去操作）
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.write('王力宏没我帅')
'''
'''''
#下面的 是写读，毫无用处
f=open('linux1','w+',encoding='utf-8')#文件句柄（包括文件名，通过f这个变量去操作）
print(f.write('adsasdfdsf--------------\n'))
print(f.write('adsasdfdsf--------------\n'))
print(f.write('adsasdfdsf--------------\n'))
print(f.write('adsasdfdsf--------------\n'))
f.write('王力宏没我帅')
'''
''''
二进制文件的读
f=open('linux1','rb')#以二进制的方式去读这个文件
print(f.readline())
'''
f=open('linux1','wb')#以二进制的方式去写这个文件
f.write('hello'.encode())
f.close()
b=''
with open('linux','r',encoding='utf-8') as f:
    for line in f:
        a=line.strip()
        b+=a
print(''.join(b.split()))



