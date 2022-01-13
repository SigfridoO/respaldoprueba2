
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

class dTarifa(object):
    def __init__(self, dTarifa):
        dTarifa.setObjectName(_fromUtf8("dTarifa"))
        dTarifa.setWindowModality(QtCore.Qt.WindowModal)
        dTarifa.resize(510, 400)
        dTarifa.setMinimumSize(QtCore.QSize(510, 400))
        dTarifa.setMaximumSize(QtCore.QSize(510, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/logotipo1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dTarifa.setWindowIcon(icon)
        dTarifa.setWindowOpacity(0.0)
        self.label = QtGui.QLabel(dTarifa)
        self.label.setGeometry(QtCore.QRect(136, 30, 231, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Return To Sender"))
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(dTarifa)
        self.comboBox.setGeometry(QtCore.QRect(45, 100, 421, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        #self.comboBox.addItem(_fromUtf8(""))
        #self.comboBox.addItem(_fromUtf8(""))
        #self.comboBox.addItem(_fromUtf8(""))
        self.pushButton = QtGui.QPushButton(dTarifa)
        self.pushButton.setGeometry(QtCore.QRect(334, 330, 131, 41))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton{\n"
		"    border:1px solid #96d1f8;\n"
		"   border-top: 1px solid #96d1f8;\n"
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
        self.pushButton_2 = QtGui.QPushButton(dTarifa)
        self.pushButton_2.setGeometry(QtCore.QRect(45, 330, 131, 41))
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
        self.txtDestar = QtGui.QPlainTextEdit(dTarifa)
        self.txtDestar.setGeometry(QtCore.QRect(45, 141, 421, 151))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.txtDestar.setFont(font)
        self.txtDestar.setReadOnly(True)
        self.txtDestar.setPlainText(_fromUtf8(""))
        self.txtDestar.setBackgroundVisible(False)
        self.txtDestar.setObjectName(_fromUtf8("txtDestar"))
        self.label_2 = QtGui.QLabel(dTarifa)
        self.label_2.setGeometry(QtCore.QRect(420, 0, 91, 91))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("img/logotipo1.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(dTarifa)
        QtCore.QMetaObject.connectSlotsByName(dTarifa)
        

	
    def retranslateUi(self, dTarifa):
        dTarifa.setWindowTitle(_translate("dTarifa", "Seleccionar Tarifa - EUM", None))
        self.label.setText(_translate("dTarifa", "Seleccionar Tarifa", None))
        self.comboBox.setItemText(0, _translate("dTarifa", "2h Voluntario", None))
        self.comboBox.setItemText(1, _translate("dTarifa", "Locatario", None))
        self.comboBox.setItemText(2, _translate("dTarifa", "Boleto Perdido", None))
        self.pushButton.setText(_translate("dTarifa", "Seleccionar", None))
        self.pushButton.setShortcut(_translate("dTarifa", "Return", None))
        self.pushButton_2.setText(_translate("dTarifa", "Cancelar", None))
        self.pushButton_2.setShortcut(_translate("dTarifa", "Esc", None))
"""
		self.comboBox.setItemText(0, _translate("dTarifa", "2h Voluntario", None))
        self.comboBox.setItemText(1, _translate("dTarifa", "Fijo 15", None))
        self.comboBox.setItemText(2, _translate("dTarifa", "2h Voluntaria", None))
        self.comboBox.setItemText(3, _translate("dTarifa", "Boleto Perdido", None))
        self.comboBox.setItemText(4, _translate("dTarifa", "Locatario", None))
        self.comboBox.setItemText(5, _translate("dTarifa", "Proveedor", None))
"""
