# class dog():
#     def __init__(self,name):
#         self.name=name
#     def bulk(self):
#         print('{a} is wangwangwang'.format(a=self.name))
#
# D1=dog('zhangruilai')
# D2=dog('lixueke')
# D1.bulk()
class Role( object ):
    def __init__(self , name , role , weapon , life_value=100 , money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print( "shooting..." )

    def got_shot(self):
        print( "ah...,I got shot..." )

    def buy_gun(self , gun_name):
        print( "%s just bought %s" %(self.name,gun_name)  )


r1 = Role('zhanghaonan','police','12')

r1.buy_gun('asdsad')