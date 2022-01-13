
PATH_LOGOS_1="/home/pi/Documents/EUM_CAJA/img/logotipo1.png"

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

class dAccess(object):
    def __init__(self, dAccess):
        dAccess.setObjectName(_fromUtf8("dAccess"))
        dAccess.resize(530, 135)
        dAccess.setMinimumSize(QtCore.QSize(530, 135))
        dAccess.setMaximumSize(QtCore.QSize(530, 135))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(PATH_LOGOS_1)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dAccess.setWindowIcon(icon)
        self.pushButton = QtGui.QPushButton(dAccess)
        self.pushButton.setGeometry(QtCore.QRect(367, 80, 101, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton2 = QtGui.QPushButton(dAccess)
        self.pushButton2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))        
        self.lineEdit = QtGui.QLineEdit(dAccess)
        self.lineEdit.setGeometry(QtCore.QRect(70, 30, 400, 32))
        self.lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(dAccess)
        QtCore.QMetaObject.connectSlotsByName(dAccess)

    def retranslateUi(self, dAccess):
        dAccess.setWindowTitle(_translate("dAccess", "Acceso para programadores", None))
        self.pushButton.setText(_translate("dAccess", "Acceder", None))
        self.pushButton.setShortcut(_translate("dAccess", "Return", None))
        self.pushButton2.setShortcut(_translate("dAccess", "Esc", None))

