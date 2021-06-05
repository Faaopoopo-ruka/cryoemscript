#Author：Alex.Zhang
import os
import requests

# 新建文件夹
folder_name = 'data'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
data_urls=[]
print(data_urls)
# 对url循环遍历
for url in data_urls:
    res = requests.get(url)
    file_name = url.split('/')[-1]
    # 将网页内容写入到文件
    with open(os.path.join(folder_name, file_name), mode='wb') as file:
        file.write(res.content)
