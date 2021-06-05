# Author：Alex.Zhang
import requests
import json

data={'LoginName': 'YHW30Zxi3ow7Mi+hP1FGSVciPxgSMoFLxCXjxHfgpNDMfBA6KFWXcWQynW9Yv0LrhQ+ziX+S9H3mw4NXX/dy7xvhcQ9kfoqX7HOIb62ZhVyuZpySxAZQlPJ2BTBPUQ32kDixHA8spc09THamXruKzFm4y7Zcld1OZrZiO+We68I=', 'geetest_challenge': '83d7622a098def23182674b66a225084', 'geetest_validate': 'f776a7521114ca2cc629aadad82e18e9', 'geetest_seccode': 'f776a7521114ca2cc629aadad82e18e9|jordan', 'Password': 'gHyVhqUXA6dwYpgDERdfxmzvY2+nikW8YbPU3pQbU9/3Vzy9u0Z02XTcn5IfsybF4o/2k9Iqp35OIXcWPFd2OSmexKWWC5w4kzZBgE/jqhcZE7IIwc4vmqu8gjL+2T5iqCxw7pNX3cnDT4+wclys2bo1oBYcTxVoj06y25igoy0=', '__RequestVerificationToken': 'CfDJ8DeHXSeUWr9KtnvAGu7_dX8hVxzxFwO8oiiJ6s6BDU_lECF6N4plWi0HQNQn2O4RnZx1XEyoyA-gluqOfx1RkSI9tVHoyh56lXw6YKcyMMRXEnq7Qo2EUUE58n7HPWctSZ-7hFFyOcgzPf_kQnJnKTM'}
#实例化session
session = requests.session()

url='https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F'
header={'authority': 'account.cnblogs.com', 'method': 'GET', 'path': '/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F', 'scheme': 'https', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'max-age=0', 'cookie': '_ga=GA1.2.718190844.1563785575; __gads=ID=a532a0c58a1a00a7:T=1563785576:S=ALNI_Ma4wM7Mv2utTzjT-AsGWiXYA0juJw; _gid=GA1.2.1241366812.1571992439; .Cnblogs.Account.Antiforgery=CfDJ8DeHXSeUWr9KtnvAGu7_dX_UHi2qHvNeu8xWZTFFT9DR4ohSiWLtaBdjhZ0Ks2z5prCF8EnGUBZKF3rz77K3FFNC67ppSfFBL8vh0dOQt1AtAmWuh_bPDRhTF71qZgnKSi4S7Lg-8gLoW6NN4CZJJYk; .Cnblogs.Account.Session=CfDJ8DeHXSeUWr9KtnvAGu7%2FdX9fe0Vby8i0CZQpqpk9BqjnubN6KK89CQcCv2ZhEWFdMqwKS4mmIR3U9gMjxMA6m%2Fs5Rn0X9HlKDZsrTIer035SeON3Ssn%2FVDdFbX5PxtwzRIph%2B6Sv6IVrFmE1odA7%2BgfH0%2FfdeMmAMHzlSIXuqw6q; SERVERID=d0724c395727ce8eb048bea7fa14fd42|1572165648|1572158524', 'referer': 'https://account.cnblogs.com/continuesignout?Url=https%3A%2F%2Faccount.cnblogs.com%2Fsignin%3FreturnUrl%3Dhttps%253A%252F%252Fwww.cnblogs.com%252F&Name=%25E7%2599%25BB%25E5%25BD%2595', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}



response = session.post(url,headers=header,data=data)
if response.status_code==200:
    url='https://www.cnblogs.com/klausage/'
    response = session.get( url,headers=header)
    print(response.text.encode('utf-8'))

