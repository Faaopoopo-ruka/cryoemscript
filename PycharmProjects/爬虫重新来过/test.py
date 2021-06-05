# import requests,re
# from bs4 import BeautifulSoup
# header={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#  'Accept-Encoding': 'gzip, deflate',
#  'Accept-Language': 'zh-CN,zh;q=0.9',
#  'Cache-Control': 'max-age=0',
#  'Connection': 'keep-alive',
#  'Cookie': 'Hm_lvt_7c9f93d0379a9a7eb9fb60319911385f=1572402183; '
#            'Hm_lpvt_7c9f93d0379a9a7eb9fb60319911385f=1572402183; '
#            '_ga=GA1.2.1915950024.1572402183; _gid=GA1.2.1426308343.1572402183',
#  'Host': 'www.budejie.com',
#  'If-Modified-Since': 'Tue, 29 Oct 2019 14:06:59 GMT',
#  'Referer': 'http://www.so.com/link?m=aBHdre9PnZR%2FSwfj94mhaXKACLQV2qVVMGOmtfDtXgZWcvtdm4TXMwtoLzxCkWSOxgng511YNNk3jbCaVuV%2BXJM3H2HobW5BwP21NJjwJZKZ09Jxh%2FLHu8Qyqg7s%3D',
#  'Upgrade-Insecure-Requests': '1',
#  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
#                '(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# response=requests.get('http://www.budejie.com/')
# content=response.content.decode()
#
# soup=BeautifulSoup(content,"lxml")
# all_a = soup.find_all( 'div' , class_='j-r-list-tool' )
# all_a=str(all_a)
# # print(type(all_a))
#
# # for i in all_a:
#
# final=re.findall('data-title=".*?"',all_a)
#
# print(final)
# # for i in all_a:
# #     print(i.get_text())
#
#
import re
aa='''1最大似然估计框架能够很好地解决冷冻电镜三维颗粒的重构冋题,但目前的冷冻电镜单颗粒重构还存在着两个问题.第一个是不管是模版匹配法还是期望最大化最大似然估计算法,如果没有一个很好地初始化模型,整个算法的收敛性将会非常糟糕③37,经常无法收敛,或者收敛到完全错误的结构上去.第二个问题就是,目前的单颗粒重构算法都非常的慢,这也限制输入的颗粒投影数量,冷冻电镜单颗粒软件 RELION17]的主页上报告了在200个CPU上运行程序处理100.000张的投影图像需要耗费2个星期的时间.由于目前自动化收集大量数据的能力越来越好,这个问题将变得越来越糟糕和普遍.输入的数据量越多,通常意味着有可能获得更高分辨率的结构.
多伦多大学的 Marcus brubaker研究组提出了一个新的冷冻电镜结构重构框架(48,将统计模型下的最大后验概率估计(MAP)问题转化为随机优化( stochastic optimiza-
tion)问题.新框架非常高效,能够在短短十几个小时内得到一个较高分辨率的结构,并且只需要一台桌面级别的CPU工作站即可完成重构任务.该算法利用随机梯度下降和重要性釆样,能够解决对初始结构的依赖性问题和加速重构的计算过程.下文对该方法进行简单的介绍.
'''
final=re.sub('[0-9]','',aa)
print(final)