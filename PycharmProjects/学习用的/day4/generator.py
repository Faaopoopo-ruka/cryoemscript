#Author：Alex.Zhang
# a=[i*2 for i in range(10)]
#
# print(a[3])
# s=[]
# for i in range(100):
#     s.append(i*2)
# print(s)
#这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)  生成器的形成只需要把print变成yield
        yield ( b )
        a, b = b, a + b
        n = n + 1
    return 'done'#用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
f=fib(2)
# print(f)#<generator object fib at 0x000002416B110840>
print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
g = fib(6)

while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
#这是最终版本，最好不要再动啦