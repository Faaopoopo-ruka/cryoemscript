#Author：Alex.Zhang
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import schedule
import time

# 输入邮箱发件人、收件人以及邮箱的授权码
account = str( input( '请输入发件人邮箱地址：' ) )
password = str( input( '请输入邮箱授权码：' ) )
receiver = str( input( '请输入收件人邮箱地址：' ) )


# 建立天气网爬虫，爬取天气信息
def weather_spider():
    # 模拟浏览器：
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
    return tem , weather
# 发送邮件的代码
def send_email(tem , weather):
    global account , password , receiver
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect( mailhost , 25 )
    qqmail.login( account , password )
    content = '上海的天气是：\n' + tem + weather
    message = MIMEText( content , 'plain' , 'utf-8' )
    subject = '今日天气预报from python'
    message['Subject'] = Header( subject , 'utf-8' )
    try:
        qqmail.sendmail( account , receiver , message.as_string() )
        print( '邮件发送成功' )
    except:
        print( '邮件发送失败' )
    qqmail.quit()


# 建立任务
def job():
    print( '开始一次任务' )
    tem , weather = weather_spider()
    send_email( tem , weather )
    print( '任务完成' )


# 定时发送
schedule.every().day.at( "07:00" ).do( job )
while True:
    schedule.run_pending()
    time.sleep( 1 )
