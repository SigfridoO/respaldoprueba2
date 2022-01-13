from PyQt4 import QtCore, QtGui
import RPi.GPIO as GPIO
from threading import Thread
import time,os
import commands

PATH_PONER_DATOS_TICKET="/home/pi/Documents/CAJA_1_Monterrey/datos_tikets/ticket.txt "
PATH_PONER_DATOS_TICKET_AUX="/home/pi/Documents/CAJA_1_Monterrey/datos_tikets/ticketAux.txt"
DESPLEGAR_CAMARA="sudo zbarcam --raw  --prescale=10x10"
DESPLEGAR_INTERFAZ_ENTRADA="sudo python /home/pi/Documents/CAJA_1_Monterrey/registrosalida.py"
DESPLEGAR_INTERFAZ_ENTRADA_SIN_IMPRESORA="sudo python /home/pi/Documents/CAJA_1_Monterrey/registrosalidaSinImpresora.py"


def activarCamara():
	print "EL hilo ...." 
	os.system("rm "+PATH_PONER_DATOS_TICKET)
	os.system("rm "+PATH_PONER_DATOS_TICKET_AUX)
	os.system(DESPLEGAR_CAMARA+" >> "+PATH_PONER_DATOS_TICKET)
	os.system(" echo -1 >> "+PATH_PONER_DATOS_TICKET)
	os.system(" echo [Error] Camara >> "+PATH_PONER_DATOS_TICKET)
	os.system(" echo [Error] Devolvio un estado de ERROR  ...>> "+PATH_PONER_DATOS_TICKET)
	os.system(" echo [Error] Asegurate de conectar la camara. >> "+PATH_PONER_DATOS_TICKET)

def ejecutaInterfaz():
	os.system(DESPLEGAR_INTERFAZ_ENTRADA)

def Hilos():
	thread1 = Thread(target = activarCamara, args=())
	thread2 = Thread(target = ejecutaInterfaz, args=())
	try:
		thread1.start()
		thread2.start()
	except Exception:
		pass
		
	while(thread1.is_alive):
		kill = 0
	kill = 1

def ejecutaInterfazSIN_IMPRESORA():
	os.system(DESPLEGAR_INTERFAZ_ENTRADA_SIN_IMPRESORA)

def Hilos2():
	thread1 = Thread(target = activarCamara, args=())
	thread2 = Thread(target = ejecutaInterfazSIN_IMPRESORA, args=())
	try:
		thread1.start()
		thread2.start()
	except Exception:
		pass
		
	while(thread1.is_alive):
		kill = 0
	kill = 1




if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(20,GPIO.IN)
	GPIO.setup(21,GPIO.IN)
	config1 = GPIO.input(20)
	config2 = GPIO.input(21)
	
	if(config1==True and config2==True ):	# conf1 = 1 and conf2 = 1	CONFIGURAR DATOS
		print("Acceso para Configurar Caja Y expedidora")
		os.system("lxterminal -e sudo python /home/pi/Documents/EUM_CONFIGURACION_EXP/entrada.py  ")
	elif(config1==False and config2==False):# conf1 = 0 and conf2 = 0		ENTRADA A PROGRAMADORES
		#print("Entrada")
		from registrosalida import Ui_Form
		Hilos()	
	elif(config1==False and config2==True):	# conf1 = 0 and conf2 = 1		EXPEDIDORA
		print("Entrada")
		os.system("sudo python3 /home/pi/Documents/eum/app/expedidora/first.py")
	elif(config1==True and config2==False ):	# conf1 = 1 and conf2 = 0		SALIDA
		#os.system("sudo python3 /home/pi/Documents/eum/app/salida/salida.py")
		print("Acceso Caja Sin impresora")
		from registrosalidaSinImpresora import Ui_Form
		Hilos2()
	GPIO.cleanup()

