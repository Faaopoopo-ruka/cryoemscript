import numpy as np
from eulerangles import euler2matrix
from eulerangles import matrix2euler
eulers = np.array([30, 60, 75])
rotation_matrix1 = euler2matrix(eulers,
                               axes='zyz',
                               intrinsic=True,
                               right_handed_rotation=True)
print(rotation_matrix1)
eulers = matrix2euler(rotation_matrix1,
                      axes='zyz',
                      intrinsic=True,
                      right_handed_rotation=True)
print(eulers)

#star文件操作
import starfile
def read_starfile(file):
    df = starfile.open(file)
    return df
def extract_oula(data):
    df=data
    v_want = df[['rlnAngleRot','rlnAngleTilt','rlnAnglePsi']]
    return v_want
def write_starfile(df,tomo):
    starfile.new(df, tomo+'.star')
def remove_starfile(df):
    new_want=df.drop(['rlnAngleRot','rlnAngleTilt','rlnAnglePsi'], axis=1)
    return new_want
def add_starfile(df1,df2):
    result = pd.concat([df1, df2], axis=1)
    return result
op1=read_starfile('no_rotation_good.star')
op2=extract_oula(op1)
op3=op2.values
op4=read_starfile('run_it025_data.star')
op5=extract_oula(op4)
op6=op5.values
op7=remove_starfile(op4)
print(op7.head(5))
import pandas as pd

df = pd.DataFrame(columns=['rlnAngleRot','rlnAngleTilt','rlnAnglePsi'])

for i in range(0,op3.shape[0]-1):
    ang1=op6[i]
    ang2=op3[i]

    rotation_matrix1 = euler2matrix(ang1,
                                    axes='zyz',
                                    intrinsic=True,
                                    right_handed_rotation=True)
    rotation_matrix2 = euler2matrix(ang2,
                                    axes='zyz',
                                    intrinsic=True,
                                    right_handed_rotation=True)
    rotation_matrix3=rotation_matrix1*rotation_matrix2
    eulers = matrix2euler(rotation_matrix3,
                          axes='zyz',
                          intrinsic=True,
                          right_handed_rotation=True)


    df.loc[i] = [eulers[0],eulers[1],eulers[2]]  # 其中loc[]中需要加入的是插入地方dataframe的索引，默认是整数型
print(df.head(5))
op8=add_starfile(op7,df)
print(op8.head(5))
op9=write_starfile(op8,'transform')

# for index, row in op2.iterrows():
#     print(np.array(row))