# with open('map03.mrc.mdoc','r+',encoding='utf-8') as f:
#     for i,line in enumerate(f):
#         if 'Binning = 1' in line:
#             line = line + " \nSubFramePath = H:\map03\map03\map03_0.mrc "
#
#             print('yes',i)
newlist=[]
f = open("map06.mrc.mdoc")               # 返回一个文件对象
line = f.readlines()               # 调用文件的 readline()方法
a=0
for i,k in enumerate(line):
    if 'Binning = 1' in k:
       line = k + "SubFramePath = E:\map03\map06_%d.mrc\n"%(a)
       newlist.append(line)
       a=a+1
    else:
        newlist.append(k)
f = open("newmap06.mrc.mdoc",'a')               # 返回一个文件对象
for j in newlist:
    f.write(j)