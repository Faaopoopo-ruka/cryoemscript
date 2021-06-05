__author__ = "Alex Li"

import time
import queue
from greenlet import greenlet


def consumer(name):
    print("--->starting eating baozi...")
    gr2.switch('asdasdasd')
    while True:
        for i in range(5):
            new_baozi = i
            print("[%s] is eating baozi %s" % (name, new_baozi))
            # time.sleep(1)


def producer(name):
    time.sleep(1)
    print("\033[32;1m[producer]\033[0m is making baozi %s" )


if __name__ == '__main__':
    gr1 = greenlet(consumer) # 启动一个携程
    gr2 = greenlet(producer)
    gr1.switch('asdasdas')