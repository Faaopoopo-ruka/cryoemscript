#Author：Alex.Zhang
# import json  json只能处理简单的字符，像是字典，列表等简单的，但是对于像函数一样复杂的序列，应该用pickle
# info={'name':'haha'
#       ,'age':23}
# print(json.dumps(info))
# with open('ab.txt','w') as f:
#     f.write(json.dumps(info))
import pickle#pickle序列化的过程中，写入序列需要用wb二进制的格式，否则写入不进去，当然反序列化时也要用二进制的这种方法去读取,出现乱码不要慌，因为这是二进制文件
def func(*args):
    print(*args,'-----------------')
info = {'name': 'haha'
    , 'age': 23
    , 'funk': func}
with open('json','wb') as c:
    # c.write(pickle.dumps(info))#这是序列化的方式之一
    pickle.dump(info,c)#这句话的意思和上面的意思是一样的
import json  #json只能处理简单的字符，像是字典，列表等简单的，但是对于像函数一样复杂的序列，应该用pickle
info={'name':'haha'
      ,'age':23}
print(json.dumps(info))
with open('ab.txt','w') as f:
    f.write(json.dumps(info))