# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Braille_to_text import Ui_Braille_To_Text
from Image_to_braille import Ui_Image_To_Braille
from Image_to_text import Ui_Image_To_Text
from Braille_Image_to_text import Ui_Braille_Image_to_text

class Ui_Main(object):
    def openWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Braille_To_Text()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow1(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Image_To_Braille()
        self.ui.setupUi(self.window)
        self.window.show()     
    def openWindow2(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Image_To_Text()
        self.ui.setupUi(self.window)
        self.window.show()     
    def openWindow3(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Braille_Image_to_text()
        self.ui.setupUi(self.window)
        self.window.show()     

        
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(758, 625)
        Main.setStyleSheet("Background:url('abc.jpg')")
        self.label_3 = QtWidgets.QLabel(Main)
        self.label_3.setGeometry(QtCore.QRect(250, 0, 491, 91))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Main)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 91, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icons/E:/YOUR_PROJECT_DIRECTORY/im1.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Main)
        self.label.setGeometry(QtCore.QRect(220, 130, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Main)
        self.pushButton.setGeometry(QtCore.QRect(180, 230, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("Background-Color:rgb(61, 182, 226)")
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.openWindow3)
        
        self.pushButton_2 = QtWidgets.QPushButton(Main)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 310, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("Background-Color:rgb(61, 182, 226)")

        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_2.clicked.connect(self.openWindow2)
        
        self.pushButton_3 = QtWidgets.QPushButton(Main)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 390, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("Background-Color:rgb(61, 182, 226)")
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_3.clicked.connect(self.openWindow1)
        
        self.pushButton_4 = QtWidgets.QPushButton(Main)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 470, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("Background-Color:rgb(61, 182, 226)")
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.pushButton_4.clicked.connect(self.openWindow)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Form"))
        self.label_3.setText(_translate("Main", "Brebraille"))
        self.label.setText(_translate("Main", "Choose one of them:"))
        self.pushButton.setText(_translate("Main", "Braille Image To Text Convertor"))
        self.pushButton_2.setText(_translate("Main", "Image To Text Converter"))
        self.pushButton_3.setText(_translate("Main", "Image To Braille Converter"))
        self.pushButton_4.setText(_translate("Main", "Text To Braille Converter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

