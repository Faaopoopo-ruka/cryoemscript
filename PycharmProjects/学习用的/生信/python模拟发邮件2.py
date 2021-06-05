#Author：Alex.Zhang
import urllib
import urllib.request
from bs4 import BeautifulSoup
import requests,schedule,time
# 下载数据
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
url = 'http://www.weather.com.cn/weather1d/101020100.shtml'
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
#Author：Alex.Zhang
from gne import GeneralNewsExtractor
import requests,time
from selenium import webdriver
def parser(url):
    header={'authority': 'www.toutiao.com',
     'method': 'GET',
     'path': '/a6778613347827843597/',
     'scheme': 'https',
     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
     'accept-encoding': 'gzip, deflate, br',
     'accept-language': 'zh-CN,zh;q=0.9',
     'cache-control': 'max-age=0',
     'cookie': 'csrftoken=3506881fd2f41996fd36dafe4dc357f4; '
               'UM_distinctid=16c5168bbbe3a-0dc87a1396d551-36664c08-1fa400-16c5168bbbf521; '
               'CNZZDATA1259612802=1794567395-1564731331-https%253A%252F%252Fwww.toutiao.com%252F%7C1564731331; '
               'tt_webid=6757860260021667336; tt_webid=6757860260021667336; '
               's_v_web_id=1051c38bf2e8ab551da6ae7d39fedd02; '
               'WEATHER_CITY=%E5%8C%97%E4%BA%AC; '
               '__tasessionId=rmdomdwy51578293068494',
     'referer': 'https://www.toutiao.com/',
     'upgrade-insecure-requests': '1',
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

    html=response=requests.get(url,headers=header).content.decode()
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(3)
    extractor=GeneralNewsExtractor()
    result=extractor.extract(browser.page_source)
    print(result)
def chaolianjie():
    from urllib.request import urlopen  # 用于获取网页
    from bs4 import BeautifulSoup  # 用于解析网页

    header = {'authority': 'www.toutiao.com' ,
              'method': 'GET' ,
              'path': '/a6778613347827843597/' ,
              'scheme': 'https' ,
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,
              'accept-encoding': 'gzip, deflate, br' ,
              'accept-language': 'zh-CN,zh;q=0.9' ,
              'cache-control': 'max-age=0' ,
              'cookie': 'csrftoken=3506881fd2f41996fd36dafe4dc357f4; '
                        'UM_distinctid=16c5168bbbe3a-0dc87a1396d551-36664c08-1fa400-16c5168bbbf521; '
                        'CNZZDATA1259612802=1794567395-1564731331-https%253A%252F%252Fwww.toutiao.com%252F%7C1564731331; '
                        'tt_webid=6757860260021667336; tt_webid=6757860260021667336; '
                        's_v_web_id=1051c38bf2e8ab551da6ae7d39fedd02; '
                        'WEATHER_CITY=%E5%8C%97%E4%BA%AC; '
                        '__tasessionId=rmdomdwy51578293068494' ,
              'referer': 'https://www.toutiao.com/' ,
              'upgrade-insecure-requests': '1' ,
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    url = 'https://www.toutiao.com/'
    browser = webdriver.Chrome()
    browser.get( url )
    time.sleep( 3 )
    html =browser.page_source
    links = []
    soup = BeautifulSoup(html, "html.parser" )
    url_list = soup.find_all( 'a' )

    for link in url_list:
        links.append( link.get( 'href' ) )
    return links
aa=chaolianjie()

new = []
for i in aa:
    if i is not None and 'group' in i:
        new.append( i )
import re
sb=[]
for i in new:
    hb = re.sub( '/[A-Za-z]*' , '' , i)
    cb=re.sub('#[A-Za-z]*','',hb)
    sb.append(cb)
gb=[]
for i in range(len(sb)):
        if i%2==0:
            gb.append(sb[i])
import random
l=random.randint(0,len(gb))
houzhui=gb[l]
url='https://www.toutiao.com/a'+houzhui
print(url)
xinwen=parser(url)
content='上海的天气是：\n'+tem+weather+"\n"+str(xinwen)
# 发送邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def job():
    msg_from = "1501256676@qq.com"
    EMAIL_HOST_PASSWORD = 'kuybmighwcyxhcdc'
    msg_to = "mahonez1125@outlook.com"
    subject = "Python给小可爱爬取天气"
    other = str(xinwen)
    print( other )
    msg = MIMEText( other , 'plain' , 'utf-8' )
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to

    s = smtplib.SMTP_SSL( "smtp.qq.com" , 465 )
    s.set_debuglevel( 1 )
    s.login( msg_from , EMAIL_HOST_PASSWORD )
    s.sendmail( msg_from , msg_to , msg.as_string() )
    print( "发送成功" )
# schedule.every().day.at( "07:00" ).do( job )
# while True:
#     schedule.run_pending()
#     time.sleep( 1 )
job()

