# -*- coding: utf-8 -*-

PATH_IMAGEN_LOGOTIPO="InterfacesImagenesExp/logotipoEUM.png"
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
        #def setupUi(self, dcorteCaja):
        dcorteCaja.setObjectName(_fromUtf8("dcorteCaja"))
        dcorteCaja.setWindowModality(QtCore.Qt.WindowModal)
        dcorteCaja.resize(554, 438)
        dcorteCaja.setMinimumSize(QtCore.QSize(554, 438))
        dcorteCaja.setMaximumSize(QtCore.QSize(554, 438))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(PATH_IMAGEN_LOGOTIPO)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dcorteCaja.setWindowIcon(icon)
        dcorteCaja.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.comboBox = QtGui.QComboBox(dcorteCaja)
        self.comboBox.setGeometry(QtCore.QRect(115, 111, 331, 28))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        #self.comboBox.addItem(_fromUtf8(""))
        """
        Ponemos por defaltut la fecha actual del sistema
        """
        fechaY=int(time.strftime("%Y"))
        fechaM=int(time.strftime("%m"))
        fechaD=int(time.strftime("%d "))


        self.dateEdit = QtGui.QDateEdit(dcorteCaja)
        self.dateEdit.setGeometry(QtCore.QRect(245, 166, 201, 28))
        self.dateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(fechaY, fechaM, fechaD), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setDate(QtCore.QDate(fechaY, fechaM, fechaD))
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1817, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCurrentSection(QtGui.QDateTimeEdit.MonthSection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.label_3 = QtGui.QLabel(dcorteCaja)
        self.label_3.setGeometry(QtCore.QRect(222, 310, 111, 111))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(PATH_IMAGEN_LOGOTIPO)))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.dateEdit_2 = QtGui.QDateEdit(dcorteCaja)
        self.dateEdit_2.setGeometry(QtCore.QRect(245, 201, 201, 28))
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(fechaY, fechaM, fechaD), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setDate(QtCore.QDate(fechaY, fechaM, fechaD))
        self.dateEdit_2.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1817, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setCurrentSection(QtGui.QDateTimeEdit.MonthSection)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.pushButton_Cancelar = QtGui.QPushButton(dcorteCaja)
        self.pushButton_Cancelar.setGeometry(QtCore.QRect(60, 360, 140, 41))
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
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.label_2 = QtGui.QLabel(dcorteCaja)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 151, 151))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto Slab"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("bg-color: white;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(dcorteCaja)
        self.label.setGeometry(QtCore.QRect(150, 30, 311, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Return To Sender"))
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(dcorteCaja)
        self.pushButton.setGeometry(QtCore.QRect(385, 360, 140, 41))
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
        self.label_NumeroTer = QtGui.QLabel(dcorteCaja)
        self.label_NumeroTer.setGeometry(QtCore.QRect(250, 240, 171, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_NumeroTer.setFont(font)
        self.label_NumeroTer.setText(_fromUtf8(""))
        self.label_NumeroTer.setObjectName(_fromUtf8("label_NumeroTer"))
        """
        Extra el boton de ESP
        """
        self.pushButton2 = QtGui.QPushButton(dcorteCaja)
        self.pushButton2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton2.setGeometry(QtCore.QRect(0,0,0,0))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        """
        Fin del contenido extra
        """
        self.retranslateUi(dcorteCaja)
        QtCore.QMetaObject.connectSlotsByName(dcorteCaja)


    def retranslateUi(self, dcorteCaja):
        dcorteCaja.setWindowTitle(_translate("dcorteCaja", "Corte de Caja", None))
        self.comboBox.setItemText(0, _translate("dcorteCaja", "Total de Dia", None))
        self.comboBox.setItemText(1, _translate("dcorteCaja", "Corte entre Fechas", None))
        #self.comboBox.setItemText(2, _translate("dcorteCaja", "Corte entre Fechas", None))
        self.dateEdit.setDisplayFormat(_translate("dcorteCaja", "dd/MM/yyyy", None))
        self.dateEdit_2.setDisplayFormat(_translate("dcorteCaja", "dd/MM/yyyy", None))
        self.pushButton_Cancelar.setText(_translate("dcorteCaja", "Cancelar", None))
        self.label_2.setText(_translate("dcorteCaja", "<html><head/><body><p>Fecha Incio</p><p>Fecha Fin<br/></p><p><span style=\" font-weight:600;\">Número Terminal</span></p></body></html>", None))
        self.label.setText(_translate("dcorteCaja", "Corte de Caja", None))
        self.pushButton.setText(_translate("dcorteCaja", "Aceptar", None))
        self.pushButton.setShortcut(_translate("dcorteCaja", "Return", None))
        #Agregado
        self.pushButton2.setShortcut(_translate("dcorteCaja", "Escape", None))

"""
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dcorteCaja = QtGui.QDialog()
    ui = Ui_dcorteCaja()
    ui.setupUi(dcorteCaja)
    dcorteCaja.show()
    sys.exit(app.exec_())
"""
