#Author：Alex.Zhang
import csv
with open('hehe.csv','r',encoding='utf-8') as f:
    reader=csv.reader(f)
    fieldnames=next(reader)
    csvreader=csv.DictReader(f,fieldnames=fieldnames)
    for row in csvreader:
        d={}
        for k,v in row.items():
            d[k]=v
        print (d)