# Author：Alex.Zhang
import time

def motherfucker(func):
    def wrapper():
        time_format='%y-%m-%d-%a-%g %X'
        time_current=time.strftime(time_format)
        'this fuction is for the latter work'
        print('enheng')

        with open( 'mabi' , 'a' ) as f:
            f.write( '   time%s\n'%time_current)
            func()
    return wrapper
@motherfucker
def text1():
    'The function of definition'
    with open( 'mabi' , 'a' ) as f:
        f.write('nihao')
text1()
