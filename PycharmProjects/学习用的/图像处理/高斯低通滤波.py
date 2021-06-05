#Author：zhanghaonan
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

def GaussianLowFilter(image,d):

    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    s1 = np.log( np.abs( fshift ) )
    def make_transform_matrix(d):
        transfor_matrix = np.zeros(image.shape)
        center_point = tuple(map(lambda x:(x-1)/2,s1.shape))
        for i in range(transfor_matrix.shape[0]):
            for j in range(transfor_matrix.shape[1]):
                def cal_distance(pa,pb):
                    from math import sqrt
                    dis = sqrt((pa[0]-pb[0])**2+(pa[1]-pb[1])**2)
                    return dis
                dis = cal_distance(center_point,(i,j))
                transfor_matrix[i,j] = np.exp(-(dis**2)/(2*(d**2)))
        return transfor_matrix
    d_matrix = make_transform_matrix(d)
    new_img = np.abs(np.fft.ifft2(np.fft.ifftshift(fshift*d_matrix)))
    return new_img
def do_it(filename,distance):
    img= cv.imread(filename,0)#把你文件名输入进来，尾缀必须有.jpg或.png
    img_d1=GaussianLowFilter(img,distance)
    plt.subplot(111)
    plt.axis("off")
    plt.imshow(img_d1,cmap="gray")
    plt.title('Gaussianlow')
    plt.show()
if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(
        description='高斯滤波' ,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument( '-i' , '--input' , help='输入你的照片路径' )
    parser.add_argument( '-d' , '--distance' , help='低通滤波大小(default = 1)',type=float )
    parser.add_argument( '-v' , '--version' , action='version' , version='v. 1.0' )
    args = parser.parse_args()
    if not args.input:
        print( '{0}\nPlease provide an input file.\n{0}'.format( 50 * '-' ) )
        parser.print_help()
        quit()
    if not args.distance:
        args.distance=1
    do_it(args.input,args.distance)
