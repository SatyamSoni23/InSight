# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 22:11:59 2019

@author: DELL
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from keras.models import load_model
import string
import cv2
import numpy as np
class Ui_Braille_Image_to_text(object):
    def calc(self):
        path=self.textEdit.toPlainText()
        alphabet = list(string.ascii_lowercase)
        cur_pos = 0
        target = {}
        for letter in alphabet:
            target[letter] = [0] * 27
            target[letter][cur_pos] = 1
            cur_pos += 1
        target[' '] = [0] * 27
        target[' '][26] = 1
        
        model = load_model('braille_train.h5')
        pred_img = cv2.imread(path,cv2.IMREAD_COLOR)
        pred_img = cv2.resize(pred_img, (28,28))
        pred_img = pred_img.astype(np.float32)/255.0
        pred_img = np.expand_dims(pred_img,axis=0)
        pred_lb = model.predict(pred_img)
        for j in range(len(pred_lb[0])):
            if pred_lb[0][j] > 0.6:
                pred_lb[0][j] = 1.0
            else:
                pred_lb[0][j] = 0.0
        for key,value in target.items():
            if np.array_equal(np.asarray(pred_lb[0]),np.asarray(value)):
                print(key)
                self.textEdit_2.setText(key)
        
    def setupUi(self, Image_To_Text):
        Image_To_Text.setObjectName("Image_To_Text")
        Image_To_Text.resize(768, 615)
        Image_To_Text.setStyleSheet("Background-image:url('abc.jpg')")
        self.pushButton = QtWidgets.QPushButton(Image_To_Text)
        self.pushButton.setGeometry(QtCore.QRect(270, 450, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("Background-Color:rgba(61, 182, 226,1)")
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.calc)
        
        self.textEdit = QtWidgets.QTextEdit(Image_To_Text)
        self.textEdit.setGeometry(QtCore.QRect(230, 180, 461, 91))
        self.textEdit.setStyleSheet("background:rgb(224, 226, 226)")
        
        self.textEdit.setObjectName("textEdit")
        
        self.label_3 = QtWidgets.QLabel(Image_To_Text)
        self.label_3.setGeometry(QtCore.QRect(140, 0, 491, 91))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Image_To_Text)
        self.label.setGeometry(QtCore.QRect(70, 190, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Image_To_Text)
        self.label_2.setGeometry(QtCore.QRect(70, 310, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(Image_To_Text)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 300, 461, 91))
        self.textEdit_2.setStyleSheet("background:rgb(224, 226, 226)")
        
        self.textEdit_2.setObjectName("textEdit_2")
        
        self.label_4 = QtWidgets.QLabel(Image_To_Text)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 91, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icons/E:/YOUR_PROJECT_DIRECTORY/im1.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Image_To_Text)
        QtCore.QMetaObject.connectSlotsByName(Image_To_Text)
        
        

    def retranslateUi(self, Image_To_Text):
        _translate = QtCore.QCoreApplication.translate
        Image_To_Text.setWindowTitle(_translate("Image_To_Text", "Form"))
        self.pushButton.setText(_translate("Image_To_Text", "Convert"))
        self.textEdit.setHtml(_translate("Image_To_Text", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Image_To_Text", "Braille Image Converter"))
        self.label.setText(_translate("Image_To_Text", "Braille Image Path"))
        self.label_2.setText(_translate("Image_To_Text", " Your Text"))
        self.textEdit_2.setHtml(_translate("Image_To_Text", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Image_To_Text = QtWidgets.QWidget()
    ui = Ui_Braille_Image_to_text()
    ui.setupUi(Image_To_Text)
    Image_To_Text.show()
    sys.exit(app.exec_())

