import speech_recognition as sr
# import urllib.request,random
# proxy_iplist=['122.114.31.177:808','61.135.217.7:80']
# proxy_ip=random.choice(proxy_iplist)
#
# handler=urllib.request.ProxyHandler({'http':proxy_ip})
# opener=urllib.request.build_opener(handler)
# import urllib.request,requests
# import random
# iplist = ['115.32.41.100:80','58.30.231.36:80','123.56.90.175:3128']
# proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
# opener = urllib.request.build_opener(proxy_support)
# opener.addheaders = [('User-Agent','Test_Proxy_Python3.5_maminyao')]
# urllib.request.install_opener(opener)
# print(requests.get(' http://www.google.com'))
print(sr.__version__)
r = sr.Recognizer()
test = sr.AudioFile('444.wav')
with test as source:
    audio = r.record(source)
print(type(audio))
c=r.recognize_google(audio,language="en-US", show_all=False)     #识别输出
print(c)
