__author__ = "Alex Li"

from urllib import request
import gevent,time
from gevent import monkey
monkey.patch_all() #把当前程序的所有的io操作给我单独的做上标记

def f(url,num):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()

    with open('file%s.txt'%num,'wb') as w:
        w.write(data)

    print('%d bytes received from %s.' % (len(data), url))

urls = ['https://www.python.org/',
        'https://www.yahoo.com/',
        'https://github.com/' ]
time_start = time.time()
#for url in urls:
#    f(url)
#print("同步cost",time.time() - time_start)
async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/',11),
    gevent.spawn(f, 'https://www.baidu.com/',12),
    gevent.spawn(f, 'https://wenku.baidu.com/view/9a5e50496f1aff00bed51edb.html',13),
])
print("异步cost",time.time() - async_time_start)