#Author：Alex.Zhang
#这就叫嵌套函数，一定所有的内部函数都要调用哦，内部函数相当于局部变量
def foo():
    print('in the foo')
    def bar():
        print('this is in bar')
    bar()
    return adsd
return asd
foo()