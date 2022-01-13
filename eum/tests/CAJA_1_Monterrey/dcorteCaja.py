import time

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

class dcorteCaja(object):
    def __init__(self, dcorteCaja):
        dcorteCaja.setObjectName(_fromUtf8("dcorteCaja"))
        dcorteCaja.setWindowModality(QtCore.Qt.WindowModal)
        dcorteCaja.resize(554, 438)
        dcorteCaja.setMinimumSize(QtCore.QSize(554, 438))
        dcorteCaja.setMaximumSize(QtCore.QSize(554, 438))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/logotipo1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dcorteCaja.setWindowIcon(icon)
        self.comboBox = QtGui.QComboBox(dcorteCaja)
        self.comboBox.setGeometry(QtCore.QRect(115, 111, 331, 28))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        
        """
        Ponemos por defaul la fecha de hoy
        """
        fechaY=int(time.strftime("%Y"))
        fechaM=int(time.strftime("%m"))
        fechaD=int(time.strftime("%d"))
        
        self.dateEdit = QtGui.QDateEdit(dcorteCaja)
        self.dateEdit.setGeometry(QtCore.QRect(245, 166, 201, 28))
        self.dateEdit.setDate(QtCore.QDate(fechaY, fechaM, fechaD))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.label_3 = QtGui.QLabel(dcorteCaja)
        self.label_3.setGeometry(QtCore.QRect(222, 310, 111, 111))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/logotipo1.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.dateEdit_2 = QtGui.QDateEdit(dcorteCaja)
        self.dateEdit_2.setGeometry(QtCore.QRect(245, 201, 201, 28))
        self.dateEdit_2.setDate(QtCore.QDate(fechaY, fechaM, fechaD))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.pushButton_2 = QtGui.QPushButton(dcorteCaja)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 360, 111, 41))
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
        self.label_2 = QtGui.QLabel(dcorteCaja)
        self.label_2.setGeometry(QtCore.QRect(115, 171, 111, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Slab"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("bg-color: white;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(dcorteCaja)
        self.label.setGeometry(QtCore.QRect(185, 30, 211, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Return To Sender"))
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(dcorteCaja)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(245, 251, 81, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(dcorteCaja)
        self.pushButton.setGeometry(QtCore.QRect(385, 360, 111, 41))
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

        self.retranslateUi(dcorteCaja)
        QtCore.QMetaObject.connectSlotsByName(dcorteCaja)

    def retranslateUi(self, dcorteCaja):
        dcorteCaja.setWindowTitle(_translate("dcorteCaja", "Corte de Caja", None))
        self.comboBox.setItemText(0, _translate("dcorteCaja", "Total de Dia", None))
        self.comboBox.setItemText(1, _translate("dcorteCaja", "Tarifa", None))
        self.comboBox.setItemText(2, _translate("dcorteCaja", "Corte entre Fechas", None))
        self.comboBox.setItemText(3, _translate("dcorteCaja", "Turno Matutino", None))
        self.comboBox.setItemText(4, _translate("dcorteCaja", "Turno Vespertino", None))
        self.pushButton_2.setText(_translate("dcorteCaja", "Cancelar", None))
        self.label_2.setText(_translate("dcorteCaja", "<html><head/><body><p>Fecha Incio</p><p>Fecha Fin<br/></p><p><span style=\" font-weight:600;\">Caja ID</span><br/></p></body></html>", None))
        self.label.setText(_translate("dcorteCaja", "Corte de Caja", None))
        self.pushButton.setText(_translate("dcorteCaja", "Aceptar", None))
        self.pushButton.setShortcut(_translate("dcorteCaja", "Return", None))

