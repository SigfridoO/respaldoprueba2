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

class dConfigurarTerminal(object):
    def __init__(self, dConfigurarTerminal):
        #def setupUi(self, dConfigurarTerminal):
        dConfigurarTerminal.setObjectName(_fromUtf8("dConfigurarTerminal"))
        dConfigurarTerminal.resize(600, 600)
        dConfigurarTerminal.setMinimumSize(QtCore.QSize(600, 600))
        dConfigurarTerminal.setMaximumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(PATH_IMAGEN_LOGOTIPO)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dConfigurarTerminal.setWindowIcon(icon)
        self.txtNombrePlaza = QtGui.QLineEdit(dConfigurarTerminal)
        self.txtNombrePlaza.setGeometry(QtCore.QRect(270, 170, 270, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.txtNombrePlaza.setFont(font)
        self.txtNombrePlaza.setObjectName(_fromUtf8("txtNombrePlaza"))
        self.txtLocalidadEstado = QtGui.QLineEdit(dConfigurarTerminal)
        self.txtLocalidadEstado.setGeometry(QtCore.QRect(270, 240, 270, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.txtLocalidadEstado.setFont(font)
        self.txtLocalidadEstado.setObjectName(_fromUtf8("txtLocalidadEstado"))
        self.txtLocalidadMunicipio = QtGui.QLineEdit(dConfigurarTerminal)
        self.txtLocalidadMunicipio.setGeometry(QtCore.QRect(270, 310, 270, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.txtLocalidadMunicipio.setFont(font)
        self.txtLocalidadMunicipio.setText(_fromUtf8(""))
        self.txtLocalidadMunicipio.setObjectName(_fromUtf8("txtLocalidadMunicipio"))
        self.label_Atributo = QtGui.QLabel(dConfigurarTerminal)
        self.label_Atributo.setGeometry(QtCore.QRect(20, 150, 241, 281))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Atributo.setFont(font)
        self.label_Atributo.setObjectName(_fromUtf8("label_Atributo"))
        self.pushButton_Aceptar = QtGui.QPushButton(dConfigurarTerminal)
        self.pushButton_Aceptar.setGeometry(QtCore.QRect(440, 530, 121, 41))
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
        self.label_Titulo = QtGui.QLabel(dConfigurarTerminal)
        self.label_Titulo.setGeometry(QtCore.QRect(70, 50, 451, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Return To Sender"))
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.label_Titulo.setFont(font)
        self.label_Titulo.setObjectName(_fromUtf8("label_Titulo"))
        self.pushButton_Cancelar = QtGui.QPushButton(dConfigurarTerminal)
        self.pushButton_Cancelar.setGeometry(QtCore.QRect(40, 530, 131, 41))
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
        self.label_Imagen = QtGui.QLabel(dConfigurarTerminal)
        self.label_Imagen.setGeometry(QtCore.QRect(250, 461, 111, 111))
        self.label_Imagen.setText(_fromUtf8(""))
        self.label_Imagen.setPixmap(QtGui.QPixmap(_fromUtf8(PATH_IMAGEN_LOGOTIPO)))
        self.label_Imagen.setScaledContents(True)
        self.label_Imagen.setObjectName(_fromUtf8("label_Imagen"))
        self.spinBox = QtGui.QSpinBox(dConfigurarTerminal)
        self.spinBox.setGeometry(QtCore.QRect(270, 370, 281, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Waree"))
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))

        """
        Extra el boton de ESP
        """
        self.pushButton2 = QtGui.QPushButton(dConfigurarTerminal)
        self.pushButton2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton2.setGeometry(QtCore.QRect(0,0,0,0))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        """
        Fin del contenido extra
        """


        self.retranslateUi(dConfigurarTerminal)
        QtCore.QMetaObject.connectSlotsByName(dConfigurarTerminal)

    def retranslateUi(self, dConfigurarTerminal):
        dConfigurarTerminal.setWindowTitle(_translate("dConfigurarTerminal", "Registro de Usuarios", None))
        self.label_Atributo.setText(_translate("dConfigurarTerminal", "<html><head/><body><p><span style=\" font-size:18pt;\">Nombre de la Plaza</span></p><p><span style=\" font-size:18pt;\"><br/>Localidad (Estado)</span></p><p><span style=\" font-size:18pt;\"><br/>Localidad Municipio</span></p><p><span style=\" font-size:18pt;\"><br/>No.Terminal</span></p></body></html>", None))
        self.pushButton_Aceptar.setText(_translate("dConfigurarTerminal", "Aceptar", None))
        self.pushButton_Aceptar.setShortcut(_translate("dConfigurarTerminal", "Return", None))
        self.label_Titulo.setText(_translate("dConfigurarTerminal", "Configurar Terminal", None))
        self.pushButton_Cancelar.setText(_translate("dConfigurarTerminal", "Cancelar", None))
        #Agregado
        self.pushButton2.setShortcut(_translate("dConfigurarTerminal", "Escape", None))

"""
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dConfigurarTerminal = QtGui.QDialog()
    ui = Ui_dConfigurarTerminal()
    ui.setupUi(dConfigurarTerminal)
    dConfigurarTerminal.show()
    sys.exit(app.exec_())
"""
