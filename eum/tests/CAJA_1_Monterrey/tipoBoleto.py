# -*- coding: utf-8 -*-

import escribirTipoBoleto as boleto

PATH_IMAGENES="/home/pi/Documents/CAJA_1_Monterrey/imagenesCobro/"

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class tipoBoleto(object):
    def setupUi(self, registro):
        registro.setObjectName(_fromUtf8("registro"))
        registro.resize(500, 250)#ancho y alto
        registro.setMinimumSize(QtCore.QSize(500, 250))
        registro.setMaximumSize(QtCore.QSize(500, 250))
        self.pushButton = QtGui.QPushButton(registro)
        self.pushButton.setGeometry(QtCore.QRect(60, 180, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(registro)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 180, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(registro)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 410, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(registro)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 410, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label = QtGui.QLabel(registro)
        self.label.setGeometry(QtCore.QRect(60, 30, 171, 131))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(PATH_IMAGENES+"walmart.jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(registro)
        self.label_2.setGeometry(QtCore.QRect(270, 30, 171, 131))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(PATH_IMAGENES+"sinSello.jpg")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(registro)
        self.label_3.setGeometry(QtCore.QRect(80, 250, 141, 151))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(PATH_IMAGENES+"taxi.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(registro)
        self.label_4.setGeometry(QtCore.QRect(290, 260, 141, 121))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8(PATH_IMAGENES+"sinSello.jpg")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.pushButton.clicked.connect(self.Suburbia)
        self.pushButton_2.clicked.connect(self.SinSello)
        self.pushButton_3.clicked.connect(self.Taxi)
        self.pushButton_4.clicked.connect(self.Banco)

        self.retranslateUi(registro)
        QtCore.QMetaObject.connectSlotsByName(registro)


    
    def Suburbia(self):
        print "Suburbia"
        boleto.putDato("conSuburbia")
        exit()
        pass

    def Banco(self):
        print "Banco"
        #boleto.putDato("conBanco")
        exit()
        pass
    def Taxi(self):
        print "Taxi"
        #boleto.putDato("taxi")
        #exit()
        pass
    def SinSello(self):
        print "SinSello"
        boleto.putDato("sin")
        exit()
        pass



    def retranslateUi(self, registro):
        registro.setWindowTitle(_translate("registro", "TIPO DE BOLETO", None))
        self.pushButton.setText(_translate("registro", "City Club", None))
        self.pushButton_2.setText(_translate("registro", "Sin Sello", None))
        self.pushButton_3.setText(_translate("registro", "Taxi", None))
        self.pushButton_4.setText(_translate("registro", "Banco", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    registro = QtGui.QDialog()
    ui = tipoBoleto()
    ui.setupUi(registro)
    registro.show()
    sys.exit(app.exec_())

