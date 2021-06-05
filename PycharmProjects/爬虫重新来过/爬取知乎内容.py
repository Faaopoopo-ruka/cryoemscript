#Author：Alex.Zhang
import requests,re
from bs4 import BeautifulSoup
headers={
 'referer': 'https://cn.bing.com/',
 'upgrade-insecure-requests': '1',
 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
response=requests.get('https://www.zhihu.com/question/20852004',headers=headers)
content=response.text.encode('utf-8')
soup=BeautifulSoup(content,"lxml")
all_a = soup.find_all( 'p' )
all_a=str(all_a)
final=re.findall('<p>(.*?)</p>',all_a)
final=str(final)
last=re.sub('<img alt=.*?/>','',final)
aa=str(last)
la=re.sub('</b>','',aa)
sb=str(la)
hb=re.sub('<br/>','',sb)
print(''.join(hb))
# from pyquery import PyQuery as pq
# import requests
#
# headers = {'User-Agent': 'Mozilla'}
# url = "https://www.zhihu.com/explore"
# r = requests.get( url , headers=headers )
# html = r.text
# doc = pq( html )
# items = doc( '.explore-feed.feed-item' ).items()
# for item in items:
#     question = item.find( 'h2' ).text()
#     author = item.find( '.author-link-line' ).text()
#     anwser = pq( item.find( '.content' ).html() ).text()
#     file = open( 'explore3.txt' , 'a' , encoding='utf-8' )
#     file.write( '\n'.join( [question , author , anwser] ) )
#     file.write( '\n' + '=' * 50 + '\n' )
#     file.close()
