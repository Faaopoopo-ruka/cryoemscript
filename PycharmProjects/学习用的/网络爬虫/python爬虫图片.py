import requests,os
from bs4 import BeautifulSoup
# # circle = requests.get('http://travel.quanjing.com/tag/12975/%E9%A9%AC%E5%B0%94%E4%BB%A3%E5%A4%AB')
# #
# # # 将获取的图片地址依次放入count中
# count = ['https://webimg.quanjing.com/creative/1.jpg']
# # # 将获取的网页内容放入BeautifulSoup
# # soup = BeautifulSoup(circle.text, 'lxml')
# # # 根据谷歌SelectGadGet这个插件，获取html标签，比如获取：#gallery-list
# # for item in soup.select('#gallery-list'):
# #     # 用bs4中的find_all获取 #gallery-list 中是否存在 img这个标签
# #     for img in item.find_all('img'):
# #         print('img', img)
# #         # m 是 img标签中存在的属性
# #         img_path = img.get('m')
# #         count.append(img_path)
# # 用enumerate依次取出count中的图片地址 放入v中
#
# for i,v in enumerate(count):
#     print(v)
#     # 将获取的v值再次放入request中进行与网站相应
#     image = requests.get(v)
#     # 存取图片过程中，出现不能存储 int 类型，故而，我们对他进行类型转换 str()。w:读写方式打开，b：二进制进行读写。图片一般用到的都是二进制。
#     folder_name = 'newpic'
#     if not os.path.exists( folder_name ):
#         os.makedirs( folder_name )
#         new_path=os.path.join(os.getcwd(),folder_name)
#         with open(new_path+'\\'+str(i)+'.jpg', 'wb') as file:
#             print(image.content)
#         # content：图片转换成二进制，进行保存。
#
#             file.write(image.content)
#             print('ok')
#     print(i)
import requests  # Python上网必备
import os  # 用来创建文件夹保存皮肤图片
import time  # 导入时间库，用来计算程序用时

# 所有英雄对应的编号
herolist = {"266": "Aatrox" , "103": "Ahri" , "84": "Akali" , "12": "Alistar" , "32": "Amumu" , "34": "Anivia" ,
            "1": "Annie" , "22": "Ashe" , "136": "AurelionSol" , "268": "Azir" , "432": "Bard" , "53": "Blitzcrank" ,
            "63": "Brand" , "201": "Braum" , "51": "Caitlyn" , "164": "Camille" , "69": "Cassiopeia" , "31": "Chogath" ,
            "42": "Corki" , "122": "Darius" , "131": "Diana" , "119": "Draven" , "36": "DrMundo" , "245": "Ekko" ,
            "60": "Elise" , "28": "Evelynn" , "81": "Ezreal" , "9": "Fiddlesticks" , "114": "Fiora" , "105": "Fizz" ,
            "3": "Galio" , "41": "Gangplank" , "86": "Garen" , "150": "Gnar" , "79": "Gragas" , "104": "Graves" ,
            "120": "Hecarim" , "74": "Heimerdinger" , "420": "Illaoi" , "39": "Irelia" , "427": "Ivern" ,
            "40": "Janna" , "59": "JarvanIV" , "24": "Jax" , "126": "Jayce" , "202": "Jhin" , "222": "Jinx" ,
            "145": "Kaisa" , "429": "Kalista" , "43": "Karma" , "30": "Karthus" , "38": "Kassadin" , "55": "Katarina" ,
            "10": "Kayle" , "141": "Kayn" , "85": "Kennen" , "121": "Khazix" , "203": "Kindred" , "240": "Kled" ,
            "96": "KogMaw" , "7": "Leblanc" , "64": "LeeSin" , "89": "Leona" , "127": "Lissandra" , "236": "Lucian" ,
            "117": "Lulu" , "99": "Lux" , "54": "Malphite" , "90": "Malzahar" , "57": "Maokai" , "11": "MasterYi" ,
            "21": "MissFortune" , "62": "MonkeyKing" , "82": "Mordekaiser" , "25": "Morgana" , "267": "Nami" ,
            "75": "Nasus" , "111": "Nautilus" , "76": "Nidalee" , "56": "Nocturne" , "20": "Nunu" , "2": "Olaf" ,
            "61": "Orianna" , "516": "Ornn" , "80": "Pantheon" , "78": "Poppy" , "555": "Pyke" , "133": "Quinn" ,
            "497": "Rakan" , "33": "Rammus" , "421": "RekSai" , "58": "Renekton" , "107": "Rengar" , "92": "Riven" ,
            "68": "Rumble" , "13": "Ryze" , "113": "Sejuani" , "35": "Shaco" , "98": "Shen" , "102": "Shyvana" ,
            "27": "Singed" , "14": "Sion" , "15": "Sivir" , "72": "Skarner" , "37": "Sona" , "16": "Soraka" ,
            "50": "Swain" , "134": "Syndra" , "223": "TahmKench" , "163": "Taliyah" , "91": "Talon" , "44": "Taric" ,
            "17": "Teemo" , "412": "Thresh" , "18": "Tristana" , "48": "Trundle" , "23": "Tryndamere" ,
            "4": "TwistedFate" , "29": "Twitch" , "77": "Udyr" , "6": "Urgot" , "110": "Varus" , "67": "Vayne" ,
            "45": "Veigar" , "161": "Velkoz" , "254": "Vi" , "112": "Viktor" , "8": "Vladimir" , "106": "Volibear" ,
            "19": "Warwick" , "498": "Xayah" , "101": "Xerath" , "5": "XinZhao" , "157": "Yasuo" , "83": "Yorick" ,
            "154": "Zac" , "238": "Zed" , "115": "Ziggs" , "26": "Zilean" , "142": "Zoe" , "143": "Zyra"
            }
# 这个是每个皮肤url前面不变的部分
url_1 = "http://ossweb-img.qq.com/images/lol/web201310/skin/big"
# 考虑到皮肤数量最多的安妮也只有12个，因此可以把url上限调为011来减少访问无效的地址
num = ['000' , '001' , '002' , '003' , '004' , '005' , '006' , '007' , '008' , '009' , '010' , '011' , ]
# 把访问和下载英雄图片代码做成一个函数
def getImg():
    for key , value in herolist.items():  # 遍历每个英雄对应的数字编号和名字（英文名字）
        # 在f盘新建一个以英雄名字命名的文件夹，用来保存下载的英雄皮肤壁纸
        os.mkdir( r"C:\Users\ALEX PHYLIPS\Desktop\\new\\" + value )
        os.chdir( r"C:\Users\ALEX PHYLIPS\Desktop\\new\\" + value )  # 定位到新建的文件夹中
        url_2 = url_1 + key
        for n in num:  # 遍历该英雄的每个皮肤url
            url = url_2 + n + ".jpg"  # 生成完整的皮肤url
            img = requests.get( url )  # 获得Response对象
            # 如果img的状态码不等于200，表示刚刚生成的url不存在，也就是已有的皮肤图片下载完了，跳过该循环
            if img.status_code == 200:
                # 用 n 做文件名保存下载的图片，img.content用来返回二进制数据
                open( n + ".jpg" , 'wb' ).write( img.content )
        print( value + " 所有的皮肤壁纸获取成功···" )
start = time.time()
getImg()  # 运行爬虫程序
end = time.time()
spendtime = end - start
print( "运行成功！\n" )
print( "用时 " + str( spendtime ) + "秒" )
