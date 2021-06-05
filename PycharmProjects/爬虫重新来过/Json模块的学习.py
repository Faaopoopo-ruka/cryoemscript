#Author：Alex.Zhang
from pprint import pprint
import json,requests
url='https://movie.douban.com/j/search_subjects?type=movie&tag=热门&page_limit=50&page_start=0'
response=requests.get(url,timeout=10).text
pprint(json.loads(response))
with open('douban.json','w',encoding='utf-8') as f:
    f.write(json.dumps(json.loads(response),ensure_ascii=False,indent=2))#这个方法太秀了，其实STR方法也可以让这个字典变成字符串，但是功能没有这个强大
with open('douban.json','r',encoding='utf-8') as f:
    f=f.read()
    pprint(json.loads(f))