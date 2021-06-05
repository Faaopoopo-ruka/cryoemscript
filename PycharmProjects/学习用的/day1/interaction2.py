# Author：Alex.Zhang
name = input( 'name:' )
age: int = int( input( 'age:' ) )  # integer
print( type( age ) )
job = input( 'job:' )
salary = input( 'salary:' )
info = '''
-------------------------------------info of %s-------------------------
name:%s
age:%d
job:%s
salary:%s
''' % (name, name, age, job, salary)
info1 = '''
-------------------------------------info of {0}-------------------------
Name:{0}
age:{1}
job:{2}
salary:{3}
'''.format( name, age, job, salary )
info2 = '''
-------------------------------------info of {_name}-------------------------
Name:{_name}
age:{_age}
job:{_job}
salary:{_salary}
'''.format(_name= name,
           _age=age,
           _job=job,
           _salary=salary)
print( info2 )
