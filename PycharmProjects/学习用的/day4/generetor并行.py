import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield
       print("[%s]包子来了,被[%s]吃了!" %(baozi,name))
def producer():
    c = consumer('张莹宝宝')#这步就是告诉系统这是个生成器
    c2 = consumer('张浩楠爸爸')#这步就是告诉系统这是个生成器
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    a=['芝麻','西瓜','狐狸','小猫']
    for i in a:
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)
producer()
