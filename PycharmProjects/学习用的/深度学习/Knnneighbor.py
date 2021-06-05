#Author：Alex.Zhang

import numpy as np
from sklearn import neighbors
import warnings

warnings.filterwarnings( 'ignore' )# warning信息不打印，可有可无

knn = neighbors.KNeighborsClassifier() # 取得knn分类器

data = np.array( [[1 , 1 , 1 , 1] ,
[0.1 , 0.1 , 0.1 , 0.1] ,
[0.5 , 0.5 , 0.5 , 0.5] ,
[1 , 0.8 , 0.3 , 1] ,
[0.6 , 0.5 , 0.7 , 0.5] ,
[1 , 1 , 0.9 , 0.5] ,
[1 , 0.6 , 0.5 , 0.8] ,
[0.5 , 0.5 , 1 , 1] ,
[0.9 , 1 , 1 , 1] ,
[0.6 , 0.6 , 1 , 0.1] ,
[1 , 0.8 , 0.5 , 0.5] ,
[1 , 0.1 , 0.1 , 1] ,
[1 , 1 , 0.7 , 0.3] ,
[0.2 , 0.3 , 0.4, 0.5] ,
[0.5 , 1 , 0.6 , 0.6]
])

labels = np.array( ['美女' ,
'淑女' ,
'丑女' ,
'一般型' ,
'淑女' ,
'一般型' ,
'美女' ,
'一般型' ,
'淑女' ,
'美女' ,
'丑女' ,
 '可爱型' ,
 '可爱型' ,
 '淑女' ,
 '丑女'
])

knn.fit( data , labels )  # 导入数据进行训练

print( '预测类型为:' , knn.predict( [[0.8 , 1 , 1 , 1]] ) )
