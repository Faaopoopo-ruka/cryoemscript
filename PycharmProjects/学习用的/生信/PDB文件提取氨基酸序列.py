haha=''
with open('6666.ent','r',encoding='utf-8') as f:
    for line in f:
        if line[0:6]=='SEQRES':
            columns=line.split()
            print(columns)
            haha+=''.join(columns[4:])
            # haha.append(columns)
print(haha)






















