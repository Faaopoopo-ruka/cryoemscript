import requests
import re

url = 'http://www.renren.com/PLogin.do'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

post_data = {
    "email": "15626046299",
    "password": "044610Fa"
}

# 创建session对象
session = requests.Session()

# 发送登录请求
session.post(url, data=post_data, headers=headers)

# 验证登录
response = session.get('http://www.renren.com/965882188')

print(re.findall('新用户', response.text))
print(response.url)
