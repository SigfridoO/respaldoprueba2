# -*- coding: utf-8 -*-

PATH_IMAGEN_LOGOTIPO="InterfacesImagenesExp/logotipoEUM.png"

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

class dConfigurarFechaHora(object):
    def __init__(self, dConfigurarFechaHora):
        #def setupUi(self, dConfigurarFechaHora):
        dConfigurarFechaHora.setObjectName(_fromUtf8("dConfigurarFechaHora"))
        dConfigurarFechaHora.setEnabled(True)
        dConfigurarFechaHora.setMinimumSize(QtCore.QSize(500, 500))
        dConfigurarFechaHora.setMaximumSize(QtCore.QSize(500, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(PATH_IMAGEN_LOGOTIPO)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dConfigurarFechaHora.setWindowIcon(icon)
        self.label_Atributo = QtGui.QLabel(dConfigurarFechaHora)
        self.label_Atributo.setGeometry(QtCore.QRect(30, 200, 251, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Atributo.setFont(font)
        self.label_Atributo.setObjectName(_fromUtf8("label_Atributo"))
        self.pushButton_Aceptar = QtGui.QPushButton(dConfigurarFechaHora)
        self.pushButton_Aceptar.setGeometry(QtCore.QRect(340, 390, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_Aceptar.setFont(font)
        self.pushButton_Aceptar.setStyleSheet(_fromUtf8("QPushButton{\n"
"    border:1px solid #5b8a3c;\n"
"   border-top: 1px solid #5b8a3c;\n"
"   background: #5b8a3c;\n"
"   padding: 9px 18px;\n"
"   border-radius: 9px;\n"
"   color: white;\n"
"    font: 75 16pt \"Roboto Condensed\";\n"
"   /*text-decoration: none;*/\n"
"   vertical-align: middle;\n"
"\n"
"}\n"
"  \n"
"QPushButton:hover {\n"
"   border-top-color:rgb(77, 207, 57);\n"
"    background: rgb(77, 207, 57);\n"
"   }"))
        self.pushButton_Aceptar.setObjectName(_fromUtf8("pushButton_Aceptar"))
        self.label_Titulo = QtGui.QLabel(dConfigurarFechaHora)
        self.label_Titulo.setGeometry(QtCore.QRect(30, 50, 451, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Return To Sender"))
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.label_Titulo.setFont(font)
        self.label_Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Titulo.setObjectName(_fromUtf8("label_Titulo"))
        self.pushButton_Cancelar = QtGui.QPushButton(dConfigurarFechaHora)
        self.pushButton_Cancelar.setGeometry(QtCore.QRect(30, 390, 129, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_Cancelar.setFont(font)
        self.pushButton_Cancelar.setStyleSheet(_fromUtf8("QPushButton{\n"
"   border:1px solid rgb(165, 0, 0);\n"
"   border-top: rgb(165, 0, 0);\n"
"   background: rgb(165, 0, 0);\n"
"   padding: 9px 18px;\n"
"   border-radius: 9px;\n"
"   color: white;\n"
"   font-size: 16px;\n"
"    font: 75 16pt \"Roboto Condensed\";\n"
"   /*text-decoration: none;*/\n"
"   vertical-align: middle;\n"
"\n"
"}\n"
"  \n"
"QPushButton:hover {\n"
"   border-top-color: rgb(235, 0, 3);\n"
"    background:rgb(235, 0, 3);\n"
"   }"))
        self.pushButton_Cancelar.setShortcut(_fromUtf8(""))
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.label_Imagen = QtGui.QLabel(dConfigurarFechaHora)
        self.label_Imagen.setGeometry(QtCore.QRect(200, 340, 111, 111))
        self.label_Imagen.setText(_fromUtf8(""))
        self.label_Imagen.setPixmap(QtGui.QPixmap(_fromUtf8(PATH_IMAGEN_LOGOTIPO)))
        self.label_Imagen.setScaledContents(True)
        self.label_Imagen.setObjectName(_fromUtf8("label_Imagen"))


        self.timeEditHora = QtGui.QLineEdit(dConfigurarFechaHora)
        self.timeEditHora.setGeometry(QtCore.QRect(310, 260, 150, 31))
        self.timeEditHora.setObjectName(_fromUtf8("timeEditHora"))
        
        self.dateEditFecha = QtGui.QLineEdit(dConfigurarFechaHora)
        self.dateEditFecha.setGeometry(QtCore.QRect(310, 200, 150, 31))
        self.dateEditFecha.setObjectName(_fromUtf8("dateEditFecha"))
        """
        Extra el boton de ESP
        """
        self.pushButton2 = QtGui.QPushButton(dConfigurarFechaHora)
        self.pushButton2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton2.setGeometry(QtCore.QRect(0,0,0,0))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        """
        Fin del contenido extra
        """
        self.retranslateUi(dConfigurarFechaHora)
        QtCore.QMetaObject.connectSlotsByName(dConfigurarFechaHora)

    def retranslateUi(self, dConfigurarFechaHora):
        dConfigurarFechaHora.setWindowTitle(_translate("dConfigurarFechaHora", "Configurar Fecha y Hora", None))
        self.label_Atributo.setText(_translate("dConfigurarFechaHora", "<html><head/><body><p><span style=\" font-size:18pt;\">Fecha (dd/mm/aaaa)<br/></span></p><p><span style=\" font-size:18pt;\">Hora (hh:mm:ss)</span></p><p><br/></p></body></html>", None))
        self.pushButton_Aceptar.setText(_translate("dConfigurarFechaHora", "Aceptar", None))
        self.pushButton_Aceptar.setShortcut(_translate("dConfigurarFechaHora", "Return", None))
        self.label_Titulo.setText(_translate("dConfigurarFechaHora", "Fecha y Hora", None))
        self.pushButton_Cancelar.setText(_translate("dConfigurarFechaHora", "Cancelar", None))
        #Agregado
        self.pushButton2.setShortcut(_translate("dConfigurarFechaHora", "Escape", None))


"""
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dConfigurarFechaHora = QtGui.QDialog()
    ui = Ui_dConfigurarFechaHora()
    ui.setupUi(dConfigurarFechaHora)
    dConfigurarFechaHora.show()
    sys.exit(app.exec_())
"""
