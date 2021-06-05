#Author：Alex.Zhang
import pickle#pickle序列化的过程中，写入序列需要用wb二进制的格式，否则写入不进去，当然反序列化时也要用二进制的这种方法去读取,出现乱码不要慌，因为这是二进制文件
def func(*args):
    print(*args,'-----------------')
info = {'name': 'haha'
    , 'age': 23
    , 'funk': func}
with open('json','wb') as c:
    # c.write(pickle.dumps(info))#这是序列化的方式之一
    pickle.dump(info,c)#这句话的意思和上面的意思是一样的
    info['age']=45
    pickle.dump(info,c)
    #这个文件只告诉我们一个道理，只dump一次和只load一次
    try:
        pickle.loads(c)
    except Exception as a:
        print('a')