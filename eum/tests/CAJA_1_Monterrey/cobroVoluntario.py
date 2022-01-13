import sys
from PyQt4 import QtCore, QtGui, uic
 
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("/home/pi/Documents/CAJA_1_Monterrey/Interfaces_Caja/tarifaVoluntaria.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):

	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.pushButton.clicked.connect(self.btn_event)

	# Evento del boton
	def btn_event(self):
		valor = self.lineEdit.text()
		estado = "bien"
		puntos = 0
		for letra in valor:
			if letra != "1" and  letra != "2" and  letra != "3" and  letra != "4" and  letra != "5" and  letra != "6" and  letra != "7" and  letra != "8" and  letra != "9" and  letra != "0" and  letra != ".":
				estado = "error"
			if letra == ".":
				puntos = puntos + 1
		if valor == "":
			estado = "vacio"
		if estado == "error" or puntos > 1:
			self.label_3.setText("Cantidad no valida")
		elif estado == "vacio":
			self.label_3.setText("Ingresa una cantidad")
		else:
			archivo=open("/home/pi/Documents/CAJA_1_Monterrey/montoVoluntario.txt", "w")
			archivo.write(valor)
			archivo.close()
			exit()
			pass

app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()
