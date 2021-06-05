#Author：Alex.Zhang
import requests,json
class Douban:
    def __init__(self):
        self.header={'Accept': '*/*',
 'Accept-Encoding': 'gzip, deflate, br',
 'Accept-Language': 'zh-CN,zh;q=0.9',
 'Connection': 'keep-alive',
 'Cookie': 'bid=EyWgaiJuBrE; douban-fav-remind=1; ll="108295"; '
           '__utmc=30149280; __utmc=223695111; '
           '_vwo_uuid_v2=D992CB78B0D55D5C33198816A53B260F5|72dec092a8f5435e5fec29a2fa9f2313; '
           '_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1572262213%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DEFiTPnbj73_-CjfnTx5npdB5EEg5myIl8viwwFWGRBPV9Zlj7QO93ldIvXzkrvBX%26wd%3D%26eqid%3D82314ec70001b54f000000025db6d13f%22%5D; '
           '_pk_ses.100001.4cf6=*; '
           '__utma=30149280.799974825.1568108256.1572262188.1572262213.6; '
           '__utmb=30149280.0.10.1572262213; '
           '__utmz=30149280.1572262213.6.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; '
           '__utma=223695111.1194362506.1572238260.1572238260.1572262213.2; '
           '__utmb=223695111.0.10.1572262213; '
           '__utmz=223695111.1572262213.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; '
           'ap_v=0,6.0; '
           '_pk_id.100001.4cf6=75395e1e5df90813.1572238259.2.1572263743.1572239903.',
 'Host': 'movie.douban.com',
 'Referer': 'https://movie.douban.com/tv/',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
 'X-Requested-With': 'XMLHttpRequest'}
        self.starturl='https://movie.douban.com/j/search_subjects?type=tv&tag={}&sort=recommend&page_limit={}&page_start={}'
    def parse_url(self,url):
        response=requests.get(url,headers=self.header)
        result=response.content.decode()
        return result
    def get_content(self,content):
        json_str=json.loads(content)
        json_str1=json_str['subjects']
        return json_str1

    def save_content_list(self,json_str1):
        with open('豆瓣电视剧.json','a+',encoding='utf-8') as f:
            f.write( json.dumps( json_str1  , ensure_ascii=False , indent=2 ) )
    def run(self):
        l1=["热门","美剧","英剧","韩剧","日剧","国产剧","港剧","日本动画","综艺","纪录片"]
        for i in range(10):
            num=i*20
            url=self.starturl.format(l1[0],20,num)
            content=self.parse_url(url)
            finalresult=self.get_content(content)
            wewant=self.save_content_list(finalresult)
if __name__=='__main__':
    douban=Douban()
    douban.run()
