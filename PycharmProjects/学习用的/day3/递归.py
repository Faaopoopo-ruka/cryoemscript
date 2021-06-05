#Author：Alex.Zhang
#什么叫递归？在函数的内部，可以调用其他函数，如果一个函数在内部调用自己，那这个函数叫递归函数
#必须有一个明确的结束条件
# def fuc():
#     'this fuction is for haha'
#     print('nimabi')
#     return 1
# fuc()
# print(fuc())
# #递归
# def count(n):
#     print(n)
#     return count(n+1)
# count(0)
def cal(n):
    print(n)
    if int(n/2)>0:
        return cal(int(n/2))
    print('----',n)
cal(10)
