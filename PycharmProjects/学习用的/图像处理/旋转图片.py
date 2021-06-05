#Author：Alex.Zhang
import cv2
import numpy as np


def subimage(image , center , theta , width , height):
    theta *= np.pi / 180  # convert to rad
    v_x = (np.cos( theta ) , np.sin( theta ))
    v_y = (-np.sin( theta ) , np.cos( theta ))
    s_x = center[0] - v_x[0] * (width / 2) - v_y[0] * (height / 2)
    s_y = center[1] - v_x[1] * (width / 2) - v_y[1] * (height / 2)
    mapping = np.array( [[v_x[0] , v_y[0] , s_x] ,
                         [v_x[1] , v_y[1] , s_y]] )
    return cv2.warpAffine( image , mapping , (width , height) , flags=cv2.WARP_INVERSE_MAP ,
                           borderMode=cv2.BORDER_REPLICATE )


image = cv2.imread( 'form.jpg' )
image = subimage( image , center=(746 , 1104) , theta=0 , width=762 , height=428 )
# cv2.imwrite('patch.jpg', image)
cv2.imshow( 'patch.jpg' , image )

