#Author：Alex.Zhang
import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield
       print("[%s]包子来了,被[%s]吃了!" %(baozi,name))
    return  done
g = consumer('张莹宝宝')

count=0
while count<5:
    try:
        x = next(g)
        print( x)
        count+=1
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

