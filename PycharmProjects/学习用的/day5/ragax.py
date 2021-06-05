#Author：Alex.Zhang
import re
res=re.match('.+','zhanghaonan123')
print(res.group())
# res=re.match('z.+','zhanghaonan123')
# print(res.group())
rap=re.search('y.+21','zhangyingbaobao521')
print(rap.group())
# fuck=re.findall('as','asasdas')
# print(fuck)#用findall就不能用group的方法啦
#
# print(re.findall( "ab*" , "cabb3abcbbac" ))
# print(re.search( "(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})" , "371481199306143242" ).groupdict( "city" ))
# print(re.sub('[?P]','|',"?Poj"))
print(re.search( "(abc){2}a(123|456)c" , "abcabca456c" ).group())
import re

key = r"<html><body><h1>hello world<h1></body></html>"#这段是你要匹配的文本
p1 = r"<h1>(.+?)<h1>"#这是我们写的正则表达式规则，你现在可以不理解啥意思
pattern1 = re.compile(p1)#我们在编译这段正则表达式
matcher1 = re.findall(pattern1,key)#在源文本中搜索符合正则表达式的部分
print (matcher1)#打印出来