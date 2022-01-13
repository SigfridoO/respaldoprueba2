
from PyQt4 import QtCore, QtGui


PATH_LOGOS_1="/home/pi/Documents/CAJA_1_Monterrey/img/logotipo1.png"
PATH_LOGOS_2="/home/pi/Documents/CAJA_1_Monterrey/img/login-user.png"
PATH_LOGOS_3="/home/pi/Documents/CAJA_1_Monterrey/img/login-psw.png"


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

class dLogin(object):
    def __init__(self, dLogin):
        dLogin.setObjectName(_fromUtf8("dLogin"))
        dLogin.resize(500, 370)
        dLogin.setMinimumSize(QtCore.QSize(500, 370))
        dLogin.setMaximumSize(QtCore.QSize(500, 370))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(PATH_LOGOS_1)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dLogin.setWindowIcon(icon)
        dLogin.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.pushButton = QtGui.QPushButton(dLogin)
        self.pushButton.setGeometry(QtCore.QRect(324, 300, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("12 Roboto Condensed"))
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton{\n"
		"    border:1px solid #5b8a3c;\n"
		"   border-top: 1px solid #5b8a3c;\n"
		"   background: #5b8a3c;\n"
		"   padding: 9px 18px;\n"
		"   border-radius: 9px;\n"
		"   color: white;\n"
		"    font: 75 pt 12 \"Roboto Condensed\";\n"
		"   /*text-decoration: none;*/\n"
		"   vertical-align: middle;\n"
		"\n"
		"}\n"
		"  \n"
		"QPushButton:hover {\n"
		"   border-top-color:rgb(77, 207, 57);\n"
		"    background: rgb(77, 207, 57);\n"
		"   }\n"
		"QPushButton:change {\n"
		"   border-top-color:rgb(77, 207, 57);\n"
		"    background: rgb(77, 207, 57);\n"
		"   }\n"
		""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        self.pushButton2 = QtGui.QPushButton(dLogin)
        self.pushButton2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton2.setGeometry(QtCore.QRect(0,0,0,0))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))        
        self.label = QtGui.QLabel(dLogin)
        self.label.setGeometry(QtCore.QRect(140, 30, 221, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Return To Sender"))
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(dLogin)
        self.label_3.setGeometry(QtCore.QRect(50, 122, 71, 71))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(PATH_LOGOS_2)))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.label_4 = QtGui.QLabel(dLogin)
        self.label_4.setGeometry(QtCore.QRect(370, 30, 71, 71))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8(PATH_LOGOS_1)))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(dLogin)
        self.lineEdit.setGeometry(QtCore.QRect(150, 142, 291, 30))
        self.lineEdit.setStyleSheet(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2 = QtGui.QLineEdit(dLogin)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 230, 291, 30))
        self.lineEdit_2.setInputMask(_fromUtf8(""))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setProperty("clearButtonEnabled", False)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit"))        
        self.label_2 = QtGui.QLabel(dLogin)
        self.label_2.setGeometry(QtCore.QRect(50, 210, 71, 71))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(PATH_LOGOS_3)))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.elabel = QtGui.QLabel(dLogin)
        self.elabel.setGeometry(QtCore.QRect(50, 290, 261, 61))
        self.elabel.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.elabel.setText(_fromUtf8(""))
        self.elabel.setObjectName(_fromUtf8("elabel"))

        self.retranslateUi(dLogin)
        QtCore.QMetaObject.connectSlotsByName(dLogin)

    def retranslateUi(self, dLogin):
        dLogin.setWindowTitle(_translate("dLogin", "Login", None))
        self.pushButton.setText(_translate("dLogin", "Acceder", None))
        self.pushButton.setShortcut(_translate("dLogin", "Return", None))
        self.pushButton2.setShortcut(_translate("dLogin", "Escape", None))
        self.label.setText(_translate("dLogin", "Iniciar Sesion", None))

