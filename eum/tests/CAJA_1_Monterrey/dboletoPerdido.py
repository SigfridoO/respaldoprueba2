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

PATH_LOGOS_1="/home/pi/Documents/CAJA_1_Monterrey/img/logotipo1.png"

class dBoletoPerdido(object):
    def __init__(self, dBoletoPerdido):
        dBoletoPerdido.setObjectName(_fromUtf8("dBoletoPerdido"))
        dBoletoPerdido.setWindowModality(QtCore.Qt.WindowModal)
        dBoletoPerdido.resize(600, 675)
        dBoletoPerdido.setMinimumSize(QtCore.QSize(600, 675))
        dBoletoPerdido.setMaximumSize(QtCore.QSize(600, 675))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(PATH_LOGOS_1)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dBoletoPerdido.setWindowIcon(icon)
        self.txtMarca = QtGui.QLineEdit(dBoletoPerdido)
        self.txtMarca.setGeometry(QtCore.QRect(250, 257, 271, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtMarca.setFont(font)
        self.txtMarca.setObjectName(_fromUtf8("txtMarca"))
        self.txtPlacas = QtGui.QLineEdit(dBoletoPerdido)
        self.txtPlacas.setGeometry(QtCore.QRect(250, 293, 271, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtPlacas.setFont(font)
        self.txtPlacas.setObjectName(_fromUtf8("txtPlacas"))
        self.txtModelo = QtGui.QLineEdit(dBoletoPerdido)
        self.txtModelo.setGeometry(QtCore.QRect(250, 330, 271, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtModelo.setFont(font)
        self.txtModelo.setStyleSheet(_fromUtf8(""))
        self.txtModelo.setObjectName(_fromUtf8("txtModelo")) 
        self.txtLicencia = QtGui.QLineEdit(dBoletoPerdido)
        self.txtLicencia.setGeometry(QtCore.QRect(250, 366, 271, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtLicencia.setFont(font)
        self.txtLicencia.setObjectName(_fromUtf8("txtLicencia"))
        self.label_4 = QtGui.QLabel(dBoletoPerdido)
        self.pushButton_2 = QtGui.QPushButton(dBoletoPerdido)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 580, 111, 41))
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
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(dBoletoPerdido)
        self.label_2.setGeometry(QtCore.QRect(81, 100, 151, 451))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(dBoletoPerdido)
        self.label_3.setGeometry(QtCore.QRect(245, 550, 111, 111))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(PATH_LOGOS_1)))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txtNombre = QtGui.QLineEdit(dBoletoPerdido)
        self.txtNombre.setGeometry(QtCore.QRect(250, 403, 271, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtNombre.setFont(font)
        self.txtNombre.setObjectName(_fromUtf8("txtNombre"))

        self.pushButton = QtGui.QPushButton(dBoletoPerdido)
        self.pushButton.setGeometry(QtCore.QRect(412, 580, 111, 41))
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
        self.txtTelefono = QtGui.QLineEdit(dBoletoPerdido)
        self.txtTelefono.setGeometry(QtCore.QRect(250, 440, 271, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtTelefono.setFont(font)
        self.txtTelefono.setObjectName(_fromUtf8("txtTelefono"))
        self.label = QtGui.QLabel(dBoletoPerdido)
        self.label.setGeometry(QtCore.QRect(146, 34, 321, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Return To Sender"))
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4.lower()
        self.label_4.setGeometry(QtCore.QRect(71, 110, 461, 131))
        self.label_4.setStyleSheet(_fromUtf8("background-color: rgb(181, 181, 181);\n"
		"border-radius: 15px;"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.labelTotal = QtGui.QLabel(dBoletoPerdido)
        self.labelTotal.setGeometry(QtCore.QRect(250, 500, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelTotal.setFont(font)
        self.labelTotal.setText(_fromUtf8(""))
        self.labelTotal.setObjectName(_fromUtf8("labelTotal"))
        self.labelFechout = QtGui.QLabel(dBoletoPerdido)
        self.labelFechout.setGeometry(QtCore.QRect(250, 158, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelFechout.setFont(font)
        self.labelFechout.setText(_fromUtf8(""))
        self.labelFechout.setObjectName(_fromUtf8("labelFechout"))
        self.labelHoraout = QtGui.QLabel(dBoletoPerdido)
        self.labelHoraout.setGeometry(QtCore.QRect(250, 192, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelHoraout.setFont(font)
        self.labelHoraout.setText(_fromUtf8(""))
        self.labelHoraout.setObjectName(_fromUtf8("labelHoraout"))
        self.labelTicket = QtGui.QLabel(dBoletoPerdido)
        self.labelTicket.setGeometry(QtCore.QRect(250, 120, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelTicket.setFont(font)
        self.labelTicket.setText(_fromUtf8(""))
        self.labelTicket.setObjectName(_fromUtf8("labelTicket"))

        self.retranslateUi(dBoletoPerdido)
        QtCore.QMetaObject.connectSlotsByName(dBoletoPerdido)
        
    def retranslateUi(self, dBoletoPerdido):
        dBoletoPerdido.setWindowTitle(_translate("dBoletoPerdido", "Boleto Perdido", None))
        self.pushButton_2.setText(_translate("dBoletoPerdido", "Cancelar", None))
        self.label_2.setText(_translate("dBoletoPerdido", "<html><head/><body><p>Boleto Suplido</p><p>Fecha de Salida</p><p>Hora de Salida<br/></p><p>Marca</p><p>Placas</p><p>Modelo</p><p>Licencia</p><p>Nombre</p><p>Telefono<br/></p><p>Importe</p></body></html>", None))
        self.pushButton.setText(_translate("dBoletoPerdido", "Aceptar", None))
        self.label.setText(_translate("dBoletoPerdido", "Registrar Boleto Perdido", None))

