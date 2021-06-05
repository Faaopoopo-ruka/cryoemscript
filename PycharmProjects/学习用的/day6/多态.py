__author__ = "Alex Li"

#同一种接口实现多种状态叫多态
class Animal:
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        pass #raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod#这个叫做静态方法
    def animal_talk(self):
        self.talk()

class Cat(Animal):
    def talk(self):
        print('Meow!')


class Dog(Animal):
    def talk(self):
        print('Woof! Woof!')


d = Dog("陈荣华")
#d.talk()

c = Cat("徐良伟")
#c.talk()
#
# def animal_talk(obj):
#     obj.talk()

Animal.animal_talk(c)
d.animal_talk(d)

