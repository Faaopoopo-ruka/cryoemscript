#Author：Alex.Zhang
#面向对象：类（class）和面向过程：过程（def）、函数式编程（编程的方法论）：函数（def）
#函数就是逻辑化和过程化的一种编程方法
#函数首先是def,之后是注释，一定要养成习惯
def text():
    'The function of definition'
    print('in the fuc1')
    return 0
#过程就是没有RETURN的函数
def text2():
    'The function of definition'
    print( 'in the fuc2' )
x=text()
y=text2()
print('{a}'.format(a=x))
print('{b}'.format(b=y))