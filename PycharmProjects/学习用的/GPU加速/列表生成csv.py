#Author：Alex.Zhang
import pandas as pd

#任意的多组列表
a = [1,2,3]
b = [4,5,6]
c=[7,8,9,10]

#字典中的key值即为csv中列名
dataframe = pd.DataFrame({'a_name':a,'b_name':b})
print(dataframe)

#将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("test.csv",index=False,sep=',')
data = pd.read_csv('test.csv')
print (data)
ke=data['a_name'].mean()
be=data['b_name'].mean()
data.loc[3]=[ke,be]
data['c_name']=c
data=data.to_csv('te.csv')
zhen=pd.read_csv('te.csv')
zhen.index=['beijing', 'shanghai', 'guangzhou','rtr']
print(zhen)
# cross=pd.crosstab(data['a_name'],data['b_name'])
# print (cross)
