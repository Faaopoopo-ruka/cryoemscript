__author__ = "Alex Li"

import gevent,time

def foo():
    print('Running in foo')
    gevent.sleep(2)
    print('Explicit context switch to foo again')
def bar():
    print('Explicit精确的 context内容 to bar')
    gevent.sleep(1)
    print('Implicit context switch back to bar')
def func3():
    print("running func3 ")
    gevent.sleep(0)
    print("running func3  again ")

start_time=time.time()

gevent.joinall([
    gevent.spawn(foo), #生成，
    gevent.spawn(bar),
    gevent.spawn(func3),
])
end_time=time.time()
print(end_time-start_time)