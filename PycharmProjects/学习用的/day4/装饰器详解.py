#Author：Alex.Zhang
import time
def mom(func):
    def deco(*args,**kwargs):
        'this is a deco'
        start=time.time()
        func(*args,**kwargs)
        over=time.time()
        print('haha{a}'.format(a=start-over))
    return deco


@mom
def test1():
    time.sleep(3)
    print('this is fuction1')
@mom
def test2(name,age,hh):
    time.sleep(3)
    print('this is fuction2')
    print(name)
    print(age)
    print(hh)
print(mom(test1))

test1()

test2('sdas',34,5)
print(mom(test1))
# test1()
# test2()