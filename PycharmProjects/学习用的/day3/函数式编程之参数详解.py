#Author：Alex.Zhang
'''''
def fuc1():
    'This is a test file'
    print('in the test 1')
#没有定义RETURN解释器就会给你返回一个NONE
def fuc2():
    'This is a test file'
    print('in the test 2')
    return 0
def fuc3():
    'This is a test file'
    print('in the test 3')
    return fuc2(),'hello',['alex','wupeiqi'],{'name':'alex'}
x=fuc1()
y=fuc2()
z=fuc3()
print(x)
print(y)
print(z)
#定义RETURN:当没有return时，return一个none。当return=0时，return一个0.当return多个值时，返回一个元组
'''
def test(x,y):#x,y为形参
    print(x)
    print(y)
test(1,22)#这叫位置参数
test(y=1,x=2)#1，2为实参，实参与形参必须是一一对应的关系,位置输出始终为X,Y,这叫关键参数
def test(x,y):#x,y为形参
    print(x)
    print(y)
    return 3,'over'
x=1
y=3
test(y=y,x=x)
test(6,y=3)#关键参数与位置参数同时存在的时候，只能写在位置参数的后面

print(test(x,y))
