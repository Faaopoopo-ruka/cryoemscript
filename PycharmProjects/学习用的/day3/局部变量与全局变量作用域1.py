#Author：Alex.Zhang
# def test(name,age=13,**kwargs):
#     print(name)
#     print(age)
#     print(kwargs)
#     logger('test')
#
#
# def logger(source):
#     print('from {haha}'.format(haha=source))
# test('dasd',a='dasf',b='dfsf')
#在代码顶层的变量叫做全局变量
school='shengwu'
def change(name):
    global school#用这种方法改变全局变量
    school='fdfgfdgdh'
    print(school)
    print('before change',name)
    name='nimabi'#这就叫局部变量，只在函数中生效，这个函数就是这个变量的作用域，只能在函数中作用哦
    print('after change',name)
name='haha'
change(name)
print(name,school)
#以下是一种作死行为，千万别这么用，在函数内部定义全局变量
def hehe():
    global name
    name='jiji'
hehe()
print(name)
#在定义局部变量的子程序中，局部变量起作用，在外面，全局变量起作用
#除了字符之外的，稍微复杂的变量形式都无所谓局部变量和全局变量，在函数中进行改变同时也在全局进行了改变
name=['haha','ahsdhjk','asjdh','asdhg']

def fuck():
    name[0]='zhangying'
    print(name)
fuck()
print(name)