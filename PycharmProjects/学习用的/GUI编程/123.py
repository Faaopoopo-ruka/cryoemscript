# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '123.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(210, 370, 571, 192))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(50, 40, 296, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(460, 170, 85, 145))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 85, 85))
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 85, 85))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(80, 370, 47, 21))
        self.toolButton.setObjectName("toolButton")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")


        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "1"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "新建列"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "新建列"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "新建列"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "新建列"))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "新建列"))
        self.treeWidget.headerItem().setText(6, _translate("MainWindow", "新建列"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "123"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("MainWindow", "123"))
        self.treeWidget.topLevelItem(0).setText(2, _translate("MainWindow", "456"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "新建子项目"))
        self.treeWidget.topLevelItem(0).child(0).setText(1, _translate("MainWindow", "123"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "123"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Page 1"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Page 2"))
        self.toolButton.setText(_translate("MainWindow", "..."))


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
