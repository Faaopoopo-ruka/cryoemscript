#Author：Alex.Zhang
with open('length','r') as f:
    w=f.readlines()
    bylength=sorted(w,key=lambda x:len(x))
    out=''
    for i in bylength:
        i=[str(x) for x in i]
        out+=''.join(i)+'\n'
with open('out_file','w') as l:
    l.write(out)
#只能说太完美了