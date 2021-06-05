#Author：Alex.Zhang
import random

print(random.randint(1,4))#随机整数
print(random.randrange(1,2))
print(random.choice('ajsdhjagdadgh'))
print(random.sample('atgc',2))
print(random.sample(['a','t','g','c'],3))
print(random.sample('helladsas',4))
a=[1,1,5,5,4,7]
print(a)
random.shuffle(a)
print(a)#以后shuffle命令只能这么玩懂不懂

#五位验证码成功
import random
checkcode=''
for i in range(5):
    current=random.randint(1,6)
    if i==current:
        a=chr(random.randint(65,90))
    else:
        a=random.randint(0,9)
    checkcode+=str(a)
print(checkcode)
print(random.sample('atgc',2))




