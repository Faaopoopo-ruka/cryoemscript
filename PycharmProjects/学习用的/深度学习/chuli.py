#Author：Alex.Zhang
import pandas_profiling
import pandas as pd
data=pd.read_csv('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt')

data['age'].fillna(data['age'].mean(), inplace=True)
pfr = pandas_profiling.ProfileReport(data)
pfr.to_file('report.html')
# import pandas as pd
#
# df1 = pd.DataFrame({'key':['a','a','b','b'],'data1':range(4)})
# print (df1)
# df2 = pd.DataFrame({'key':['b','b','c','c'],'data2':range(4)})
# print (df2)
# print(pd.concat([df1,df2],axis=0))