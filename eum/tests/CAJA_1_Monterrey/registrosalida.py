#Controlador
import fechaUTC as fecha
import qr as q
#import cortes as corteCaja
import tarifas as calTar
import validacionesForm as vForm
import configuracionEXP as archivoConfiguracion
import leerConfiguracionFechaHora as confFH
import leerCamara as camara		#new
#Controlador de Python-Raspberry
import RPi.GPIO as GPIO
import time, os

#Modelo
from recurringTimer import RecurringTimer
from conexion import Conexion
from PyQt4 import QtCore, QtGui
from datetime import datetime

#Vista
from dLogin import dLogin
from dtarifa import dTarifa
from dcorteCaja import dcorteCaja
from dboletoPerdido import dBoletoPerdido
from dGestionUsuario import dGestionUsuario
from dAccess import dAccess

OUTPUT_TERMINAL=(archivoConfiguracion.getNumTer())
print OUTPUT_TERMINAL
SUPER_PASSWORD = "n0m3l0"		#PASSWORD PARA EL ACCESO A PROGRAMADORES
COSTO_BOLETO_PERDIDO=100		#SE OCUPA ESTA MACRO PARA LA PARTE DE COBRO POR TARIFA DE BOLETO PERDIDO
CLAVE_CAMBIAR_TARIFA_A_VOLUNTARIA=25342534

horaDeApagado=confFH.getHora()

PATH_LOGOS_1="/home/pi/Documents/CAJA_1_Monterrey/img/logotipo1.png"



GPIO.setmode(GPIO.BCM)			#CONTROLADOR DE GPIO


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

class Ui_Form(object):
	def __init__(self):
		#*Inicia Contenido Extra
		#self.gpiocleanup()
		self.tmins = 0
		self.thors = 0
		self.Total = 0
		self.treg = 1
		self.itarifa = 1
		self.FEDITABLE = True
		self.query = []
		self.Form = QtGui.QWidget()
		#**
		self.eflag = False
		self.mflag = False
		self.rflag = False
		self.cflag = False
		self.RolAdmin=False
		self.RolRoot=False
		#**
		#*Termina contenido extra
		self.Form.setObjectName(_fromUtf8("Form"))
		self.Form.resize(1366, 768)
		self.Form.setMinimumSize(QtCore.QSize(1366, 768))
		self.Form.setMaximumSize(QtCore.QSize(1366, 768))
		self.Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		self.Form.setGeometry(QtCore.QRect(160, 0, 241, 41))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(PATH_LOGOS_1)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.Form.setWindowIcon(icon)
		self.Form.setStyleSheet(_fromUtf8(""))
		self.label = QtGui.QLabel(self.Form)
		self.label.setGeometry(QtCore.QRect(230, 108, 181, 411))
		
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Roboto"))
		font.setPointSize(12)
		font.setBold(False)
		font.setWeight(50)
		self.label.setFont(font)
		self.label.setObjectName(_fromUtf8("label"))
		
		#LabelS de CAMARA
		self.label_camara_back = QtGui.QLabel(self.Form)
		self.label_camara_back.setGeometry(QtCore.QRect(749, 117, 300, 181))
		self.label_camara_back.lower()
		self.label_camara_back.setStyleSheet(_fromUtf8("background-color: rgb(211, 211, 211);\n border-radius: 10px;"))
		self.label_camara_back.setText(_fromUtf8(""))
		self.label_camara_back.setObjectName(_fromUtf8("label_camara_back"))
		#	label de titulo
		self.label_camara = QtGui.QLabel(self.Form)
		self.label_camara.setGeometry(QtCore.QRect(749, 117, 461, 25))
		font.setFamily(_fromUtf8("Roboto"))
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(70)
		self.label_camara.setFont(font)
		self.label_camara.setObjectName(_fromUtf8("label_camara"))
		#	label de contenido
		self.label_camara_1 = QtGui.QLabel(self.Form)
		self.label_camara_1.setGeometry(QtCore.QRect(750, 150,290, 170))
		font.setFamily(_fromUtf8("Roboto"))
		font.setPointSize(12)
		font.setBold(False)
		font.setWeight(70)
		self.label_camara_1.setStyleSheet(_fromUtf8("background-color: rgb(0, 211, 211);\n border-radius: 10px;"))
		self.label_camara_1.setFont(font)
		self.label_camara_1.setObjectName(_fromUtf8("label_camara_1"))
		#FIN LABELS CAMARA
		#BOTON NUEVO CANCELAR
		
		#FIN BOTON CANCELAR
		self.pushButton = QtGui.QPushButton(self.Form)
		self.pushButton.setGeometry(QtCore.QRect(920, 570, 110, 42))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Roboto Condensed"))
		font.setPointSize(16)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(9)
		self.pushButton.setFont(font)
		self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
		self.pushButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
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
		self.pushButton.setFlat(True)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		self.pushButton_2 = QtGui.QPushButton(self.Form)
		self.pushButton_2.setGeometry(QtCore.QRect(230, 566, 110, 42))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Roboto Condensed"))
		font.setPointSize(16)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(9)
		self.pushButton_2.setFont(font)
		self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
		self.pushButton_2.setFlat(True)
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.pushButton_3 = QtGui.QPushButton(self.Form)
		self.pushButton_3.setGeometry(QtCore.QRect(400, 570, 171, 41))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Roboto Condensed"))
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.pushButton_3.setFont(font)
		self.pushButton_3.setStyleSheet(_fromUtf8(""))
		self.pushButton_3.setShortcut(_fromUtf8(""))
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
		self.label_12 = QtGui.QLabel(self.Form)
		self.label_12.setGeometry(QtCore.QRect(320, 40, 251, 61))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Return To Sender"))
		font.setPointSize(36)
		font.setBold(False)
		font.setWeight(50)
		self.label_12.setFont(font)
		self.label_12.setObjectName(_fromUtf8("label_12"))
		self.groupBox = QtGui.QGroupBox(self.Form)
		self.groupBox.setGeometry(QtCore.QRect(749,370, 271, 141))
		self.groupBox.setEnabled(False)
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Roboto"))
		self.groupBox.setFont(font)
		self.groupBox.setObjectName(_fromUtf8("groupBox"))
		self.comboBox = QtGui.QComboBox(self.groupBox)
		self.comboBox.setGeometry(QtCore.QRect(0, 40, 271, 28))
		self.comboBox.setObjectName(_fromUtf8("comboBox"))
		self.comboBox.addItem(_fromUtf8(""))
		self.comboBox.addItem(_fromUtf8(""))
		self.comboBox.addItem(_fromUtf8(""))
		self.comboBox.addItem(_fromUtf8(""))
		self.pushButton_4 = QtGui.QPushButton(self.groupBox)
		self.pushButton_4.setGeometry(QtCore.QRect(180, 110, 85, 27))
		self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
		self.txtInput = QtGui.QLineEdit(self.Form)
		self.txtInput.setEnabled(False)
		self.txtInput.setGeometry(QtCore.QRect(420, 298, 261, 32))
		self.txtInput.setObjectName(_fromUtf8("txtInput"))
		self.txtFolio = QtGui.QLineEdit(self.Form)
		self.txtFolio.setEnabled(False)
		self.txtFolio.setGeometry(QtCore.QRect(420, 259, 261, 32))
		self.txtFolio.setObjectName(_fromUtf8("txtFolio"))
		self.txtTarifa = QtGui.QLineEdit(self.Form)
		self.txtTarifa.setEnabled(False)
		self.txtTarifa.setGeometry(QtCore.QRect(420, 410, 261, 32))
		self.txtTarifa.setObjectName(_fromUtf8("txtTarifa"))
		self.txtHorain = QtGui.QLineEdit(self.Form)
		self.txtHorain.setEnabled(False)
		self.txtHorain.setGeometry(QtCore.QRect(420, 374, 261, 32))
		self.txtHorain.setObjectName(_fromUtf8("txtHorain"))
		self.txtFechin = QtGui.QLineEdit(self.Form)
		self.txtFechin.setEnabled(False)
		self.txtFechin.setGeometry(QtCore.QRect(420, 337, 261, 32))
		self.txtFechin.setObjectName(_fromUtf8("txtFechin"))
		self.labelTotal = QtGui.QLabel(self.Form)
		self.labelTotal.setGeometry(QtCore.QRect(420, 475, 231, 31))
		font = QtGui.QFont()
		font.setPointSize(25)
		font.setBold(True)
		font.setWeight(75)
		self.labelTotal.setFont(font)
		self.labelTotal.setText(_fromUtf8(""))
		self.labelTotal.setObjectName(_fromUtf8("labelTotal"))
		self.label_3 = QtGui.QLabel(self.Form)
		self.label_3.setGeometry(QtCore.QRect(749, 370, 291, 181))
		self.label_3.lower()
		self.label_3.setStyleSheet(_fromUtf8("background-color: rgb(211, 211, 211);\n"
		"border-radius: 10px;"))
		self.label_3.setText(_fromUtf8(""))
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.pushButton_5 = QtGui.QPushButton(self.Form)
		self.pushButton_5.setGeometry(QtCore.QRect(760, 320, 271, 41))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Roboto Condensed"))
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.pushButton_5.setFont(font)
		self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
		self.pushButton_7 = QtGui.QPushButton(self.Form)
		self.pushButton_7.setGeometry(QtCore.QRect(600, 570, 131, 41))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Roboto"))
		font.setPointSize(12)
		font.setBold(False)
		font.setWeight(50)
		self.pushButton_7.setFont(font)
		self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
		self.pushButton_6 = QtGui.QPushButton(self.Form)
		self.pushButton_6.setGeometry(QtCore.QRect(750, 570, 121, 41))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Roboto"))
		font.setPointSize(12)
		font.setBold(False)
		font.setWeight(50)
		self.pushButton_6.setFont(font)
		self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
		#PUSH BOTON DE APAGAR
		self.pushButton_8 = QtGui.QPushButton(self.Form)
		self.pushButton_8.setGeometry(QtCore.QRect(760, 20, 71, 41))
		self.pushButton_8.setFont(font)
		self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
		##FIN PUSH BOTON APAGAR		
		self.labelVendedor = QtGui.QLabel(self.Form)
		self.labelVendedor.setGeometry(QtCore.QRect(420, 113, 261, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.labelVendedor.setFont(font)
		self.labelVendedor.setText(_fromUtf8(""))
		self.labelVendedor.setObjectName(_fromUtf8("labelVendedor"))
		self.labelOutput = QtGui.QLabel(self.Form)
		self.labelOutput.setGeometry(QtCore.QRect(420, 153, 261, 37))
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.labelOutput.setFont(font)
		self.labelOutput.setText(_fromUtf8(""))
		self.labelOutput.setObjectName(_fromUtf8("labelOutput"))
		self.labelFechout = QtGui.QLabel(self.Form)
		self.labelFechout.setGeometry(QtCore.QRect(420, 190, 261, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.labelFechout.setFont(font)
		self.labelFechout.setText(_fromUtf8(""))
		self.labelFechout.setObjectName(_fromUtf8("labelFechout"))
		self.labelHoraout = QtGui.QLabel(self.Form)
		self.labelHoraout.setGeometry(QtCore.QRect(421, 222, 261, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.labelHoraout.setFont(font)
		self.labelHoraout.setText(_fromUtf8(""))
		self.labelHoraout.setObjectName(_fromUtf8("labelHoraout"))
		self.label_4 = QtGui.QLabel(self.Form)
		self.label_4.setGeometry(QtCore.QRect(221, 117, 461, 141))
		self.label_4.lower()
		self.label_4.setStyleSheet(_fromUtf8("background-color: rgb(211, 211, 211);\n"
		"border-radius: 10px;"))
		self.label_4.setText(_fromUtf8(""))
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.label_5 = QtGui.QLabel(self.Form)
		self.label_5.setGeometry(QtCore.QRect(50, 0, 121, 121))
		self.label_5.setText(_fromUtf8(""))
		self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(PATH_LOGOS_1)))
		self.label_5.setScaledContents(True)
		self.label_5.setObjectName(_fromUtf8("label_5"))

		self.retranslateUi(self.Form)
		QtCore.QMetaObject.connectSlotsByName(self.Form)
		self.Form.setTabOrder(self.txtFolio, self.txtInput)
		self.Form.setTabOrder(self.txtInput, self.txtFechin)
		self.Form.setTabOrder(self.txtFechin, self.txtHorain)
		self.Form.setTabOrder(self.txtHorain, self.txtTarifa)
		self.Form.setTabOrder(self.txtTarifa, self.comboBox)
		self.Form.setTabOrder(self.comboBox, self.pushButton_4)
		self.Form.setTabOrder(self.pushButton_4, self.pushButton_5)
		self.Form.setTabOrder(self.pushButton_5, self.pushButton_6)
		self.Form.setTabOrder(self.pushButton_6, self.pushButton_7)
		self.Form.setTabOrder(self.pushButton_7, self.pushButton)
		self.Form.setTabOrder(self.pushButton, self.pushButton_3)
		self.Form.setTabOrder(self.pushButton_3, self.pushButton_2)
		
		#Funcionalidades
		self.login = QtGui.QDialog(self.Form)
		self.l = dLogin(self.login)
		self.l.pushButton.clicked.connect(self.vLogin)
		self.l.pushButton2.clicked.connect(self.secretAccess)
		self.pushButton_2.clicked.connect(self.Logout)
		self.pushButton_3.clicked.connect(self.lostTicket)
		self.pushButton_4.clicked.connect(self.btnAdmin)
		self.pushButton_5.clicked.connect(self.leerBoleto)
		self.pushButton_6.clicked.connect(self.abrirBarrera)
		self.pushButton_7.clicked.connect(self.cerrarBarrera)
		self.pushButton_8.clicked.connect(self.apagar)
		self.pushButton.clicked.connect(self.registroVenta)
		self.login.show()
		#Final
		self.daccess= QtGui.QDialog(self.Form)
		self.access1 = dAccess(self.daccess)
		self.access1.pushButton.clicked.connect(self.vAccess)
		self.access1.pushButton2.clicked.connect(self.Logout)
		
		self.currentTabIndex = 0
		self.registroUsuario = QtGui.QDialog(self.Form)
		self.regUsu = dGestionUsuario(self.registroUsuario)
		self.regUsu.pushButton.clicked.connect(self.btnRegUsu)
		self.regUsu.pushButton_2.clicked.connect(self.cancelRegUsu)
		self.regUsu.pushButton_6.clicked.connect(self.cleanUsu)
		self.regUsu.tabWidget.currentChanged.connect(self.tabClicked, self.regUsu.tabWidget.currentIndex())
		self.txtTarifa.setText(self.getTarifa(self.itarifa))
		self.labelTotal.setText("$"+str(self.Total))
		#SE DESPLIEGA OCULTA LA CAMARA PARA LA LECT5URA DE LOS BOLETOS
		
	pass
	
	def cleanUsu(self):
		print self.currentTabIndex
		if self.currentTabIndex==0:
			self.regUsu.txtNombre.setText("")
			self.regUsu.txtApp.setText("")
			self.regUsu.txtApm.setText("")
			self.regUsu.txtUsuario.setText("")
			self.regUsu.txtPassword.setText("")
			self.regUsu.cbxHorario.setCurrentIndex(0)
			self.regUsu.cbxRol.setCurrentIndex(0)
			self.regUsu.txtPuesto.setText("")
			
		elif self.currentTabIndex==1:
			self.regUsu.txtCNombre.setText("")
			self.regUsu.txtCApp.setText("")
			self.regUsu.txtCApm.setText("")
			self.regUsu.txtCUsuario.setText("")
			self.regUsu.cbxCHorario.setCurrentIndex(0)
			self.regUsu.cbxCRol.setCurrentIndex(0)
			self.regUsu.txtCPuesto.setText("")
		
		elif self.currentTabIndex==2:
			self.regUsu.txtMNombre.setText("")
			self.regUsu.txtMApp.setText("")
			self.regUsu.txtMApm.setText("")
			self.regUsu.txtMUsuario.setText("")
			self.regUsu.txtMPassword.setText("")
			self.regUsu.cbxMHorario.setCurrentIndex(0)
			self.regUsu.cbxMRol.setCurrentIndex(0)
			self.regUsu.txtMPuesto.setText("")
			self.regUsu.txtMNombre.setEnabled(False)
			self.regUsu.txtMApp.setEnabled(False)
			self.regUsu.txtMApm.setEnabled(False)
			self.regUsu.txtMPassword.setEnabled(False)
			self.regUsu.txtMPuesto.setEnabled(False)
			self.regUsu.cbxMRol.setEnabled(False)
			self.regUsu.cbxMHorario.setEnabled(False)
			self.regUsu.txtMUsuario.setEnabled(True)
			self.mflag = False
			self.regUsu.pushButton.setText("Buscar")
			
		
		elif self.currentTabIndex==3:
			self.regUsu.txtENombre.setText("")
			self.regUsu.txtEApp.setText("")
			self.regUsu.txtEApm.setText("")
			self.regUsu.txtEUsuario.setText("")
			self.regUsu.cbxEHorario.setCurrentIndex(0)
			self.regUsu.cbxERol.setCurrentIndex(0)
			self.regUsu.txtEPuesto.setText("")
	pass
	
	def tabClicked(self, opt):
		if opt==0:
			self.currentTabIndex = 0
			self.regUsu.pushButton.setText("Agregar")
			self.cleanUsu()

		elif opt==1:
			self.currentTabIndex = 1
			self.cleanUsu()
		elif opt==2:
			self.cleanUsu()
			self.currentTabIndex = 2
			if(self.mflag == False):
				self.regUsu.pushButton.setText("Buscar")
		elif opt==3:
			self.cleanUsu()
			self.currentTabIndex = 3
			if(self.eflag == False):
				self.regUsu.pushButton.setText("Buscar")
	pass
	
	def secretAccess(self):
		print("Hola")
		self.login.setHidden(True)
		self.daccess.show()
	pass

	def vAccess(self):
		if(self.access1.lineEdit.text()==SUPER_PASSWORD):
			print("acceso concedido")
			exit()
	pass
	
	def updateTime(self):
		self.labelFechout.setText(""+str(fecha.fechaConFormato()))
		self.labelHoraout.setText(""+str(fecha.tiempoConFormato()))
		H=time.strftime("%H:%M:%S")
		self.apagarExp(H)
	pass
	#APAGAR EQUIPO POR HORA
	def apagarExp(self,H):
		if horaDeApagado==H:
			print "Se apaga el sistema" 
			os.system("sudo shutdown 0")
	#FIN APAGAR EQUIPO POR HORA
	
	def apagar(self):
		print "Se apaga el sistema"
		os.system("sudo shutdown 0")
	
	def statusCamara(self):
		#import leerCamara as camara
		contenido=[]
		contenido=camara.getTodo()
		print "Status camara ..."+str(contenido) 
		print len(contenido)
		if len(contenido)==0 :
			print "Esperando boleto ..."
			self.label_camara_1.setText("Esperando Boleto..." )
		elif contenido[0]=="-1\n" :
			self.label_camara_1.setText(contenido[1]+"\n"+contenido[2]+"\n"+contenido[3])
		elif contenido[0]!="-1\n" and len(contenido)>1  and len(self.txtHorain.text())==0:
			self.label_camara_1.setText("Leyendo boleto...\n Presionar Aceptar para registrar Venta" )
			camara.respaldaArchivoTicket()
			camara.borrarArchivo()
			self.vaciarDatosInterfaz()
		else:
			print "Esperando a registrar venta "
		QtCore.QTimer.singleShot(1000, self.statusCamara)
	
		#Se pueden segrar algunas funciones para el calculo de los minutos
	def vaciarDatosInterfaz(self):
		self.pushButton_3.setEnabled(False)		#Deshabilitamos el boton de boleto perdido para que forzosamente cobren lo que se leyo
		self.pushButton_2.setEnabled(False)		#Boton de cancelar
		self.pushButton_6.setEnabled(False)		#Boton de Abrir barrera
		self.pushButton.setEnabled(True)		#Aceptar
		
		readQR = camara.getArreglo()
		################LOGICA DE QR
		print "**********************"
		print readQR[0]
		print len(readQR[0])
		print type(readQR[0])
		if readQR[0]=='Banco\n':
			print "Bancooooo"
			self.txtFolio.setText(readQR[0])
			self.txtInput.setText("BOLETO")
			self.txtFechin.setText("LOCATARIO")
			self.txtHorain.setText(readQR[1])
			try:
				self.Total=0.0
				self.labelTotal.setText("$"+str(self.Total))
				self.pushButton_5.setEnabled(True)		#LEER BOLETO
				self.pushButton.setEnabled(True)		#Aceptar
				self.treg=2.1
			except:
				print("Interfaz vacia")
		elif readQR[0]=='Suburbia\n':
			print "Suburbiiaaa"	
			self.txtFolio.setText(readQR[0])
			self.txtInput.setText("BOLETO")
			self.txtFechin.setText("LOCATARIO")
			self.txtHorain.setText(readQR[1])
			try:
				self.Total=0.0
				self.labelTotal.setText("$"+str(self.Total))
				self.pushButton_5.setEnabled(True)		#LEER BOLETO
				self.pushButton.setEnabled(True)		#Aceptar
				self.treg=2.1
			except:
				print("Interfaz vacia")
		else:
			print "BOLETO NORMAL"
			self.txtFolio.setText(readQR[0])
			self.txtInput.setText(readQR[1])
			self.txtFechin.setText(readQR[2])
			self.txtHorain.setText(readQR[3])
			try:
				print("Calcular")
				self.minsin = int(self.labelHoraout.text()[3:5])
				h=int(readQR[3][0:2])
				m= int(readQR[3][3:5])
				s= int(readQR[3][6:8])
				horaIn= str(h)
				minutosIn=str(m)
				self.tmins=self.calcularMinutosParaLeerBoletos(horaIn, minutosIn)
				self.labelTotal.setText("$"+str(self.Total))
				self.pushButton_5.setEnabled(True)		#LEER BOLETO
				self.pushButton.setEnabled(True)		#Aceptar
				
			except:
				print("Interfaz vacia")
		print "**********************"
	pass

	
	def showDestar(self):
		index = self.dTar.comboBox.currentIndex()
		q = "SELECT pol_tar FROM \"CTarifas\" where id_tar = "+str(index+1)+""
		conexion = Conexion()
		q = conexion.doQuery(q)
		self.dTar.txtDestar.clear()
		self.dTar.txtDestar.insertPlainText(str(q[0][0]))
	
	def changeTarifa(self):
		self.itarifa = self.dTar.comboBox.currentIndex() + 1
		self.txtTarifa.setText(self.getTarifa(self.itarifa))
		#self.Total = calTar.calcularMonto(self.tmins, self.itarifa, CLAVE_CAMBIAR_TARIFA_A_VOLUNTARIA)
		self.treg=1
		self.labelTotal.setText("$"+str(self.Total))
		self.dialogoTarifa.setHidden(True)
	pass
	
	def closeDialog(self):
		self.dialogoTarifa.setHidden(True)
	pass
	
	def btnAdmin(self):
		index = self.comboBox.currentIndex()
		if(index == 0):
			self.regUsu.pushButton.setText("Agregar")
			self.registroUsuario.show()
		elif(index == 1):
			self.corteCaja = QtGui.QDialog(self.Form)
			self.corCaj = dcorteCaja(self.corteCaja)
			self.corCaj.lineEdit.setText(OUTPUT_TERMINAL)
			self.corCaj.dateEdit.date = fecha.fechaConFormato()
			self.corCaj.pushButton.clicked.connect(self.btnCorteCaja)
			self.corCaj.pushButton_2.clicked.connect(self.cancelCorCaj)			
			self.corteCaja.show()
					
		elif(index==2):
			self.dialogoTarifa = QtGui.QDialog(self.Form)
			self.dTar = dTarifa(self.dialogoTarifa)
			self.dTar.comboBox.activated.connect(self.showDestar)
			self.dTar.pushButton_2.clicked.connect(self.closeDialog)
			self.dTar.pushButton.clicked.connect(self.changeTarifa)
			self.showDestar()
			self.dialogoTarifa.show()
			
		elif(index==3):
			if(self.FEDITABLE==True):
				self.treg = 2
				self.txtFechin.setEnabled(True)
				self.txtFolio.setEnabled(True)
				self.txtInput.setEnabled(True)
				self.txtHorain.setEnabled(True)
				self.pushButton_5.setEnabled(False)
				self.comboBox.setItemText(3,"Registro Automatico")
				self.FEDITABLE = False
			else:
				self.treg = 1
				self.txtFechin.setEnabled(False)
				self.txtFolio.setEnabled(False)
				self.txtInput.setEnabled(False)
				self.txtHorain.setEnabled(False)
				self.pushButton_5.setEnabled(True)
				self.comboBox.setItemText(3,"Registro Manual")
				self.FEDITABLE = True
		
	pass
	
	#Comienza RegistroUsuario
	def btnRegUsu(self):
		print self.currentTabIndex
		conexion = Conexion()
		if self.RolRoot==True:
			print "Soy Root"
			if self.currentTabIndex==0:
				nom = self.regUsu.txtNombre.text()
				app= self.regUsu.txtApp.text()
				apm= self.regUsu.txtApm.text()
				usu= self.regUsu.txtUsuario.text()
				pwd= self.regUsu.txtPassword.text()
				hor= self.regUsu.cbxHorario.currentIndex() + 1
				rol = self.regUsu.cbxRol.currentIndex() + 1
				pst = self.regUsu.txtPuesto.text()
				#Query de validacion
				q = "SELECT id_usu   FROM \"Usuario\" WHERE usu_usu='"+usu+"' ;"
				print q
				f = conexion.doQuery(q)
				print len(f)
				if len(f)<=0 and nom!='' and app!='':
					#Logica para query de registrar usuariio
					q = "INSERT INTO \"Usuario\" (nom_usu, app_usu, apm_usu, usu_usu, rol_usu, pwd_usu, id_hor, pst_usu) values ('"+nom+"','"+app+"','"+apm+"','"+usu+"', "+str(rol)+", '"+pwd+"', "+str(hor)+", '"+pst+"');"
					print(q)
					f = conexion.execQuery(q)
					if(f<0):
						print("Error: El registro del usuario perdido no ha sido guardado")
					else:
						#self.registroUsuario.setHidden(True)
						self.cleanUsu()
				else:
					print("Error:USUARIO EXISTENTE o faltan datos")
					print "	EL Id usu existente es:"+str(f)
					vForm.ventana("***********Error al registrar*********","Error:USUARIO EXISTENTE o faltan datos")
			elif self.currentTabIndex==1:
				usu = self.regUsu.txtCUsuario.text()
				q = "SELECT * FROM \"Usuario\" WHERE usu_usu = '"+usu+"';"
				f = conexion.doQuery(q)
				if(f<0):
					print("Error: El usuario no se encuentra en el registro")
				else:
					self.regUsu.txtCNombre.setText(str(f[0][1]))
					self.regUsu.txtCApp.setText(str(f[0][2]))
					self.regUsu.txtCApm.setText(str(f[0][3]))
					self.regUsu.txtCPuesto.setText(str(f[0][8]))
					self.regUsu.cbxCRol.setCurrentIndex(int(f[0][5])-1)
					self.regUsu.cbxCHorario.setCurrentIndex(int(f[0][7])-1)
			elif self.currentTabIndex==2:
				if self.mflag == False:
					self.regUsu.pushButton.setText("Modificar")
					usu = self.regUsu.txtMUsuario.text()
					q = "SELECT * FROM \"Usuario\" WHERE usu_usu = '"+usu+"';"
					f = conexion.doQuery(q)
					if(f<0):
						print("Error: El usuario no se encuentra en el registro")
					else:
						print f
						self.regUsu.txtMNombre.setText(str(f[0][1]))
						self.regUsu.txtMApp.setText(str(f[0][2]))
						self.regUsu.txtMApm.setText(str(f[0][3]))
						self.regUsu.txtMPassword.setText(str(f[0][6]))
						self.regUsu.txtMPuesto.setText(str(f[0][8]))
						self.regUsu.cbxMRol.setCurrentIndex(int(f[0][5])-1)
						self.regUsu.cbxMHorario.setCurrentIndex(int(f[0][7])-1)
						self.regUsu.txtMNombre.setEnabled(True)
						self.regUsu.txtMApp.setEnabled(True)
						self.regUsu.txtMApm.setEnabled(True)
						self.regUsu.txtMPassword.setEnabled(True)
						self.regUsu.txtMPuesto.setEnabled(True)
						self.regUsu.cbxMRol.setEnabled(True)
						self.regUsu.cbxMHorario.setEnabled(True)
						self.regUsu.txtMUsuario.setEnabled(False)
					self.mflag=True
				else:
					nom = self.regUsu.txtMNombre.text()
					app= self.regUsu.txtMApp.text()
					apm= self.regUsu.txtMApm.text()
					usu= self.regUsu.txtMUsuario.text()
					pwd= self.regUsu.txtMPassword.text()
					hor= self.regUsu.cbxMHorario.currentIndex() + 1
					rol = self.regUsu.cbxMRol.currentIndex() + 1
					pst = self.regUsu.txtMPuesto.text()
					#q = "UPDATE \"Usuario\" SET (nom_usu = '"+nom+"', app_usu = '"+app+"', apm_usu = '"+apm+"', usu_usu = '"+usu+"', rol_usu = "+str(rol)+", pwd_usu = '"+pwd+"', id_hor = "+str(hor)+", pst_usu = '"+pst+"') WHERE usu_usu = '"+usu+"';"
					q = "UPDATE \"Usuario\" SET nom_usu = '"+nom+"', app_usu = '"+app+"', apm_usu = '"+apm+"', rol_usu = "+str(rol)+", pwd_usu = '"+pwd+"', id_hor = "+str(hor)+", pst_usu = '"+pst+"' WHERE usu_usu = '"+usu+"';"
					print(q)
					f = conexion.execQuery(q)
					if(f<0):
						print("Error: Los datos del usuario no han sido actualizados")
					self.regUsu.pushButton.setText("Buscar")
					self.mflag=False
			elif self.currentTabIndex==3:
				if self.eflag == False:
					self.eflag = True
					self.regUsu.pushButton.setText("Eliminar")
					usu = self.regUsu.txtEUsuario.text()
					q = "SELECT * FROM \"Usuario\" WHERE usu_usu = '"+usu+"';"
					f = conexion.doQuery(q)
					if(f<0):
						print("Error: El usuario no se encuentra en el registro")
					else:
						self.regUsu.txtENombre.setText(str(f[0][1]))
						self.regUsu.txtEApp.setText(str(f[0][2]))
						self.regUsu.txtEApm.setText(str(f[0][3]))
						self.regUsu.txtEPuesto.setText(str(f[0][8]))
						self.regUsu.cbxERol.setCurrentIndex(int(f[0][5])-1)
						self.regUsu.cbxEHorario.setCurrentIndex(int(f[0][7])-1)
				else:
					usu = self.regUsu.txtEUsuario.text()
					self.regUsu.pushButton.setText("Buscar")
					self.eflag = False
					q = "DELETE FROM \"Usuario\" WHERE usu_usu = '"+usu+"';"
					f = conexion.execQuery(q)
					if(f<0):
						print("Error: Los datos del usuario no fueron eliminados")
					else:
						self.cleanUsu()
		if self.RolRoot==False:
			print "Soy Administrador"		#*********************************************************************ADMINISTRADOR
			if self.currentTabIndex==0:
				nom = self.regUsu.txtNombre.text()
				app= self.regUsu.txtApp.text()
				apm= self.regUsu.txtApm.text()
				usu= self.regUsu.txtUsuario.text()
				pwd= self.regUsu.txtPassword.text()
				hor= self.regUsu.cbxHorario.currentIndex() + 1
				rol = 2
				pst = self.regUsu.txtPuesto.text()
				#Query de validacion
				q = "SELECT id_usu   FROM \"Usuario\" WHERE usu_usu='"+usu+"' ;"
				f = conexion.doQuery(q)
				if len(f)<=0 and nom!='' and app!='':
					#Logica para query de registrar usuariio
					q = "INSERT INTO \"Usuario\" (nom_usu, app_usu, apm_usu, usu_usu, rol_usu, pwd_usu, id_hor, pst_usu) values ('"+nom+"','"+app+"','"+apm+"','"+usu+"', "+str(rol)+", '"+pwd+"', "+str(hor)+", '"+pst+"');"
					print(q)
					f = conexion.execQuery(q)
					if(f<0):
						print("Error: El registro del usuario perdido no ha sido guardado")
					else:
						#self.registroUsuario.setHidden(True)
						self.cleanUsu()
				else:
					print("Error:USUARIO EXISTENTE o faltan datos")
					print "	EL Id usu existente es:"+str(f)
					vForm.ventana("***********Error al registrar*********","Error:USUARIO EXISTENTE o faltan datos")
			#TERMINA AGREGAR USUARIO
			elif self.currentTabIndex==1:
				usu = self.regUsu.txtCUsuario.text()
				q = "SELECT * FROM \"Usuario\" WHERE usu_usu = '"+usu+"';"
				f = conexion.doQuery(q)
				if(f<0):
					print("Error: El usuario no se encuentra en el registro")
				else:
					self.regUsu.txtCNombre.setText(str(f[0][1]))
					self.regUsu.txtCApp.setText(str(f[0][2]))
					self.regUsu.txtCApm.setText(str(f[0][3]))
					self.regUsu.txtCPuesto.setText(str(f[0][8]))
					self.regUsu.cbxCRol.setCurrentIndex(int(f[0][5])-1)
					self.regUsu.cbxCHorario.setCurrentIndex(int(f[0][7])-1)
			#TERMINA BUSCAR USUARIO
			elif self.currentTabIndex==2:
				if self.mflag == False:
					self.regUsu.pushButton.setText("Modificar")
					usu = self.regUsu.txtMUsuario.text()
					q = "SELECT * FROM \"Usuario\" WHERE usu_usu = '"+usu+"'  and rol_usu!='1' and rol_usu!='3' ;"
					f = conexion.doQuery(q)
					if(f<0):
						print("Error: El usuario no se encuentra en el registro")
					else:
						print f
						self.regUsu.txtMNombre.setText(str(f[0][1]))
						self.regUsu.txtMApp.setText(str(f[0][2]))
						self.regUsu.txtMApm.setText(str(f[0][3]))
						self.regUsu.txtMPassword.setText(str(f[0][6]))
						self.regUsu.txtMPuesto.setText(str(f[0][8]))
						self.regUsu.cbxMRol.setCurrentIndex(int(f[0][5])-1)
						self.regUsu.cbxMHorario.setCurrentIndex(int(f[0][7])-1)
						self.regUsu.txtMNombre.setEnabled(False)
						self.regUsu.txtMApp.setEnabled(False)
						self.regUsu.txtMApm.setEnabled(False)
						self.regUsu.txtMPassword.setEnabled(True)		#SOLO HABILITAMOS EL CAMBIAR PASSWORD
						self.regUsu.txtMPuesto.setEnabled(False)
						self.regUsu.cbxMRol.setEnabled(False)
						self.regUsu.cbxMHorario.setEnabled(False)
						self.regUsu.txtMUsuario.setEnabled(False)
					self.mflag=True
				else:
					nom = self.regUsu.txtMNombre.text()
					app= self.regUsu.txtMApp.text()
					apm= self.regUsu.txtMApm.text()
					usu= self.regUsu.txtMUsuario.text()
					pwd= self.regUsu.txtMPassword.text()
					hor= self.regUsu.cbxMHorario.currentIndex() + 1
					rol = self.regUsu.cbxMRol.currentIndex() + 1
					pst = self.regUsu.txtMPuesto.text()
					#q = "UPDATE \"Usuario\" SET (nom_usu = '"+nom+"', app_usu = '"+app+"', apm_usu = '"+apm+"', usu_usu = '"+usu+"', rol_usu = "+str(rol)+", pwd_usu = '"+pwd+"', id_hor = "+str(hor)+", pst_usu = '"+pst+"') WHERE usu_usu = '"+usu+"';"
					q = "UPDATE \"Usuario\" SET nom_usu = '"+nom+"', app_usu = '"+app+"', apm_usu = '"+apm+"', rol_usu = "+str(rol)+", pwd_usu = '"+pwd+"', id_hor = "+str(hor)+", pst_usu = '"+pst+"' WHERE usu_usu = '"+usu+"' and rol_usu!='1' ;"
					print(q)
					f = conexion.execQuery(q)
					if(f<0):
						print("Error: Los datos del usuario no han sido actualizados")
					self.regUsu.pushButton.setText("Buscar")
					self.cleanUsu()
					self.mflag=False
			elif self.currentTabIndex==3:
				vForm.ventana("***********No Puedes eliminar*********","Error: solo el gerente  puede eliminar")
	pass
	
	def cancelRegUsu(self):
		self.registroUsuario.setHidden(True)
	pass
	#Termina RegistroUsuario
	
	#Comienza corteCaja
	def btnCorteCaja(self):
		index = self.corCaj.comboBox.currentIndex()
		fechInicio = self.corCaj.dateEdit.text()
		fechFin = self.corCaj.dateEdit_2.text()
		corteCaja.elijeCorte((index+1), fechInicio, fechFin, OUTPUT_TERMINAL, self.query[0][3])
		self.corteCaja.setHidden(True)		
	pass
	
	def cancelCorCaj(self):
		self.corteCaja.setHidden(True)
	pass
	#Termina corteCaja

	
	#Verificar la forma de obtener el ultimo registro
	def lostTicket(self):
		self.lt = QtGui.QDialog(self.Form)
		self.dlt = dBoletoPerdido(self.lt)
		self.dlt.labelFechout.setText(self.labelFechout.text())
		self.dlt.labelHoraout.setText(self.labelHoraout.text())
		#Cuando esto deje de ser local dejara de funcionar
		q = "SELECT MAX(id_bol) FROM \"Boleto\";"
		conexion = Conexion()
		q = conexion.doQuery(q)
		self.dlt.labelTicket.setText(str(q[0][0]+1))
		self.Total = (calTar.calcularMonto(0,3,0))
		self.dlt.labelTotal.setText("$"+str(calTar.calcularMonto(0,3,0)))
		self.dlt.pushButton.clicked.connect(self.botonregLostTicket)
		self.dlt.pushButton_2.clicked.connect(self.cancelLt)
		self.lt.show()
	pass
	
	def botonregLostTicket(self):
		self.treg=3
		self.regLostTicket()
	#Sugerido cambiar los nombres de los campos de boleto perdido
	def regLostTicket(self):
		marca = self.dlt.txtMarca.text()
		placa= self.dlt.txtPlacas.text()
		modelo= self.dlt.txtModelo.text()
		licencia= self.dlt.txtLicencia.text()
		nombre= self.dlt.txtNombre.text()
		telefono= self.dlt.txtTelefono.text()
		vFlag = vForm.validarBolPer(marca,placa,modelo,licencia,nombre,telefono)
		if vFlag != True:
			self.registroVenta()
			q = "INSERT INTO \"BoletoPerdido\" (mar_car_bol_per, pla_bol_per, mod_bol_per, lic_num_bol_per, nom_usu_bol_per, tel_usu_bol_per, id_bol) values ('"+marca+"','"+placa+"','"+modelo+"','"+licencia+"','"+nombre+"', '"+telefono+"', "+str(int(self.dlt.labelTicket.text()))+");"
			print(q)
			conexion = Conexion()
			f = conexion.execQuery(q)
			if(f<0):
				print("Error: El registro del boleto perdido no ha sido guardado")
			else:
				self.limparDespuesDeCancelarBoletoPerdido()
				self.lt.setHidden(True)
	pass
	
	def cancelLt(self):
		print "BOTON CANCELAR"
		self.clearScreen()
		self.limparDespuesDeCancelarBoletoPerdido()
		self.lt.setHidden(True)
		
	pass

	def limparDespuesDeCancelarBoletoPerdido(self):
		marca = self.dlt.txtMarca.setText("")
		placa= self.dlt.txtPlacas.setText("")
		modelo= self.dlt.txtModelo.setText("")
		licencia= self.dlt.txtLicencia.setText("")
		nombre= self.dlt.txtNombre.setText("")
		telefono= self.dlt.txtTelefono.setText("")
		#Limpiamos ventana de registro
		self.treg = 1
		self.labelTotal.setText("$"+str(self.Total))
	
	def registroVenta(self):
		folio = self.txtFolio.text()
		inputTerminal = self.txtInput.text()
		outputTerminal = self.labelOutput.text()
		dateIn = self.txtFechin.text()
		dateOut = self.labelFechout.text()
		horIn = self.txtHorain.text()
		horOut = self.labelHoraout.text()
		idUsu = self.query[0][3]
		idTar = self.itarifa
		tipReg = self.treg
		#REGISTRO DE BOLETOS SIN SELLO / CON SELLO (SUBURBIA O BANCO)
		if tipReg==1 or tipReg==4 or tipReg==5 or tipReg==6 or tipReg==2.1 :					##BOTON DE ACEPTAR CON REGISTRO AUTOMATICO
			totBol = self.Total
			if tipReg==4 : #REGISTRO DE BOLETOS DE BANCO
				idTar = 4
			if tipReg==5 :#REGISTRO DE BOLETOS DE SUBUIRBIA
				idTar = 5
			if tipReg==6 :#REGISTRO DE BOLETOS DE TAXI
				idTar = 6
			if tipReg==2.1 :#REGISTRO DE BOLETOS DE SUBUIRBIA
				idTar = 2
				tipReg=1
				folio ="674715"
				inputTerminal = ""
				dateIn = "01/01/2000"
				horIn = "00:00:00"
			print "CHECATE LA TARIFA "+str(idTar)
			vFlag = vForm.registroSalida(folio, inputTerminal, dateIn, horIn, idTar)
			#VALIDACION DE BOLETO
			q = "SELECT id_bol FROM \"Boleto\" WHERE fol_bol='"+folio+"' and in_fec_bol='"+dateIn+"' and in_ter_bol='"+inputTerminal+"' and in_hor_bol='"+horIn+"';"
			conexion = Conexion()
			registros = conexion.doQuery(q)
			if len(registros)!=0:
				vForm.ventana("Error de Registro","BOLETO YA REGISTRADO> \n"+str(registros))
			else:#FIN DE VALIDACION DE BOLETO
				if vFlag != True:
					q = "INSERT INTO \"Boleto\" (fol_bol, in_ter_bol, out_ter_bol, in_fec_bol, out_fec_bol, id_tar_bol, id_usu_bol, tip_reg, tot_bol, in_hor_bol, out_hor_bol) values ('"+folio+"','"+inputTerminal+"','"+outputTerminal+"','"+dateIn+"','"+dateOut+"', "+str(idTar)+", "+str(idUsu)+", "+str(tipReg)+", "+str(totBol)+", '"+horIn+"', '"+horOut+"');"
					conexion = Conexion()
					f = conexion.execQuery(q)
					if(f<0):
						print("Error: El registro no ha sido guardado")
					else:
						self.pushButton_5.setEnabled(True)		#LEER BOLETO
						self.clearScreen()
				else:
					vForm.ventana("Error de Registro","Verifica los campos incorrectos")
				#RESTABLECEMOS LA TARIFA
			self.treg=1
		if tipReg==2:	#BOTON DE ACEPTAR CON REGISTRO MANUAL
			idTar = 7
			self.calcularMinutos()
			totBol = self.Total
			totBol = totBol[0]
			q = "INSERT INTO \"Boleto\" (fol_bol, in_ter_bol, out_ter_bol, in_fec_bol, out_fec_bol, id_tar_bol, id_usu_bol, tip_reg, tot_bol, in_hor_bol, out_hor_bol) values ('"+folio+"','"+inputTerminal+"','"+outputTerminal+"','"+dateIn+"','"+dateOut+"', "+str(idTar)+", "+str(idUsu)+", "+str(tipReg)+", "+str(totBol)+", '"+horIn+"', '"+horOut+"');"
			conexion = Conexion()
			vFlag = vForm.registroSalida(folio, inputTerminal, dateIn, horIn, idTar)
			if vFlag != True:
				f = conexion.execQuery(q)
				if(f<0):
					print("Error: El registro no ha sido guardado")
				else:
					vForm.ventana("REGISTRAR VENTA","TOTAL A COBRAR--------------------------------------------------\n-------------------------COBRA:$"+str(totBol)+"-------------------------\n--------------------------------------------------\n")
					self.pushButton_5.setEnabled(True)		#LEER BOLETO
					self.clearScreen()
			else:
				vForm.ventana("Error de Registro","Verifica los campos incorrectos")
		
		if tipReg==3:		#Boton de REGISTRO DE BOLETO PERDIDO
			print "Boleto Perido"
			folio="801370"
			idTar=3
			horIn = "00:00:00"
			dateIn ="01/01/2000"
			vFlag = vForm.registroSalida(folio, inputTerminal, dateIn, horIn, idTar)
			if vFlag != True:
				totBol = COSTO_BOLETO_PERDIDO
				q = "INSERT INTO \"Boleto\" (fol_bol, in_ter_bol, out_ter_bol, in_fec_bol, out_fec_bol, id_tar_bol, id_usu_bol, tip_reg, tot_bol, in_hor_bol, out_hor_bol) values ('"+folio+"','"+inputTerminal+"','"+outputTerminal+"','"+dateIn+"','"+dateOut+"', "+str(idTar)+", "+str(idUsu)+", "+str(tipReg)+", "+str(totBol)+", '"+horIn+"', '"+horOut+"');"
				conexion = Conexion()
				f = conexion.execQuery(q)
				if(f<0):
					print("Error: El registro no ha sido guardado")
				else:
					vForm.ventana("REGISTRAR VENTA","TOTAL A COBRAR--------------------------------------------------\n-------------------------COBRA:$"+str(totBol)+"-------------------------\n--------------------------------------------------\n")
					self.clearScreen()
					self.pushButton_5.setEnabled(True)		#LEER BOLETO
					self.limparDespuesDeCancelarBoletoPerdido()
			else:
				vForm.ventana("Error de Registro","Verifica los campos incorrectos")
		self.pushButton_3.setEnabled(True)		#habilitamos el boton de boleto perdido para que forzosamente cobren lo que se leyo
		self.pushButton_2.setEnabled(True)		#Boton de cancelar
		self.pushButton_6.setEnabled(True)		#Boton de Abrir barrera
	pass
		
	def Logout(self):
		self.groupBox.setEnabled(False)
		self.Form.setHidden(True)
		self.daccess.setHidden(True)
		self.clearScreen()
		self.l.lineEdit.setText("")
		self.l.lineEdit_2.setText("")
		self.l.elabel.setText("")
		self.login.setHidden(False)
	pass
	
	def getTarifa(self, index):
		q = "SELECT des_tar FROM \"CTarifas\" where id_tar = "+str(index)+""
		conexion = Conexion()
		q = conexion.doQuery(q)
		return str(q[0][0])
	pass
	
	def aceptarRegistroVenta(self):
		self.labelTotal.setText("$"+str(self.Total))
	
	def clearScreen(self):
		self.cleanUsu()
		self.txtFolio.setText("")
		self.txtInput.setText("")
		self.txtFechin.setText("")
		self.txtHorain.setText("")
		self.labelTotal.setText("$")
		self.Total = 0
		if(self.FEDITABLE==False):
			#aqui tal vez se pueda mandar llamar a la funcion directamente
			self.txtFechin.setEnabled(False)
			self.txtFolio.setEnabled(False)
			self.txtInput.setEnabled(False)
			self.txtHorain.setEnabled(False)
			self.pushButton_5.setEnabled(True)
			self.comboBox.setItemText(3,"Registro Manual")
			self.FEDITABLE = True
			self.tipReg = 1
	pass
		
	def vLogin(self):
		f = -1
		user = self.l.lineEdit.text()
		password = self.l.lineEdit_2.text()
		q = str("SELECT rol_usu FROM \"Usuario\" WHERE usu_usu = '"+user+"' AND pwd_usu = '"+password+"'")
		conexion = Conexion()
		try:
			f = conexion.doQuery(q)[0][0];
		except:
			print("El usuario no se encuentra en la base de datos")
		print(f)
		print "El nuimero anterior esde la funcion de vLoging"
		if(f==1 or f==2 or f==3):
			self.login.setHidden(True)
			if(f==3):
				self.RolRoot=True
				self.groupBox.setEnabled(True)
			if(f==1):
				self.groupBox.setEnabled(True)
			t = RecurringTimer(1.0, self.updateTime)
			t.start_timer() 
			q = str("SELECT nom_usu, app_usu, apm_usu, id_usu FROM \"Usuario\" WHERE usu_usu = '"+user+"' AND pwd_usu = '"+password+"'")
			self.query = conexion.doQuery(q);
			self.labelVendedor.setText(""+str(self.query[0][0])+" "+str(self.query[0][1])+" "+str(self.query[0][2]))
			self.labelOutput.setText(OUTPUT_TERMINAL)
			print "Rol"+str(self.RolRoot)
			self.Form.show()
		elif(f<0):
			self.l.elabel.setText("Error: Datos incorrectos")
		return f
	pass
	
	#Se pueden segrar algunas funciones para el calculo de los minutos
	def leerBoleto(self):
		self.pushButton_3.setEnabled(False)		#Deshabilitamos el boton de boleto perdido para que forzosamente cobren lo que se leyo
		self.pushButton_2.setEnabled(False)		#Boton de cancelar
		self.pushButton_6.setEnabled(False)		#Boton de Abrir barrera
		self.pushButton.setEnabled(False)		#Aceptar
		
		readQR = q.leerCodQR()
		self.txtFolio.setText(readQR[0])
		self.txtInput.setText(readQR[1])
		self.txtFechin.setText(readQR[2])
		self.txtHorain.setText(readQR[3])
		#print("Hora: "+readQR[3][0:2])
		try:
			print("SE CALCULA AUTOMATICO 1")
			self.minsin = int(self.labelHoraout.text()[3:5])
			h=int(readQR[3][0:2])
			m= int(readQR[3][3:5])
			s= int(readQR[3][6:8])
			horaIn= str(h)
			minutosIn=str(m)
			self.tmins=self.calcularMinutosParaLeerBoletos(horaIn, minutosIn)
			self.labelTotal.setText("$"+str(self.Total))
			self.pushButton_5.setEnabled(True)		#LEER BOLETO
			self.pushButton.setEnabled(True)		#Aceptar
			
		except:
			self.labelTotal.setText("$0")	#Falta escribir en archivo apara registrar que se cancele la venta
			print("NO se leyo el boleto y los datos estan nulo")

	pass
	
	def calcularMinutos(self):
		horIn = str(self.txtHorain.text())
		horaAux = horaIn
		horOut = str(self.labelHoraout.text())
		horIn=horIn.replace('\n', '')
		horOut= horOut.replace('\n', '')
		print horIn
		print horOut
		format = '%H:%M:%S'
		horasReales=datetime.strptime(horOut,format) - datetime.strptime(horIn,format)
		self.tmins=horasReales.total_seconds()/60
		print("---------->" + str(self.tmins))
		self.Total = calTar.calcularMonto(self.tmins, self.itarifa, horaAux)
	
	def calcularMinutosParaLeerBoletos(self,horaIn, minutosIn):
		horIn = int(horaIn)
		minutosIn=int(minutosIn)
		horOut = str(self.labelHoraout.text())
		print str(horIn)+":"+str(minutosIn)+":00 ENTRADA"
		print horOut +" Salida"
		format = '%H:%M:%S'
		print "Calculo de tiempo Logica"
		tiempoINtotalMinutos=(horIn*60)+minutosIn	#minutos totales de la hora de entrada
		tiempoOut=time.strptime(horOut,format)
		tiempoOutH=tiempoOut[3] 	#HORAS
		tiempoOutM=tiempoOut[4] 	#MINUTOS
		tiempoOUTtotalMinutos=((int(tiempoOutH))*60)+int(tiempoOutM)
		print "Los minutos totales de entrada: "+str(tiempoINtotalMinutos)
		print "Los minutos totales de salida: "+str(tiempoOUTtotalMinutos)
		self.tmins=int(tiempoOUTtotalMinutos) - int(tiempoINtotalMinutos)
		if self.tmins<0:
			self.tmins=24-(self.tmins*(-1))
			print "ERROR HORA DE SALIDA MAYOR A LA DE ENTRADA"
		self.Total,tipoRegistro = calTar.calcularMonto(self.tmins, self.itarifa, horaIn)
		if tipoRegistro==4:
			self.treg=4
		elif tipoRegistro==5:
			self.treg=5
		elif tipoRegistro==6:
			self.treg=6
		
	def abrirBarrera(self):
		GPIO.setup(13, GPIO.OUT) #Configura el GPIO como salida 
		GPIO.output(13, True) # Transforma el GPIO en un bajo logico
		time.sleep(0.5)
		GPIO.output(13, False) # Turns the GPIO logical Low

	def cerrarBarrera(self): 
		GPIO.setup(6, GPIO.OUT) #Set GPIO Pin as Output 
		GPIO.output(6, True) # Turns the GPIO logical Low
		time.sleep(0.5)
		GPIO.output(6, False) # Turns the GPIO logical Low

	def gpiocleanup(self):
		GPIO.cleanup() # GPIO cleanup upon Close Button Press


		def __del__(self):
			print("Limpiando GPIO")
			self.gpiocleanup()

	def retranslateUi(self, Form):
		self.Form.setWindowTitle(_translate("Form", "Estacionamientos Unicos de Mexico - Registro Salida", None))
		self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Vendedor</span></p><p><span style=\" font-size:14pt;\">Salida </span></p><p><span style=\" font-size:14pt;\">Fecha Actual</span></p><p><span style=\" font-size:14pt;\">Hora Actual</span></p><p><span style=\" font-size:14pt;\">No. de Boleto</span></p><p><span style=\" font-size:14pt;\">Terminal de Entrada</span></p><p><span style=\" font-size:14pt;\">Fecha de Entrada</span></p><p><span style=\" font-size:14pt;\">Hora de Entrada</span></p><p><span style=\" font-size:14pt;\">Tarifa<br/></span></p><p><span style=\" font-size:25pt; font-weight:600;\">Total</span></p></body></html>", None))
		self.label_camara.setText(_translate("Form", "\tESTADO DE LA CAMARA", None))
		self.pushButton.setText(_translate("Form", "Aceptar", None))
		self.pushButton.setShortcut(_translate("Form", "Return", None))
		self.pushButton_2.setText(_translate("Form", "Salir", None))
		self.pushButton_2.setShortcut(_translate("Form", "Esc", None))
		self.pushButton_3.setText(_translate("Form", "Boleto Perdido", None))
		self.label_12.setText(_translate("Form", "Registro Salida", None))
		self.groupBox.setTitle(_translate("Form", "Administracion", None))
		self.comboBox.setItemText(0, _translate("Form", "Gestion de Usuarios", None))
		self.comboBox.setItemText(1, _translate("Form", "Corte de Caja", None))
		self.comboBox.setItemText(2, _translate("Form", "Ajusar Tarifa", None))
		self.comboBox.setItemText(3, _translate("Form", "Registro Manual", None))
		self.pushButton_4.setText(_translate("Form", "OK", None))
		self.pushButton_5.setText(_translate("Form", " Volver a leer Boleto", None))
		self.pushButton_7.setText(_translate("Form", "Cerrar Barrera", None))
		self.pushButton_6.setText(_translate("Form", "Abrir Barrera", None))
		self.pushButton_8.setText(_translate("Form", "APAGAR", None))
		self.statusCamara()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Ui_Form()
    sys.exit(app.exec_())

