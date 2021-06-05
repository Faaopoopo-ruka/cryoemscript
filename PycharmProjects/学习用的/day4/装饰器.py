#Author：Alex.Zhang
#装饰器的相关知识点我放在相应目录下的DOC文件中的图片里了，想看去那看吧
# 装饰器：
# 定义：本质是函数，装饰其他函数就是为其他函数添加附加功能
# 原则：1.不能修改被装饰的函数的源代码
#       2.不能修改装饰的函数的调用方式
# 实现装饰器知识储备：
# 1.函数即’变量‘
# 2.高阶函数：a.把一个函数名当作实参传给另一个函数（不改变被装饰函数的源代码）
#             b.返回值中包含函数名（不改变原函数的调用方式）
import time
def timmer(func):
    def wrapper(*args,**kwargs):
        start1=time.time()
        func()
        stop1=time.time()
        print('the time is running%s'%(stop1-start1))
    return wrapper
@timmer
def test1():
    time.sleep(1)
    print('in the test1')
test1()