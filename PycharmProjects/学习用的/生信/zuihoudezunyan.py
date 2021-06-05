#Author：Alex.Zhang
import os
import requests
import json
import base64

#首先配置必要的信息
baidu_server = 'https://aip.baidubce.com/oauth/2.0/token?'
grant_type = 'client_credentials'
client_id = 'umuduD7RyyO7OIsAGWHyuZeG' #API KEY
client_secret = 'ay0ih0NhwAInGCgIdpmbvSG9nbl0KEw3' #Secret KEY

#合成请求token的url
url = baidu_server+'grant_type='+grant_type+'&client_id='+client_id+'&client_secret='+client_secret

#获取token
res = requests.get(url).text
data = json.loads(res)
token = data['access_token']

#设置音频的属性，采样率，格式等
VOICE_RATE = 16000
FILE_NAME = '666.wav'
USER_ID = 'Xu.zh' #这里的id随便填填就好啦，我填的自己昵称
FILE_TYPE = 'wav'

#读取文件二进制内容
f_obj = open(FILE_NAME, 'rb')
content = base64.b64encode(f_obj.read())
speech = str(content, 'utf8')
size = os.path.getsize(FILE_NAME)

#json封装
datas = json.dumps({
    'format': FILE_TYPE,
    'rate': VOICE_RATE,
    'channel': 1,
    'cuid': USER_ID,
    'token': token,
    'speech':speech,
    'len': size})

#设置headers和请求地址url
headers = {'Content-Type':'application/json'}
url = 'https://vop.baidu.com/server_api'

#用post方法传数据
request = requests.post(url, datas, headers)
result = json.loads(request.text)
text = result['result']
if result['err_no'] == 0:
    print(text)
else:
    print('返回错误！')
