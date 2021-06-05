#Author：Alex.Zhang
table=[['protein','ext1','ext2','ext3'],[0.16,0.038,0.044,0.040],
       [0.33,0.089,0.095,0.091],[0.66,0.184,0.191,0.191],
       [1.00,0.280,0.292,0.283],[1.32,0.365,0.367,0.365],
       [1.66,0.441,0.443,0.444]]
table=table[1:]
protein,ext1,ext2,ext3=zip(*table)
extinction=ext1+ext2+ext3
protein=protein*3
table=zip(protein,extinction)
import json
# k=''
# with open('test','w') as p:
#     for prot,ext in table:
#         h=prot,ext
#         a=json.dumps(h)
#         k+=a+'\n'
#     p.write(k)
k=''
with open('test','w') as p:
    for prot,ext in table:




#
#
#
# second_row=table[1]
# print(second_row)
# data=[(1,2,3),(4,5,6)]
# print(zip(*data))