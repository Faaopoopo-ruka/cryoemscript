#Author：Alex.Zhang
import pandas as pd
d={
    'name':['xiao','dan','qi'],
    'sex':['male','female','male'],
    'age':[23,24,24]
}
df=pd.DataFrame(d)
print(df)
print(df.query("age<24"))