#Author：Alex.Zhang
import time
user,password='alex','123'
def auth(auth_type):
    print('----------------------------------------1',auth_type)
    def out_wrapper(func):
        def wrapper(*args , **kwargs):
            print('wrapper de ',*args,**kwargs)
            print(auth_type)
            if auth_type=='ldap':
                print( 'what the fuck' )
            else:
                while True:
                    user1 = input( 'here to write your username:' )
                    password1 = input( 'password:' )
                    if user1 == user and password1 == password:
                        print( 'ojbk' )
                        res =  func( *args , **kwargs )
                        print( 'after auth-----------------' )
                        return res

        return wrapper
    return out_wrapper


@auth(auth_type='locoal')
def index():
    print('hello my custom')
    return 'ohahahahahahhaahhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
@auth(auth_type='ldap')
def home_page():
    time.sleep(1)
    print('hello,welcome here')
    return '000000000000000000000000000000000000000000000000000000000'
index()





