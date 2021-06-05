#Author：Alex.Zhang
out=''
with open('111','r',encoding='utf-8') as f:
    for line in f:
        a=''.join(line.split() )
        out+=a
with open('222.txt','w',encoding='utf-8') as p:
    p.write(out)
