from pprint import pprint
form='''authority: blog.csdn.net
method: GET
path: /weixin_33692284/article/details/88050430
scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: max-age=0
cookie: uuid_tt_dd=10_36732819410-1563862385611-602054; dc_session_id=10_1563862385611.587941; smidV2=2019082909481066a988eccf0dc6979716e360e24e23d60074194a2e24dad80; __yadk_uid=yTB8cotbaVTL2rABsm0ZJlToxpUIAYmi; UN=qq_39460968; BT=1569584412980; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_36732819410-1563862385611-602054!1788*1*PC_VC!5744*1*qq_39460968; UM_distinctid=16df88d2fc689-06fcb0c06ec224-36664c08-1fa400-16df88d2fcc12f; Hm_lvt_62052699443da77047734994abbaed1b=1573392131; Hm_ct_62052699443da77047734994abbaed1b=5744*1*qq_39460968!6525*1*10_36732819410-1563862385611-602054; Hm_lvt_8b908b954c54e2c3a2291d77131dee94=1573392447; Hm_ct_8b908b954c54e2c3a2291d77131dee94=5744*1*qq_39460968!6525*1*10_36732819410-1563862385611-602054; Hm_ct_e5ef47b9f471504959267fd614d579cd=5744*1*qq_39460968!6525*1*10_36732819410-1563862385611-602054; Hm_lvt_e5ef47b9f471504959267fd614d579cd=1573433508,1574697682; __gads=ID=eb9b2b4767c41947:T=1575957151:S=ALNI_MYIZDyntPmUqmYl4paTEXAqDYcp5g; acw_tc=2760820615782757411043647e6c37730ed3e1aff60453cf5cb0898a52293f; TY_SESSION_ID=dde3e395-e009-47c3-9bb1-1f231ed0d53c; announcement=%257B%2522isLogin%2522%253Afalse%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Fblog.csdn.net%252Fblogdevteam%252Farticle%252Fdetails%252F103603408%2522%252C%2522announcementCount%2522%253A0%252C%2522announcementExpire%2522%253A3600000%257D; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1579762814,1579762858,1579762880,1579763629; dc_tos=q4jtic; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1579763750; c-login-auto=22
referer: https://blog.csdn.net/hfutzhouyonghang/article/details/81009760
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'''
headers = dict([line.split(": ",1) for line in form.split("\n")])
pprint(headers)