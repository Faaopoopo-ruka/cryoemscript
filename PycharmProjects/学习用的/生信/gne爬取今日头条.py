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
parser(url)
