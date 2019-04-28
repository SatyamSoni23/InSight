# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Braille_to_text.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


#import numpy as np
#from PIL import Image
#from pytesseract import image_to_string
#import PIL


from PyQt5 import QtCore, QtGui, QtWidgets

global void
global a
global b
global c
global d
global e
global f
global g
global h
global i
global j
global k
global l
global m
global n
global o
global p
global q
global r
global s
global t
global u
global v
global w
global x
global y
global z

charToArray = {
    " " : [[0,0],[0,0],[0,0]],
    "a" : [[1,0],[0,0],[0,0]],
    "b" : [[1,0],[1,0],[0,0]],
    "c" : [[1,1],[0,0],[0,0]],
    "d" : [[1,1],[0,1],[0,0]],
    "e" : [[1,0],[0,1],[1,0]],
    "f" : [[1,1],[1,0],[0,0]],
    "g" : [[1,1],[1,1],[0,0]],
    "h" : [[1,0],[1,1],[0,0]],
    "i" : [[0,1],[1,0],[1,0]],
    "j" : [[0,1],[1,1],[0,0]],
    "k" : [[1,0],[0,0],[1,0]],
    "l" : [[1,0],[1,0],[1,0]],
    "m" : [[1,1],[0,0],[1,0]],
    "n" : [[1,1],[0,1],[1,0]],
    "o" : [[1,0],[0,1],[1,1]],
    "p" : [[1,1],[1,0],[1,0]],
    "q" : [[1,1],[1,1],[1,0]],
    "r" : [[1,0],[1,1],[1,0]],
    "s" : [[0,1],[1,0],[1,0]],
    "t" : [[0,1],[1,1],[1,0]],
    "u" : [[1,0],[0,0],[1,1]],
    "v" : [[1,0],[1,0],[1,1]],
    "w" : [[0,1],[0,1],[1,1]],
    "x" : [[1,1],[0,0],[1,1]],
    "y" : [[1,1],[0,1],[1,1]],
    "z" : [[1,0],[0,1],[1,1]]
}

ascii_braille = {}

asciicodes = [' ','!','"','#','$','%','&','','(',')','*','+',',','-','.','/',
          '0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
          'r','s','t','u','v','w','x','y','z','[','\\',']','^','_']

brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢',
        '⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅',
        '⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵','⠪','⠳','⠻','⠘','⠸']

arrayLength = len(asciicodes)
counter = 0

while counter < arrayLength:
    ascii_braille[asciicodes[counter]] = brailles[counter]
    counter = counter + 1

letterToImgPath = {
    "a": "a.png",
    "b": "b.png",
    "c": "c.png",
    "d": "d.png",
    "e": "e.png",
    "f": "f.png",
    "g": "g.png",
    "h": "h.png",
    "i": "i.png",
    "j": "j.png",
    "k": "k.png",
    "l": "l.png",
    "m": "m.png",
    "n": "n.png",
    "o": "o.png",
    "p": "p.png",
    "q": "q.png",
    "r": "r.png",
    "s": "s.png",
    "t": "t.png",
    "u": "u.png",
    "v": "v.png",
    "w": "w.png",
    "x": "x.png",
    "y": "y.png",
    "z": "z.png",
    " ": "void.png",
}

def writeText(b_string):
    final_string = ''
    for letters in b_string:
        final_string = final_string + ascii_braille[letters.lower()]
    print(final_string)


def textToBraille(text):
    final_string = ''
    for char in text:
        char = char.lower()
        if char == "a":
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["a"]))
        elif char == "b":
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["b"]))
        elif char == "c":
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["c"]))
        elif char == "d":
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["d"]))
        elif char == "e": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["e"]))
        elif char == "f": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["f"]))
        elif char == "g":
            final_string = final_string + ascii_braille[char] 
            print(char + " " + str(charToArray["g"]))
        elif char == "h": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["h"]))
        elif char == "i":
            final_string = final_string + ascii_braille[char] 
            print(char + " " + str(charToArray["i"]))
        elif char == "j": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["j"]))
        elif char == "k": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["k"]))
        elif char == "l": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["l"]))
        elif char == "m": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["m"]))
        elif char == "n": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["n"]))
        elif char == "o":
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["o"]))
        elif char == "p": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["p"]))
        elif char == "q": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["q"]))
        elif char == "r": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["r"]))
        elif char == "s": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["s"]))
        elif char == "t": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["t"]))
        elif char == "u": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["u"]))
        elif char == "v": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["v"]))
        elif char == "w":
            final_string = final_string + ascii_braille[char] 
            print(char + " " + str(charToArray["w"]))
        elif char == "x": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["x"]))
        elif char == "y": 
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["y"]))
        elif char == "z":
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray["z"]))
        elif char == " ":
            final_string = final_string + ascii_braille[char]
            print(char + " " + str(charToArray[" "]))
    return final_string
    print(final_string)



class Ui_Braille_To_Text(object):
    #def signals(self):
        
    def calc(self):
        a=self.textEdit.toPlainText()
        textToBraille(a)        
        self.textEdit_2.setText(textToBraille(a))

    def setupUi(self, Braille_To_Text):
        Braille_To_Text.setObjectName("Braille_To_Text")
        Braille_To_Text.resize(771, 621)
        Braille_To_Text.setStyleSheet("Background-image:url('abc.jpg')")
        self.label_4 = QtWidgets.QLabel(Braille_To_Text)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 91, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icons/E:/YOUR_PROJECT_DIRECTORY/im1.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Braille_To_Text)
        self.label_3.setGeometry(QtCore.QRect(140, 0, 491, 91))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Braille_To_Text)
        self.pushButton.setGeometry(QtCore.QRect(270, 450, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("Background-Color:rgba(61, 182, 226,1)")
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.calc)
        #self.pushButton.clicked.connect()
        
        self.label = QtWidgets.QLabel(Braille_To_Text)
        self.label.setGeometry(QtCore.QRect(70, 190, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Braille_To_Text)
        self.textEdit.setGeometry(QtCore.QRect(230, 180, 461, 91))
        self.textEdit.setStyleSheet("background:rgb(224, 226, 226)")
        self.textEdit.setObjectName("textEdit")
        #a=self.textEdit.text()
        #b=textToBraille(a)
        
        self.label_2 = QtWidgets.QLabel(Braille_To_Text)
        self.label_2.setGeometry(QtCore.QRect(70, 310, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(Braille_To_Text)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 300, 461, 91))
        self.textEdit_2.setStyleSheet("background:rgb(224, 226, 226)")
        self.textEdit_2.setObjectName("textEdit_2")

        #self.textEdit_2.setText(b)

        self.retranslateUi(Braille_To_Text)
        QtCore.QMetaObject.connectSlotsByName(Braille_To_Text)

    def retranslateUi(self, Braille_To_Text):
        _translate = QtCore.QCoreApplication.translate
        Braille_To_Text.setWindowTitle(_translate("Braille_To_Text", "Form"))
        self.label_3.setText(_translate("Braille_To_Text", "Text to Braille Converter"))
        self.pushButton.setText(_translate("Braille_To_Text", "Convert"))
        self.label.setText(_translate("Braille_To_Text", "Text Script"))
        self.textEdit.setHtml(_translate("Braille_To_Text", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Braille_To_Text", "Braille Script"))
        self.textEdit_2.setHtml(_translate("Braille_To_Text", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Braille_To_Text = QtWidgets.QWidget()
    ui = Ui_Braille_To_Text()
    ui.setupUi(Braille_To_Text)
    Braille_To_Text.show()
    sys.exit(app.exec_())

