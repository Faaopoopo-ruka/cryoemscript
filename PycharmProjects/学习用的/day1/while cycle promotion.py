# Author：Alex.Zhang
zhang_ying_age = '22'
count = 0
while count < 3:
    age = input( 'zhang_ying_age:' )
    if zhang_ying_age == age:
        print( "ojbk" )
        break
    elif zhang_ying_age < age:
        print( "fuck you" )
    else:
        print( "think bigger" )
    count += 1
    if count==3:
        continue_confirm=input('Do you want to continue(y/n)')
        if continue_confirm!='n':
            count=0
else:
    print( 'game over' )
#Author：Alex.Zhang