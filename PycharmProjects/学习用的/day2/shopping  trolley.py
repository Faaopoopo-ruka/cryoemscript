product_list = [
    ('brush' , '5') , ('shoes' , '300') , ('pencil' , '1')
               ]
shopping_list=[]
salary=input('input your salary: ')
if salary.isdigit():
    salary = int( salary )
else:
    print('writting error')
while True:
    for index,item in enumerate(product_list):
        print(index, item )
    userschoice=input('>>What do you want to choose?')
    if userschoice.isdigit():
        userschoice = int( userschoice )
        if userschoice<len(product_list) and userschoice>=0:
            p_item = product_list[userschoice][1]
            if p_item.isdigit():
                p_item = int( p_item )
            print('you have customed',p_item)
            if salary>=p_item:
                shopping_list.append(product_list[userschoice][0])
                shopping_name = product_list[userschoice][0]
                salary-=p_item
                print('balance:',salary)
                print( 'ADD %s into your shopping car,and your current salary is \033[31;1m %d\033[0m'%(shopping_name,salary))
            else:
                print('fuck up,loser in life and you can do more ,your salary is \033[44;1m %d\033[0m'%(salary))
        else:
            print('writing error')
        haha =input('Do you want to continue?')
        if haha !='y':
            for i in shopping_list:
                print(i)
            print('thank you for you coming')
            exit()
        else:
            continue
#Author：Alex.Zhang