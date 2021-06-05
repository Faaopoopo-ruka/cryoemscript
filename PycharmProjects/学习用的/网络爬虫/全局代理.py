#Author：Alex.Zhang
import urllib.request,random,requests
# proxy_iplist=['153.19.50.62:80']
# proxy_ip=random.choice(proxy_iplist)
# url=('http://www.baidu.com/')
# handler=urllib.request.ProxyHandler({'http':proxy_ip})
# opener=urllib.request.build_opener(handler)
#     #安装opener设置全局代理，只要加载网页都会使用该代理
# urllib.request.install_opener(opener)
# proxies={'http':'47.89.49.187:80'}
print(requests.get('http://www.google.com/').text)