#Author：Alex.Zhang
def normalize(v):
    norm = np.linalg.norm( v )
    if norm == 0:
        return v
    return v / norm


### two
# import numpy as np
# from sklearn.preprocessing import normalize
#
# x = np.random.rand( 1000 ) * 10
# norm1 = x / np.linalg.norm( x )
# norm2 = normalize( x[: , np.newaxis] , axis=0 ).ravel()
# print(x[: , np.newaxis])
import cv2 as cv
import numpy as np

src=cv.imread(r'1.png')
cv.namedWindow('input',cv.WINDOW_AUTOSIZE)
# cv.imshow('input',src)
gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)

gray=np.float32(gray)
print(gray)

dst=np.zeros(gray.shape,dtype=np.float32)
cv.normalize(gray,dst=dst,alpha=0,beta=1.0,norm_type=cv.NORM_MINMAX)

print(dst)
cv.imshow('NORM_MINMAX',np.uint8(dst*255)) #NORM_MINMAX:数组的数值被平移或缩放到一个指定的范围，线性归一化，一般较常用

dst=np.zeros(gray.shape,dtype=np.float32)
cv.normalize(gray,dst=dst,alpha=1.0,beta=0,norm_type=cv.NORM_INF)#NORM_INF:归一化数组的C-范数(绝对值的最大值)
print(dst)
cv.imshow('NORM_L1',np.uint8(dst*10000000))#NORM_L1 : 归一化数组的L1-范数(绝对值的和)

dst=np.zeros(gray.shape,dtype=np.float32)
cv.normalize(gray,dst=dst,alpha=1.0,beta=0,norm_type=cv.NORM_L2)#NORM_L2: 归一化数组的(欧几里德)L2-范数
print(dst)
cv.imshow('NORM_L2',np.uint8(dst*10000))

cv.waitKey(2)
#
