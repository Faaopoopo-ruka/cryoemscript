#Author：Alex.Zhang
# import json
# with open('ab.txt','r') as x:
#
#     data=eval(x.read())
#     print(data['name'])
# import pickle
# with open( 'json', 'rb' ) as x:
#     data=pickle.loads(x.read())
#     print(data['name'])  我这里是有函数的，函数内存地址会随着序列化而消失，所以这个地方会报错
import pickle#函数可以序列化的一种方式，但是只能在python中用
def func(*args):
    print(*args,'-----------------')
    print(*args,'askdjasfhbjkdshfjkashdfjkabfvjdsbvchjdbfcvjkdbajskbfdjabcjabsj')#反序列化只要函数名一样就可以，内容不
    # 一样也没关系
with open( 'json', 'rb' ) as x:
    # data=pickle.loads(x.read())
    data=pickle.load(x)
    print(data)
















