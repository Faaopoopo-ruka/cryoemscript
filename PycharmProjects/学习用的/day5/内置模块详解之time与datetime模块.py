#Author：Alex.Zhang
# python 中模块分为三类：
# 1.标准库
# 2.开源模块
# time 和datetimr
import time as de

# print(int(time.time()))#这叫时间戳
print(de.localtime())#这个可以打印当前时间

# print(-time.timezone/3600)
# print(time.gmtime())#这是国际时间
# print(time.localtime().tm_year)
# print(time.mktime(time.localtime()))
#
# x=time.localtime()
# print(time.strftime('%y-%m-%d %H-%m %S'),x)#规定格式
# print(time.asctime()))#格式：Tue Dec 18 21:56:12 2018
# print(time.ctime())#格式：Tue Dec 18 21:56:12 2018
# import datetime
# print(datetime.datetime.now())#现在的年月日，格式：2018-12-22 21:56:12.775894
# print(datetime.datetime.now()+datetime.timedelta(4))#添加或减去时间