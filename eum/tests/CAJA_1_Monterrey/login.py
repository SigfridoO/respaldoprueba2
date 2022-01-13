from PyQt4 import QtCore, QtGui
from conexion import Conexion

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

class loginDialog(object):
    def __init__(self, Dialog):
       
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(545, 330)
        Dialog.setMinimumSize(QtCore.QSize(545, 330))
        Dialog.setMaximumSize(QtCore.QSize(545, 330))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/logotipo1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(208, 219, 229);"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(179, 30, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Return To Sender"))
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 71, 71))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("img/luser.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 70, 71, 71))
        self.label_3.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/lkey.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.keyPressed = QtCore.pyqtSignal()
        self.lineEdit.setGeometry(QtCore.QRect(140, 90, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Chapaza"))
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 180, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.buton = QtGui.QPushButton(Dialog)
        self.buton.setGeometry(QtCore.QRect(340, 250, 121, 41))
        #self.buton.clicked.connect()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Robot"))
        font.setPointSize(18)
        self.buton.setFont(font)
        self.buton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buton.setStyleSheet(_fromUtf8("QPushButton{\n"
		"   border-top: 1px solid #96d1f8;\n"
		"   background: #65a9d7;\n"
		"   padding: 9px 18px;\n"
		"   border-radius: 9px;\n"
		"   color: white;\n"
		"   font-size: 16px;\n"
		"   font-family: Robot, serif;\n"
		"   /*text-decoration: none;*/\n"
		"   vertical-align: middle;\n"
		"\n"
		"}\n"
		"  \n"
		"QPushButton:hover {\n"
		"   border-top-color: #28597a;\n"
		"   background: #28597a;\n"
		"   color: #ccc;\n"
		"   }"))
        self.buton.setObjectName(_fromUtf8("buton"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(463, 8, 81, 81))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("img/logotipobig2.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.elabel = QtGui.QLabel(Dialog)
        self.elabel.setGeometry(QtCore.QRect(60, 250, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Chapaza"))
        font.setPointSize(14)
        self.elabel.setFont(font)
        self.elabel.setText(_fromUtf8(""))
        self.elabel.setObjectName(_fromUtf8("elabel"))
        self.elabel.setStyleSheet(_fromUtf8("color: red;"))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)        
	""""
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(545, 330)
        Dialog.setMinimumSize(QtCore.QSize(545, 330))
        Dialog.setMaximumSize(QtCore.QSize(545, 330))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/logotipo1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(208, 219, 229);"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(179, 30, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Return To Sender"))
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 71, 71))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("img/luser.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 70, 71, 71))
        self.label_3.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("img/lkey.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 90, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Chapaza"))
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 180, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.buton = QtGui.QPushButton(Dialog)
        self.buton.setGeometry(QtCore.QRect(340, 250, 121, 41))
        self.buton.clicked.connect(self.vLogin)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Robot"))
        font.setPointSize(18)
        self.buton.setFont(font)
        self.buton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buton.setStyleSheet(_fromUtf8("QPushButton{\n"
		"   border-top: 1px solid #96d1f8;\n"
		"   background: #65a9d7;\n"
		"   padding: 9px 18px;\n"
		"   border-radius: 9px;\n"
		"   color: white;\n"
		"   font-size: 16px;\n"
		"   font-family: Robot, serif;\n"
		"   /*text-decoration: none;*/\n"
		"   vertical-align: middle;\n"
		"\n"
		"}\n"
		"  \n"
		"QPushButton:hover {\n"
		"   border-top-color: #28597a;\n"
		"   background: #28597a;\n"
		"   color: #ccc;\n"
		"   }"))
        self.buton.setObjectName(_fromUtf8("buton"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(463, 8, 81, 81))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("img/logotipobig2.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.elabel = QtGui.QLabel(Dialog)
        self.elabel.setGeometry(QtCore.QRect(60, 250, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Chapaza"))
        font.setPointSize(14)
        self.elabel.setFont(font)
        self.elabel.setText(_fromUtf8(""))
        self.elabel.setObjectName(_fromUtf8("elabel"))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def vLogin(self):
		f = -1
		user = self.lineEdit.text()
		password = self.lineEdit_2.text()
		q = str("SELECT rol_usu FROM \"Usuario\" WHERE usu_usu = '"+user+"' AND pwd_usu = '"+password+"'")
		conexion = Conexion()
		try:
			f = conexion.doQuery(q)[0][0];
		except:
			print("El usuario no se encuentra en la base de datos")
		print(f)
		return f
		"""
	def keyPressEvent(self):
		super(loginDialog, self).keyPressEvent(event)
		self.keyPressed.emit()
	
	
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Estacionamientos Unicos de Mexico", None))
        self.label.setText(_translate("Dialog", "Inicio de Sesion", None))
        self.buton.setText(_translate("Dialog", "ACCEDER", None))
