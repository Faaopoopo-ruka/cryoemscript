#Author：Alex.Zhang
# -*- coding: utf-8 -*-
# @Time    : 2017/11/6 22:54
# @Author  : aikes
# @Email   : 13937992699@139.com
# @File    : main.py
# @Software:    python3.6.3
#               opencv3.3.0
#               pyqt5
#               pycharm 2017.2

from test import Ui_MainWindow  # 导入uitestPyQt5.ui转换为uitestPyQt5.py中的类
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import QFileDialog,QInputDialog
import cv2
import sys
import numpy as np

cv2.namedWindow('MAT',0)
cv2.resizeWindow('MAT',480,360)
img=cv2.imread('c://girl.png')
cv2.imshow('MAT',img)

class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # 建立的是Main Window项目，故此处导入的是QMainWindow
    # class myform(QWidget,Ui_Form):如建立的是Widget项目，导入的是QWidget
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
#####################################主函数代码#################
    def btn_ShowURL(self):
        filename=self.plainTextEdit.toPlainText()
        ret,img=cv2.VideoCapture(filename).read()
        cv2.imshow('MAT',img)

    def btn_OpenFile(self):
        filename = QFileDialog.getOpenFileName(self,'.png','c:')
        self.label.setPixmap(QtGui.QPixmap(filename[0]))

    def btn_Change(self):
        self.textEdit.setText('世界，我来了！')

    def btn_Dialog(self):
        url, ok = QInputDialog.getText(self, "Input Dialog", "键入网络地址:")
        if ok:
            cap=cv2.VideoCapture(url)
            ret, img=cap.read()
            #cv2.imshow('MAT',img)
            self.label.setPixmap(QPixmap.fromImage(cvMatToQimg(img)))

###########################################################
def cvMatToQimg(mat):
    mat = cv2.cvtColor(mat, cv2.COLOR_BGR2RGB)
    #mat=cv2.cvtColor(mat,cv2.COLOR_BGR2HSV)
    #mat = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)
    return QImage(mat.tostring(), mat.shape[1], mat.shape[0], mat.shape[2] * mat.shape[1], QtGui.QImage.Format_RGB888)

app = QtWidgets.QApplication(sys.argv)
window = Mywindow()
window.show()
# window=myform()   #如果是QWidget
#windows.show()
#app.exec_()
sys.exit(app.exec_())
