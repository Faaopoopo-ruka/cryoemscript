#Author：Alex.Zhang
import json
a='haha.json'
with open('haha.json','r') as f:
    auth=json.load(f)
    print(auth)
