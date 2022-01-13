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

class dRegistroUsuario(object):
    def __init__(self, dRegistroUsuario):
        dRegistroUsuario.setObjectName(_fromUtf8("dRegistroUsuario"))
        dRegistroUsuario.resize(600, 600)
        dRegistroUsuario.setMinimumSize(QtCore.QSize(600, 600))
        dRegistroUsuario.setMaximumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/logotipo1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dRegistroUsuario.setWindowIcon(icon)
        self.txtNombre = QtGui.QLineEdit(dRegistroUsuario)
        self.txtNombre.setGeometry(QtCore.QRect(270, 152, 270, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.txtNombre.setFont(font)
        self.txtNombre.setObjectName(_fromUtf8("txtNombre"))
        self.txtApm = QtGui.QLineEdit(dRegistroUsuario)
        self.txtApm.setGeometry(QtCore.QRect(270, 226, 270, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.txtApm.setFont(font)
        self.txtApm.setObjectName(_fromUtf8("txtApm"))
        self.txtApp = QtGui.QLineEdit(dRegistroUsuario)
        self.txtApp.setGeometry(QtCore.QRect(270, 189, 270, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.txtApp.setFont(font)
        self.txtApp.setText(_fromUtf8(""))
        self.txtApp.setObjectName(_fromUtf8("txtApp"))
        self.label_2 = QtGui.QLabel(dRegistroUsuario)
        self.label_2.setGeometry(QtCore.QRect(70, 154, 151, 281))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtUsuario = QtGui.QLineEdit(dRegistroUsuario)
        self.txtUsuario.setGeometry(QtCore.QRect(270, 260, 270, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.txtUsuario.setFont(font)
        self.txtUsuario.setObjectName(_fromUtf8("txtUsuario"))
        self.pushButton = QtGui.QPushButton(dRegistroUsuario)
        self.pushButton.setGeometry(QtCore.QRect(450, 530, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton{\n"
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
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(dRegistroUsuario)
        self.label.setGeometry(QtCore.QRect(170, 31, 271, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Return To Sender"))
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.txtPuesto = QtGui.QLineEdit(dRegistroUsuario)
        self.txtPuesto.setGeometry(QtCore.QRect(270, 333, 270, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.txtPuesto.setFont(font)
        self.txtPuesto.setObjectName(_fromUtf8("txtPuesto"))
        self.txtPassword = QtGui.QLineEdit(dRegistroUsuario)
        self.txtPassword.setGeometry(QtCore.QRect(270, 295, 270, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.txtPassword.setFont(font)
        self.txtPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.txtPassword.setObjectName(_fromUtf8("txtPassword"))
        self.pushButton_2 = QtGui.QPushButton(dRegistroUsuario)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 530, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton{\n"
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
        self.pushButton_2.setShortcut(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(dRegistroUsuario)
        self.label_3.setGeometry(QtCore.QRect(250, 461, 111, 111))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/logotipo1.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.cbxRol = QtGui.QComboBox(dRegistroUsuario)
        self.cbxRol.setGeometry(QtCore.QRect(270, 371, 270, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cbxRol.setFont(font)
        self.cbxRol.setObjectName(_fromUtf8("cbxRol"))
        self.cbxRol.addItem(_fromUtf8(""))
        self.cbxRol.addItem(_fromUtf8(""))
        self.cbxHorario = QtGui.QComboBox(dRegistroUsuario)
        self.cbxHorario.setGeometry(QtCore.QRect(270, 410, 270, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cbxHorario.setFont(font)
        self.cbxHorario.setObjectName(_fromUtf8("cbxHorario"))
        self.cbxHorario.addItem(_fromUtf8(""))
        self.cbxHorario.addItem(_fromUtf8(""))
        self.cbxHorario.addItem(_fromUtf8(""))

        self.retranslateUi(dRegistroUsuario)
        self.cbxRol.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dRegistroUsuario)

    def retranslateUi(self, dRegistroUsuario):
        dRegistroUsuario.setWindowTitle(_translate("dRegistroUsuario", "Registro de Usuarios", None))
        self.label_2.setText(_translate("dRegistroUsuario", "<html><head/><body><p>Nombre</p><p>Apellido Paterno</p><p>Apellido Materno</p><p>Usuario</p><p>Password</p><p>Puesto</p><p>Rol</p><p>Horario</p></body></html>", None))
        self.pushButton.setText(_translate("dRegistroUsuario", "Aceptar", None))
        self.pushButton.setShortcut(_translate("dRegistroUsuario", "Return", None))
        self.label.setText(_translate("dRegistroUsuario", "Registrar Usuario", None))
        self.pushButton_2.setText(_translate("dRegistroUsuario", "Cancelar", None))
        self.cbxRol.setProperty("currentText", _translate("dRegistroUsuario", "Cajero", None))
        self.cbxRol.setItemText(0, _translate("dRegistroUsuario", "Administrador", None))
        self.cbxRol.setItemText(1, _translate("dRegistroUsuario", "Cajero", None))
        self.cbxHorario.setItemText(0, _translate("dRegistroUsuario", "7:00 am - 15:00 pm", None))
        self.cbxHorario.setItemText(1, _translate("dRegistroUsuario", "14:00 pm - 22:00 pm", None))
        self.cbxHorario.setItemText(2, _translate("dRegistroUsuario", "22:00 pm - 7:00 am", None))

