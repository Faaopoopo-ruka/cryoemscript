#Author：Alex.Zhang
import requests,json,execjs
from pprint import pprint
class baidufanyi(object):
    def __init__(self,valuestr):
        self.langurl='https://fanyi.baidu.com/langdetect'
        self.valuestr=valuestr
        self.header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36', 'x-requested-with': 'XMLHttpRequest'}
        pass
    def parse(self,url,data):
        respone=requests.post(url,data=data,headers=self.header)
        return json.loads(respone.content.decode())
    def generate_url(self):
        langpostdata = {'query': self.valuestr}
        lang = self.parse( self.langurl , langpostdata )['lan']
        if lang=='en':
            anotherlang='zh'
        else:
            anotherlang='en'
        fanyiurl = 'https://fanyi.baidu.com/v2transapi?from=%s&to=%s' % (lang , anotherlang)
        return fanyiurl,lang
    def generate_data(self):
        url , lang = self.generate_url()
        query = 'Hello spider'
        with open( 'baidutrans.js' , 'r' , encoding='utf-8' ) as f:
            ctx = execjs.compile( f.read() )
        sign = ctx.call( 'e' , query )
        if lang =='zh':
            data={'from': 'zh', 'to': 'en', 'query': self.valuestr, 'simple_means_flag': '3', 'sign': sign, 'token': 'a56484c79d17e730df1640a89c1a326e'}
        else:
            data = {'from': 'en' , 'to': 'zh' , 'query': self.valuestr , 'simple_means_flag': '3' , 'sign': sign ,
                    'token': 'a56484c79d17e730df1640a89c1a326e'}
        return data
    def run(self):
        url,lang=self.generate_url()
        data=self.generate_data()
        result=self.parse(url,data=data)
        final_result=result['trans_result']['data'][0]['dst']
        print('翻译结果：',final_result)
if __name__=='__main__':
    baidufanyi=baidufanyi('''Cryo-electron microscopy combined with single-particle reconstruction is a promising technique for solving 
    the high-resolution structure ofmacromolecular 
    complexes, even in the presence of conformational or compositional heterogeneity. However, 
    the usual workflow leading to one or several structures is mired in subjective decisions that must 
    be made by an expert. One problem, in particular, has been the difficulty finding algorithms capable of automatically 
    selecting and verify- ing individual views of a macromolecular complex from the electron micrograph, due to the extremely 
    low signal-to-noise ratio and the presence of contaminants. We present a novel machine-learning algorithm that overcomes these problems. 
    The performance of the algorithm is demonstrated with electron micrographs of ribosomes.
R.''')
    baidufanyi.run()

