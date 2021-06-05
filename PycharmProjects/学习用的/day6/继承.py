__author__ = "Alex Li"
# class People: 经典类
class People(object): #新式类
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.friends = []
        print("--doens't run ")
    def __eat(self):
        print("%s is eating..." % self.name)
    def talk(self):
        print("%s is talking..." % self.name)
    def sleep(self):
        print("%s is sleeping..." % self.name)
class Relation(object):
    def __init__(self,n1):
        print("init in relation")
    def make_friends(self,obj): #w1
        print("%s is making friends with %s" % (self.name,obj.name))
        self.friends.append(obj.name)
class Man(People,Relation,object):
    def __init__(self,name,age,money=100):
        super(Man,self).__init__(name,age) #新式类写法
        self.money= money
        print("%s 一出生就有%s money" %(self.name,self.money))
    def piao(self):
        print("%s is piaoing ..... 20s....done." % self.name)
    def sleep(self):
        People.sleep(self)
        print("man is sleeping ")
class Woman(People,Relation):
    def get_birth(self):
        print("%s is born a baby...." % self.name)
m1 = Man("NiuHanYang",22)
print(m1.name)
w1 = Woman("ChenRonghua",26)
w1.name = "陈三炮"
m1.make_friends(w1)
w2=Relation('dgdfgg')
print(m1.friends[0])
