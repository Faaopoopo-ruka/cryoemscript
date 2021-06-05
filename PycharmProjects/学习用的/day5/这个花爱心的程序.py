#Author：张浩楠
import random
import turtle
import datetime
import time
auth=datetime.datetime.now()
print('warning：现在时间是\033[31;1m %s\033[0m'%(auth))#规定格式
print('''你看现在都几点啦，已经不早啦，今天回去早点睡呀\n
      小可爱想要心心吗？''')
ap='yes'
timer=datetime.datetime.now()
count=0
while count<3:
    asd=input('yes or no:')
    if asd ==ap:
        aj=0
        while aj<3:
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
            ao=input('请输入验证码：')
            if ao==checkcode:
                print('恭喜你小可爱')
                # 生日快乐
                def love():
                    def func(x , y):
                        main()
                    turtle.title( '小可爱的小心心' )
                    lv = turtle.Turtle()
                    lv.hideturtle()
                    lv.getscreen().bgcolor( 'pink' )
                    lv.color( 'black' , 'red' )
                    lv.pensize( 10 )
                    lv.speed( 1 )
                    lv.up()
                    lv.goto( 0 , -150 )
                    # 开始画爱心
                    lv.down()
                    lv.begin_fill()
                    lv.goto( 0 , -150 )
                    lv.goto( -175.12 , -8.59 )
                    lv.left( 140 )
                    pos = []
                    for i in range( 19 ):
                        lv.right( 10 )
                        lv.forward( 20 )
                        pos.append( (-lv.pos()[0] , lv.pos()[1]) )
                    for item in pos[::-1]:
                        lv.goto( item )
                    lv.goto( 175.12 , -8.59 )
                    lv.goto( 0 , -150 )
                    lv.left( 50 )
                    lv.end_fill()
                    # 写字
                    lv.up()
                    lv.goto( 0 , 80 )
                    lv.down()
                    lv.write( "张莹宝宝" , font=(u"方正舒体" , 36 , "normal") , align="center" )
                    lv.up()
                    lv.goto( 0 , 0 )
                    lv.down()
                    lv.write( "最可爱！" , font=(u"方正舒体" , 36 , "normal") , align="center" )
                    lv.up()
                    lv.goto( 100 , -210 )
                    lv.down()
                    lv.write( "快点给我亲亲" , font=(u"华文琥珀" , 26 , "bold") , align="right" )
                    lv.up()
                    lv.goto( 160 , -190 )
                    lv.resizemode( 'user' )
                    lv.shapesize( 4 , 4 , 10 )
                    lv.color( 'red' , 'red' )
                    lv.onclick( func )
                    lv.showturtle()


                love()
            else:
                aj+=1
    else:
        count += 1
