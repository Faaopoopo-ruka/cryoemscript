#Author：Alex.Zhang
import zipfile
import os
os.chdir(r'C:\Users\ALEX PHYLIPS\PycharmProjects\学习用的')
# 压缩,只要把被压缩的文件路经输入对，可以选择性的压缩，真是他妈绝了
# z = zipfile.ZipFile('niubi.zip', 'w')
# z.write('day1')
# z.write('day2')
# z.close()
# 解压,extracall里面写入解压的路径，就可以解压啦
z = zipfile.ZipFile('niubi.zip', 'r')
z.extractall(r'C:\Users\ALEX PHYLIPS\Desktop')
z.close()

