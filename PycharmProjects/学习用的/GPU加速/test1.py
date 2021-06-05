import csv

headers = ['country' , 'area']

datas = [
    {'country': '俄罗斯' , 'area': 1707} ,
    {'country': '加拿大' , 'area': 997} ,
    {'country': '中国' , 'area': 960} ,
    {'country': '美国' , 'area': 936}
]

filename = 'hehe.csv'
with open( filename , 'w' , newline='' ,encoding='utf-8') as f:
    writer = csv.DictWriter( f , headers )
    writer.writeheader()

    for row in datas:
        writer.writerow( row )
        print(row)
