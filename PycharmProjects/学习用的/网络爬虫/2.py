import requests
import re
from urllib.parse import urlencode
from config import *
from requests.exceptions import RequestException
import json
from bs4 import  BeautifulSoup

def get_page_index(offset,keyword):
    header = {"authority": "www.toutiao.com" ,
              "method": "GET" ,
              "path": "/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1564750469768" ,
              "scheme": "https" ,
              "accept": "application/json, text/javascript" ,
              "accept-encoding": "gzip, deflate, br" ,
              "accept-language": "zh-CN,zh;q=0.9" ,
              "content-type": "application/x-www-form-urlencoded" ,
              "cookie": "tt_webid=6720441539534898695; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6720441539534898695; csrftoken=3579668984ecdae134d23101080d765c; UM_distinctid=16c512e8462759-0a1bacc6a502df-a7f1a3e-144000-16c512e84633c6; s_v_web_id=be57d7f0051b896db12feed7a95f86df; __tasessionId=hoo4ed6dc1564748820066; CNZZDATA1259612802=353990514-1564725921-https%253A%252F%252Fwww.toutiao.com%252F%7C1564749136" ,
              "referer": "https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D" ,
              "sec-fetch-mode": "cors" ,
              "sec-fetch-site": "same-origin" ,
              "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36" ,
              "x-requested-with": "XMLHttpRequest"}
    data={'aid': 24,
        'app_name':'web_search',
         'offset': offset,
        'format': 'json',
        'keyword': keyword,
         'autoload': 'true',
          'count': 20,
        'en_qc': 1,
        'cur_tab': 1,
         'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': 1564733227039}
    url='https://www.toutiao.com/api/search/content/?'+urlencode(data)
    try:
        response=requests.get(url,headers=header)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print('wangyeqingqiuchucuo')







def main():
    html=get_page_index(60,'街拍')
    print(html)






if __name__ == '__main__':
    main()
    print('done')