#Author：Alex.Zhan
f=open('linux','r',encoding='utf-8')
f_new=open('durant','w',encoding='utf-8')
for line in f:
    if 'LA Clippers	3' in line:
        line=line.replace('LA Clippers	3','LBJdexiaodi')
    f_new.write(line)
    #写入的一种新的方式，可以不用ELSE，不管循环正不正确，都会写入
f.close()
f_new.close()
with open('linux','r',encoding='utf-8') as f:
    for line in f:
        print(line)