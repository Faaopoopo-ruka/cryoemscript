#Author：Alex.Zhang
# table=[]
# for line in open('adf.txt',encoding='utf-8'):
#     table.append(line.strip().split('|'))
# # a,b,c,=zip(*table)
# # d=b+c
# # a=a*2
# # for i,j in zip(a,d):
# #     print(i,j)
# print(table)
out=''
import json
# for row in table:
#
#     line=[str(cell) for cell in row]
#     out+='|'.join(line)+'\n'
# with open('jijifujiji','w',encoding='utf-8') as d:
#     d.write(out)
# ji=[]
# with open('adf.txt','r',encoding='utf-8') as i:
#     for line in i:
#         n=line.strip().split('|')
#         ji.append(n)
#     print(ji)
from operator import itemgetter
table=[]
for line in open('adf.txt',encoding='utf-8'):
    columns=line.split('|')
    columns=[str(x) for x in columns]
    table.append(columns)
print(table)
column=2
table_sorted=sorted(table,key=itemgetter(column),reverse=True)#这两个等价
# table_sorted=sorted(table,key=lambda x:x[2],reverse=True)
print(table_sorted)
out=''
for row in table_sorted:
    row=[str(x) for x in row]
    out+='|'.join(row)+'\n'
    print(row)
print(out)
# hi=[]
# for i in range(4):
#     si=table[i][1]
#     hi.append(si)
# hi.sort()
# for row in hi:
#     row=[str(x) for x in row]
#     print('|'.join(row))