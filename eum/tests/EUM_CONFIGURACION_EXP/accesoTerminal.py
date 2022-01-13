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

class dAccesoConfigurarTerminal(object):
    def __init__(self, dAccesoConfigurarTerminal):
    #def setupUi(self, dAccesoConfigurarTerminal):
        dAccesoConfigurarTerminal.setObjectName(_fromUtf8("dAccesoConfigurarTerminal"))
        dAccesoConfigurarTerminal.resize(530, 135)
        dAccesoConfigurarTerminal.setMinimumSize(QtCore.QSize(530, 135))
        dAccesoConfigurarTerminal.setMaximumSize(QtCore.QSize(530, 135))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(PATH_IMAGEN_LOGOTIPO)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dAccesoConfigurarTerminal.setWindowIcon(icon)
        self.pushButton_Acceder = QtGui.QPushButton(dAccesoConfigurarTerminal)
        self.pushButton_Acceder.setGeometry(QtCore.QRect(367, 80, 101, 31))
        self.pushButton_Acceder.setObjectName(_fromUtf8("pushButton_Acceder"))
        self.palabraMagica = QtGui.QLineEdit(dAccesoConfigurarTerminal)
        self.palabraMagica.setGeometry(QtCore.QRect(70, 30, 400, 32))
        self.palabraMagica.setEchoMode(QtGui.QLineEdit.Password)
        self.palabraMagica.setObjectName(_fromUtf8("palabraMagica"))
        self.comboBox = QtGui.QComboBox(dAccesoConfigurarTerminal)
        self.comboBox.setGeometry(QtCore.QRect(70, 70, 251, 32))
        self.comboBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        """
        Extra el boton de ESP
        """
        self.pushButton2 = QtGui.QPushButton(dAccesoConfigurarTerminal)
        self.pushButton2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton2.setGeometry(QtCore.QRect(0,0,0,0))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        """
        Fin del contenido extra
        """


        self.retranslateUi(dAccesoConfigurarTerminal)
        QtCore.QMetaObject.connectSlotsByName(dAccesoConfigurarTerminal)

    def retranslateUi(self, dAccesoConfigurarTerminal):
        dAccesoConfigurarTerminal.setWindowTitle(_translate("dAccesoConfigurarTerminal", "Acceso para programadores", None))
        self.pushButton_Acceder.setText(_translate("dAccesoConfigurarTerminal", "Acceder", None))
        self.pushButton_Acceder.setShortcut(_translate("dAccesoConfigurarTerminal", "Return", None))
        self.comboBox.setItemText(0, _translate("dAccesoConfigurarTerminal", "Configurar Datos de Terminal", None))
        self.comboBox.setItemText(1, _translate("dAccesoConfigurarTerminal", "Corte de Terminal", None))
        self.comboBox.setItemText(2, _translate("dAccesoConfigurarTerminal", "Configurar Fecha de apagar equipo", None))
        self.comboBox.setItemText(3, _translate("dAccesoConfigurarTerminal", "APAGAR EQUIPO", None))
        #Agregado
        self.pushButton2.setShortcut(_translate("dAccesoConfigurarTerminal", "Escape", None))


"""

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dAccesoConfigurarTerminal = QtGui.QDialog()
    ui = Ui_dAccesoConfigurarTerminal()
    ui.setupUi(dAccesoConfigurarTerminal)
    dAccesoConfigurarTerminal.show()
    sys.exit(app.exec_())
"""
