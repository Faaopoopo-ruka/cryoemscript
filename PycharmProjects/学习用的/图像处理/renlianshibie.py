#Author：Alex.Zhang
import cv2

#待检测的图片路径


#获取训练好的人脸的参数数据，这里直接从GitHub上使用默认值

face_cascade = cv2.CascadeClassifier()

#读取图片

image = cv2.imread('sf.jpg')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#探测图片中的人脸

faces = face_cascade.detectMultiScale(gray)
for(x,y,w,h) in faces:
    cv2.circle( image , ((x + x + w) // 2 , (y + y + h) // 2) , w // 2 , (0 , 255 , 0) , 2 )
cv2.imshow('Find Faces!',image)

cv2.waitKey(0)

