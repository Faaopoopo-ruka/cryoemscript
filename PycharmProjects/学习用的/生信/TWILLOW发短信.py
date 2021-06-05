#Author：Alex.Zhang
from twilio.rest import Client
from bs4 import BeautifulSoup
import requests,schedule,time
# 下载数据
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
url = 'http://www.weather.com.cn/weather1d/101050507.shtml'
# 数据获取：
res = requests.get( url , headers=headers )
res.encoding = 'utf-8'
# 数据解析：
soup = BeautifulSoup( res.text , 'html.parser' )
# 数据提取：
tem1 = soup.find( class_='tem' )
weather1 = soup.find( class_='wea' )
tem = tem1.text
weather = weather1.text
content='兰西的天气是：\n'+tem+weather
print(content)
account_sid = 'AC8fdc9eda143343d0ee665d1961e8f495'
auth_token = '777ba66dfe918e608a0d8a4c9e7c9135'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=content,
                     from_='+12513334070',
                     to='+86 159 4557 7717'
                 )

print(message.sid)