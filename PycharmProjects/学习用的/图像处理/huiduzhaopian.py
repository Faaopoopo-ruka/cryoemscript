#Author：Alex.Zhang
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img= cv.imread('orign.png',0)#把你文件名输入进来，尾缀必须有.jpg或.png
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
s1 = np.log( np.abs( fshift ) )
plt.subplot(111),plt.imshow(s1,'gray'),plt.title('original')
plt.show()

# plt.subplot( 111 )
# plt.axis( "off" )
# plt.imshow( img , cmap="gray" )
# plt.title( 'Gaussianlow' )
# plt.show()
