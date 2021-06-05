#Author：Alex.Zhang

import json
import os
from urllib.parse import urlencode
import pymongo
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
import re
from multiprocessing import Pool
from hashlib import md5
from json.decoder import JSONDecodeError
from config import *

client = pymongo.MongoClient( MONGO_URL , connect=False )
db = client[MONGO_DB]


def get_page_index(offset , keyword):
    header = {"authority": "www.toutiao.com" ,
              "method": "GET" ,
              "path": "/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1564817679060" ,
              "scheme": "https" ,
              "accept": "application/json, text/javascript" ,
              "accept-encoding": "gzip, deflate, br" ,
              "accept-language": "zh-CN,zh;q=0.9" ,
              "content-type": "application/x-www-form-urlencoded" ,
              "cookie": "tt_webid=6720441539534898695; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6720441539534898695; csrftoken=3579668984ecdae134d23101080d765c; UM_distinctid=16c512e8462759-0a1bacc6a502df-a7f1a3e-144000-16c512e84633c6; s_v_web_id=be57d7f0051b896db12feed7a95f86df; __tasessionId=73w6tp6q51564816765396; CNZZDATA1259612802=353990514-1564725921-https%253A%252F%252Fwww.toutiao.com%252F%7C1564813937" ,
              "referer": "https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D" ,
              "sec-fetch-mode": "cors" ,
              "sec-fetch-site": "same-origin" ,
              "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36" ,
              "x-requested-with": "pass"}
    data = {
        'autoload': 'true' ,
        'count': 20 ,
        'cur_tab': 3 ,
        'format': 'json' ,
        'keyword': keyword ,
        'offset': offset ,
    }
    params = urlencode( data )
    base = 'http://www.toutiao.com/search_content/'
    url = base + '?' + params
    try:
        response = requests.get( url )
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print( 'Error occurred' )
        return None


def download_image(url):
    print( 'Downloading' , url )
    try:
        response = requests.get( url )
        if response.status_code == 200:
            save_image( response.content )
        return None
    except ConnectionError:
        return None


def save_image(content):
    file_path = '{0}/{1}.{2}'.format( os.getcwd() , md5( content ).hexdigest() , 'jpg' )
    print( file_path )
    if not os.path.exists( file_path ):
        with open( file_path , 'wb' ) as f:
            f.write( content )
            f.close()


def parse_page_index(text):
    try:
        data = json.loads( text )
        if data and 'data' in data.keys():
            for item in data.get( 'data' ):
                yield item.get( 'article_url' )
    except JSONDecodeError:
        pass


def get_page_detail(url):
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}
    try:
        response = requests.get( url )
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        print( 'Error occurred' )
        return None


def parse_page_detail(html , url):
    soup = BeautifulSoup( html , 'lxml' )
    result = soup.select( 'title' )
    title = result[0].get_text() if result else ''
    images_pattern = re.compile( 'gallery: JSON.parse\("(.*)"\)' , re.S )
    result = re.search( images_pattern , html )
    if result:
        data = json.loads( result.group( 1 ).replace( '\\' , '' ) )
        if data and 'sub_images' in data.keys():
            sub_images = data.get( 'sub_images' )
            images = [item.get( 'url' ) for item in sub_images]
            for image in images: download_image( image )
            return {
                'title': title ,
                'url': url ,
                'images': images
            }


def save_to_mongo(result):
    if db[MONGO_TABLE].insert( result ):
        print( 'Successfully Saved to Mongo' , result )
        return True
    return False


def main(offset):
    text = get_page_index( offset , KEYWORD )
    urls = parse_page_index(text )
    for url in urls:
        html = get_page_detail( url )
        result = parse_page_detail( html , url )
        if result: save_to_mongo( result )


if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range( GROUP_START , GROUP_END + 1 )])
    pool.map( main , groups )
    pool.close()
    pool.join()