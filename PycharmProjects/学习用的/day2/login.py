#Author：Alex.Zhang
_username='zybb'
_password='zybb'

while True:
    username = input( 'username:' )
    password = input( 'password:' )
    if _username==username and _password==password:
        print ('welcome login {name} '.format(name=username))
        break
    else:
        print ('Invalid password is {out}'.format(out=password))
