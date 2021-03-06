#!/usr/bin/env python3
import sys
import os
import time
import fechaUTC as hora
import cliente as Servidor
from pygame import mixer
import subprocess
#import imprimirBoleto as impresora
from threading import Timer,Thread 
import sched
import termios
import serial
import binascii
from bitstring import BitArray
from PyQt5.QtWidgets import QMainWindow,QApplication, QDialog, QGridLayout, QMessageBox,QLabel, QPushButton, QLineEdit,QSpinBox, QTableWidget,QTableWidgetItem,QComboBox,QCheckBox
from PyQt5 import QtCore, QtGui, uic
from datetime import datetime, timedelta
import calendar
import psycopg2, psycopg2.extras
import leerBotones as botones

PATH_ARCHIVO_CONFIGURACION_TERMINAL_SERIAL="/home/pi/Desktop/numeroSerial.txt"

clock = sched.scheduler(time.time, time.sleep)
cp=0
#global ser
DA=1166
Sinpago=0
ser=0
total = 0
bill = 0
a=0
ma=0
factorDeEscala = .10
tarifa=1
aux_tarifa=0
cambio=0
aux_cambio = 0
aux_cambio1 = 0
estatus=0
rep=0
kill = 0
killer = 0
kill_aux = 0
killbill=0
leido = 0
cajeroSuspendido=0
conteoPantallaPrincipal = 0
aux_tarifa1 =0
aux_dif=""
fo=""
fe=""
pe=""
costillo=0
hh=""
hsalida=""
avis=""
pagado=0
w=0
mona=0
mond=0
cs1=0
cs2=0
config=0
ser=0
monedas=[85,78,69,58]
monedasPago=[0,0,0,0]
monedasCambio=[0,0,0,0]
billetesPago=[0,0,0,0]
tarifasAplicadas=""
monedasTotal=290
dineroTotal=1166
dineroTotalB=0
billetesTotales=0
billetes=[0,0,0,0]
mensajeBoletoUsado=0
mensajeBoletoPerdido=0
mensajeError=0
suspenderCajero=0
mensajeAyuda=0
cartuchoRemovido=0
preguntarPorEstado=0
mostrarTiempoDeSalidaRestante=[0,'']
conn = psycopg2.connect(database='CajerOk',user='postgres',password='Postgres3UMd6', host='localhost')
cur = conn.cursor()
tarifaVoluntaria=0
vvol=""
comienzaCambio=0
nivelDeCambio=0
nivelActual=[0,0,0,0]
nom=""
loc=""
contadorCartuchos=1
opcionAdmin=0
cambiaColor=0
imprime=0
accesoAcaja=0
inicioPago=0
tiempoAgotadoDePago=0
y=0
z=0
p=0
w=0
q=0
v=0
c=0
USUARIO=0
correoUSUARIO=""
NoCajero=0
tarifaSeleccionada=0
varc=0
#red=117
#green=248
#blue=148
rrr=0
"""red=59
green=109
blue=153
"""
red=125
green=181
blue=215
comienzaLectura=0
varl=0
comienzaCobro=0
registraPago=0


configuracion = []
camInicial=''
USUARIO=''
host=''
ip=''
noEquipo = 0
plaza = ""
localidad = ""
user="eum"
pswd="pi"

aportacionConfirmada=0
def interface():
	class Ventana(QDialog):
		conteo_final=0
		global ser,gui,total,conn,cur,nivelActual,NoCajero,cp
		def __init__(self):
			QDialog.__init__(self)
			gui = uic.loadUi("/home/pi/Documents/eum/app/cajeroF/rb.ui", self)
			self.montos()
			gui.leerBotones()
			#gui.boleto_leido()
			gui.contadorSegundos()
			gui.contadorMiliSegundos()
			fehoy=str(datetime.now().date()).split('-',2)
			fehoy=fehoy[2]+"/"+fehoy[1]+"/"+fehoy[0]
			#self.ldate.setText(fehoy)
			self.ldate2.setText(fehoy)

			self.current_timer = None
			self.prioridad=0
			#self.alerta.setVisible(False)
			self.lerror1.setVisible(False)

			self.salirAdmin.clicked.connect(self.saliendoAdmin)

			self.bntarifa.clicked.connect(lambda:self.cambia(7))
			self.bcancelar.clicked.connect(lambda:self.cambia(6))
			self.benter.setShortcut('Return')
			self.bcancelarPago.setShortcut('c')
			self.bsalirTarifas.clicked.connect(lambda:self.cambia(9))
			self.bsalirntarifas.clicked.connect(lambda:self.cambia(9))
			self.bconfirmartarifa.clicked.connect(self.tarifaConfirmada)
			self.bquitar.clicked.connect(self.elimina2)
			self.bhabilitar.clicked.connect(self.habilitaTarifa)
			self.bconfirmavol.clicked.connect(self.volConfirmado)
			self.bn1.clicked.connect(lambda:self.tecladoSum(1))
			self.bn2.clicked.connect(lambda:self.tecladoSum(2))
			self.bn3.clicked.connect(lambda:self.tecladoSum(3))
			self.bn4.clicked.connect(lambda:self.tecladoSum(4))
			self.bn5.clicked.connect(lambda:self.tecladoSum(5))
			self.bn6.clicked.connect(lambda:self.tecladoSum(6))
			self.bn7.clicked.connect(lambda:self.tecladoSum(7))
			self.bn8.clicked.connect(lambda:self.tecladoSum(8))
			self.bn9.clicked.connect(lambda:self.tecladoSum(9))
			self.bn0.clicked.connect(lambda:self.tecladoSum(0))
			self.bnborrar.clicked.connect(lambda:self.tecladoSum(10))
			#self.lnom.editingFinished.connect(lambda:self.holi(3))
			#self.llol.editingFinished.connect(lambda:self.holi(6))

			#self.bconfirmarplaza.clicked.connect(self.cambiaNombre)
			self.salirplaza.clicked.connect(lambda:self.cambia(9))
			self.salirCalibracion.clicked.connect(self.finalizarCalibracion)
			self.salirCajon.clicked.connect(self.finalizarCorteCaja)
			self.salirAyuda.clicked.connect(self.finalizarSoporteTecnico)
			self.salirReportes.clicked.connect(lambda:self.cambia(9))
			self.bsalirLogin.clicked.connect(lambda:self.cambia(9))
			self.idtar2.valueChanged.connect(self.actualizaMensaje)
			self.idtar1.valueChanged.connect(self.actualizaMensaje2)

			"""self.btarifas.clicked.connect(self.seccionTarifas)
			self.bcorte.clicked.connect(self.cortandoLaCaja)
			self.bcalibracion.clicked.connect(self.calibrando)
			self.bplaza.clicked.connect(self.llenaCamposPlaza)
			self.bpapel.clicked.connect(self.reemplazoPapel)
			self.bpublicidad.clicked.connect(self.menuPublicidad)
			self.breporte.clicked.connect(lambda:self.cambia(12))
			"""
			self.btarifas.clicked.connect(lambda:self.mueveyManda(1))
			self.bcorte.clicked.connect(lambda:self.mueveyManda(2))
			self.bcalibracion.clicked.connect(lambda:self.mueveyManda(3))
			self.bplaza.clicked.connect(lambda:self.mueveyManda(4))
			self.bpapel.clicked.connect(lambda:self.mueveyManda(5))
			self.bpublicidad.clicked.connect(lambda:self.mueveyManda(6))
			self.breporte.clicked.connect(lambda:self.mueveyManda(7))
			self.bayuda.clicked.connect(lambda:self.mueveyManda(8))
			self.bcancelarPago.clicked.connect(self.cancelandoPago)
			self.bnoserie.clicked.connect(self.mostrarNoSerie)
			#self.bcam.clicked.connect(self.activaCamara)


			self.bentrar.clicked.connect(self.validaLogin)
			self.bboletoPerdido.clicked.connect(self.boletoPerdido)
			self.reporteTar.clicked.connect(self.imprimeReporteTarifas)
			self.bayudaCliente.clicked.connect(self.ayudando2)
			self.bayudaCliente2.clicked.connect(self.ayudando)

			self.bimprimeEventos.clicked.connect(self.imprimeReporteEventos)
			self.bpdf.clicked.connect(self.imprimeReporteEventosPDF)
			self.bimpReporteCaja.clicked.connect(self.imprimeReporte)
			self.cambia(0)



			self.tablatarifas.setColumnCount(12)
			self.tablatarifas.setHorizontalHeaderLabels(['','Id','Prioridad','Fecha_ini','Fecha_fin','Hora_ini','Hora_fin','Dia_semana','Descripcion','costo','intervalo_1','intervalo_2'])

			self.tablaMantenimiento.setColumnCount(4)
			self.tablaMantenimiento.setHorizontalHeaderLabels(['Nombre','Tipo','Descripcion','Fecha y hora'])

			cur.execute("select MAX(\"idCajero\") from \"CAJERO\"")
			for reg in cur:
				idc=reg[0]

			cur.execute("update \"CAJERO\" set \"idCajero\"="+NoCajero+" where \"idCajero\"="+str(idc))
			conn.commit()



	################MODS########
			self.bapagar.clicked.connect(self.apagarRasp)
			self.breiniciar.clicked.connect(self.reiniciarRasp)
			self.bconfirmarIP.clicked.connect(self.cambiaIp)
			self.bpanelconf.clicked.connect(self.muestraPanel)
			self.bsalirConfig.clicked.connect(lambda:self.cambia(0))
			self.bsalirLogin.clicked.connect(lambda:self.cambia(0))
			self.bsalirsucursal.clicked.connect(lambda:self.cambia(17))
			self.bsalirred.clicked.connect(lambda:self.cambia(17))
			self.bsalirCambiarFecha.clicked.connect(lambda:self.cambia(17))
			self.bsucursal.clicked.connect(lambda:self.cambia(16))
			self.bred.clicked.connect(lambda:self.cambia(15))
			self.breporte.clicked.connect(lambda:self.cambia(0))
			self.bhora.clicked.connect(lambda:self.cambia(19))
			
			self.lerror1.setVisible(False)
			self.bentrar.clicked.connect(self.validaLogin)
			self.bcambiarFecha.clicked.connect(self.cambiaFecha)
			#self.bguardar.clicked.connect(self.setConfig)
			#self.bsalirConfig.clicked.connect(self.salirConf)
			self.bconfirmarplaza.clicked.connect(self.setConfig)
			self.panelConfig()
			self.datosEstacionamiento()
			self.bcam.clicked.connect(self.scan)
			self.bcam.setShortcut("Return")
			
			
			
			
		def scan(self):
			#thread3 = Thread(target=leerCodQR, args = ())
			text=self.lscan.text()
			text=text.replace("'","-")
			text=text.replace("??",":")
			text=text.split(',')
			#os.system("sudo nice -n -19 python3 archimp.py")
			try:
				leerArch = open("/home/pi/Documents/ticket.txt", "w")
				leerArch.write(str(text[0])+"\n"+str(text[1])+"\n"+str(text[2])+"\n"+str(text[3])+"\n"+str(text[4]))
				leerArch.close()
				self.lscan.setText('')
			except Exception as e:
				print(e)
				pass
			#p=subprocess.Popen(['/home/pi/scanner/dsreader -l 1 -s 20 > /home/pi/Documents/ticket.txt'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
			
			#so=os.popen('~/bin/dsreader -l 1 -s 20 > /home/pi/Documents/ticket.txt')
		
		
		def validaLogin(self):
			global cur,accesoAcaja,USUARIO,correoUSUARIO,user,pswd
			nom=self.lusu.text()
			rol_us=""
			indice=0
			contr=self.lcont.text()
			if(nom==user):
				if(contr==pswd):
					self.cambia(18)
				else:
					self.lerror1.setText("usuario o contrase??a incorrectos")
					self.lerror1.setVisible(True)
			else:
				self.lerror1.setText("usuario o contrase??a incorrectos")
				self.lerror1.setVisible(True)
			"""cur.execute("SELECT * FROM \"USUARIO\" WHERE usuario=%s and contra=%s order by \"idUsuario\" ASC",(nom,contr))

			print("nom,contr=",nom,contr)
			for reg in cur:
				print(reg[1],reg[2],reg[3],reg[4],reg[5],reg[6])
				rol_us=reg[1]
				indice=1
			if(indice==0):
				self.lerror1.setText("usuario o contrase??a incorrectos")
				self.lerror1.setVisible(True)
			else:
				USUARIO=str(reg[0])
				self.cambia(5)"""
		
		def cambiaFecha(self):
			a=self.dtime.dateTime()
			b=self.dtime.textFromDateTime(a)
			print(b,type(b))
			os.system("sudo date -s '"+b+"' ")
			
		def setConfig(self):
			global plaza,localidad,noEquipo,host,ip,pol,pol1,pol2,pol3,pol4,pol5,impresora,anchoPapel
			lenn=0
			plaza=str(self.lnom.text())
			localidad=str(self.lloc.text())
			noEquipo=str(self.leq.text())
			
			
			print(plaza,localidad)
			dat=plaza+","+localidad+","+str(noEquipo)
			infile = open("/home/pi/Documents/eum/app/cajeroF/cajero/archivos_config/datos.txt", 'w')
			c=infile.write(dat)
			
			self.datosEstacionamiento()
			self.cambia(0)
			
		
			
			
			
			
		def datosEstacionamiento(self):
			global plaza,localidad,noEquipo,host,ip,pol,pol1,pol2,pol3,pol4,pol5,impresora,anchoPapel
			lenn=0
			self.lnom.setText(plaza)
			self.lloc.setText(localidad)
			self.leq.setText(str(noEquipo))
			self.nomPlaza_2.setText(plaza)
			self.nomLoc_2.setText(localidad)
			self.lhost.setText(host)
			self.lip.setText(ip)
			
			
		def panelConfig(self):
			global plaza,localidad,noEquipo,host,ip
			infile = open('/home/pi/Documents/eum/app/cajeroF/cajero/archivos_config/datos.txt','r')
			datos= infile.readline()
			arr=datos.split(',')
			plaza=arr[0]
			localidad=arr[1]
			noEquipo=arr[2]
			infile.close()
			
			infile = open('/home/pi/Documents/eum/app/cajeroF/cajero/archivos_config/red.txt','r')
			datos= infile.readline()
			arr=datos.split(',')
			host=arr[0]
			ip=arr[1]
			infile.close()
			
			
		def salirConf(self):
			global panelConf
			panelConf=0
			self.cambia(0)
			

		
		
		
		def sustituye(self,archivo,buscar,reemplazar):
			"""

			Esta simple funci??n cambia una linea entera de un archivo

			Tiene que recibir el nombre del archivo, la cadena de la linea entera a

			buscar, y la cadena a reemplazar si la linea coincide con buscar

			"""
			with open(archivo, "r") as f:

				# obtenemos las lineas del archivo en una lista

				lines = (line.rstrip() for line in f)
				print(lines)

		 

				# busca en cada linea si existe la cadena a buscar, y si la encuentra

				# la reemplaza

				

				altered_lines = [reemplazar if line==buscar else line for line in lines]
				f= open(archivo, "w+")
				print(altered_lines[0],len(altered_lines))
				for i in range(len(altered_lines)):
					if(buscar in altered_lines[i]):
						print (altered_lines[i])
						cambia=altered_lines[i]
						f.write(reemplazar+"\n")
					else:
						f.write(altered_lines[i]+"\n")
				f.close()
				
				
		def cambiaIp(self):
			global host,ip
			host=self.lhost.text()
			ip=self.lip.text()

			self.sustituye("/home/pi/Documents/eum/app/cajeroF/cajero/cliente.py","192.168","host = '"+host+"'")
			self.sustituye("/etc/dhcpcd.conf","ip_address","static ip_address="+ip+"/24")
			ip=ip.split(".")
			ip=ip[0]+"."+ip[1]+"."+ip[2]+".1"
			self.sustituye("/etc/dhcpcd.conf","routers","static routers="+ip)

			
			host=str(self.lhost.text())
			ip=str(self.lip.text())
			
			
			print(plaza,localidad)
			dat=host+","+ip
			infile = open("/home/pi/Documents/eum/app/cajeroF/cajero/archivos_config/red.txt", 'w')
			c=infile.write(dat)
			
			self.datosEstacionamiento()
			self.cambia(0)
			
			
		def muestraPanel(self):
			self.cambia(17)
			#datos=obtenerPlazaYLocalidad()
			#self.lno.setText(str(datos[0]))
			#self.llo.setText(str(datos[1]))
			#datos=obtenerTerminal()
			self.lusu.setText('')
			self.lcont.setText('')
			self.lerror1.setText('')
			
		def cambia(self,val):
			self.stackedWidget.setCurrentIndex(val)
		
		def apagarRasp(self):
			print("apagando...")
			os.system("sudo shutdown -P 0")
		def reiniciarRasp(self):
			print("apagando...")
			os.system("sudo shutdown -r 0")
			############################MODS FIN#################

		def activaCamara(self):
			#thread3 = Thread(target=leerCodQR, args = ())
			thread3 = Thread(target=leerCodQR, args = ())
			#os.system("sudo nice -n -19 python3 archimp.py")
			try:
			
				thread3.start()



			except Exception as e:
				pass
			#p=subprocess.Popen(['/home/pi/scanner/dsreader -l 1 -s 20 > /home/pi/Documents/ticket.txt'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
			
			#so=os.popen('~/bin/dsreader -l 1 -s 20 > /home/pi/Documents/ticket.txt')
			
			
		def mostrarNoSerie(self):
			global accesoAcaja,NoCajero,mensajeAyuda
			os.system("sudo grep Serial /proc/cpuinfo >> /home/pi/Desktop/numeroSerial.txt")
			configuracion=[]
			archivo=open(PATH_ARCHIVO_CONFIGURACION_TERMINAL_SERIAL, "r")
			c=archivo.readline()
			serie=c.split(':', 1 )
			archivo.close()
			self.lserie.setText("No. Serie: "+str(serie[1]))

			self.lmodelo.setVisible(True)
			self.lserie.setVisible(True)

		def ayudando(self):
			global accesoAcaja,NoCajero,mensajeAyuda
			descripciones=self.obtenerDineroActual()
			mensaje=str("ayuda@ayuda.com")+","+str(NoCajero)+",3,"+descripciones[0]+","+descripciones[1]
			resultado=Servidor.configSocket("log inicial", mensaje)

			if(resultado==-1):
				self.lerror1.setText("Problema en la conexion")
				self.lerror1.setVisible(True)
			else:
				#botones.apagarMonedero()
				mensajeAyuda=1
				pass

		def ayudando2(self):
			global accesoAcaja,NoCajero,mensajeAyuda
			descripciones=self.obtenerDineroActual()
			mensaje=str("ayuda@ayuda.com")+","+str(NoCajero)+",3,"+descripciones[0]+","+descripciones[1]
			resultado=Servidor.configSocket("log inicial", mensaje)

			if(resultado==-1):
				self.lerror1.setText("Problema en la conexion")
				self.lerror1.setVisible(True)
			else:
				#botones.apagarMonedero()
				mensajeAyuda=1
				self.aviso1.setText("Tu peticion esta siendo atendida")
				pass

		def cancelandoPago(self):
			global cp
			print("BOTON CANCEL PRESIONADO")
			cp=1

		def finalizarCalibracion(self):
			global cartuchoRemovido,NoCajero,correoUSUARIO,cajeroSuspendido
			cajeroSuspendido=0
			if(cartuchoRemovido==0):
				cartuchoRemovido=0
				self.cambia(9)
				mensaje=str(correoUSUARIO)+","+str(NoCajero)+",1"
				resultado=Servidor.configSocket("log final", mensaje)
				if(resultado==-1):
					pass
				else:
					pass
			else:
				cartuchoRemovido=0
				self.cambia(9)
				mensaje=str(correoUSUARIO)+","+str(NoCajero)+",2"
				resultado=Servidor.configSocket("log final", mensaje)
				if(resultado==-1):
					pass
				else:
					pass

		def finalizarCorteCaja(self):
			global cartuchoRemovido,NoCajero,correoUSUARIO
			if(cartuchoRemovido==0):
				cartuchoRemovido=0
				self.cambia(9)
				mensaje=str(correoUSUARIO)+","+str(NoCajero)+",1"
				resultado=Servidor.configSocket("log final", mensaje)
				if(resultado==-1):
					pass
				else:
					pass
			else:
				cartuchoRemovido=0
				self.cambia(9)
				mensaje=str(correoUSUARIO)+","+str(NoCajero)+",2"
				resultado=Servidor.configSocket("log final", mensaje)
				if(resultado==-1):
					pass
				else:
					pass
				#no sabria que hacer

		def finalizarSoporteTecnico(self):
			global cartuchoRemovido,NoCajero,correoUSUARIO
			if(cartuchoRemovido==0):
				cartuchoRemovido=0
				self.cambia(9)
				mensaje=str(correoUSUARIO)+","+str(NoCajero)+",1"
				resultado=Servidor.configSocket("log final", mensaje)
				if(resultado==-1):
					pass
				else:
					pass
			else:
				cartuchoRemovido=0
				self.cambia(9)
				mensaje=str(correoUSUARIO)+","+str(NoCajero)+",2"
				resultado=Servidor.configSocket("log final", mensaje)
				if(resultado==-1):
					pass
				else:
					pass
				#no sabria que hacer

		def imprimeReporteEventosPDF(self):
			dia=str(self.fechaInicio.date().day())
			mes=str(self.fechaInicio.date().month())
			anio=str(self.fechaInicio.date().year())

			dia2=str(self.fechaFin.date().day())
			mes2=str(self.fechaFin.date().month())
			anio2=str(self.fechaFin.date().year())

			fecha1=dia+"/"+mes+"/"+anio+" 00:00:00"
			fecha2=dia2+"/"+mes2+"/"+anio2+" 23:59:59"
			fechaFinal=fecha1+","+fecha2
			leerArch = open("/home/pi/Documents/fechaEventos.txt", "a+")
			leerArch.write(fechaFinal)
			leerArch.close()
			os.system("sudo python3 /home/pi/Documents/eum/app/cajeroF/cajero/reporteEventosPDF.py")

		def imprimeReporteEventos(self):
			dia=str(self.fechaInicio.date().day())
			mes=str(self.fechaInicio.date().month())
			anio=str(self.fechaInicio.date().year())

			dia2=str(self.fechaFin.date().day())
			mes2=str(self.fechaFin.date().month())
			anio2=str(self.fechaFin.date().year())

			fecha1=dia+"/"+mes+"/"+anio+" 00:00:00"
			fecha2=dia2+"/"+mes2+"/"+anio2+" 23:59:59"
			fechaFinal=fecha1+","+fecha2
			leerArch = open("/home/pi/Documents/fechaEventos.txt", "a+")
			leerArch.write(fechaFinal)
			leerArch.close()
			os.system("sudo python3 /home/pi/Documents/cajero/reporteEventos.py")

		def imprimeReporteTarifas(self):
			dia=str(self.fechaInicio2.date().day())
			mes=str(self.fechaInicio2.date().month())
			anio=str(self.fechaInicio2.date().year())

			dia2=str(self.fechaFin2.date().day())
			mes2=str(self.fechaFin2.date().month())
			anio2=str(self.fechaFin2.date().year())

			fecha1=dia+"/"+mes+"/"+anio+" 00:00:00"
			fecha2=dia2+"/"+mes2+"/"+anio2+" 23:59:59"
			fechaFinal=fecha1+","+fecha2
			leerArch = open("/home/pi/Documents/fechaTarifas.txt", "a+")
			leerArch.write(fechaFinal)
			leerArch.close()
			os.system("sudo python3 /home/pi/Documents/cajero/reporteTarifas.py")


		def leerBotones(self):
			global cp,leido,opcionAdmin,accesoAcaja,NoCajero,accesoAcaja,aux_tarifa,cambio
			botones.configurarPinesGPIO()
			#botones.prenderMonedero()
			chapaMagnetica = botones.leerBotonesEntrada()
			bnCancelar = botones.botonCancelar()
			chapaMagnetica2=botones.leerBotonesEntrada2()
			if(bnCancelar):
			#if(bnCancelar and aux_tarifa!=0):
				cp=1
				print("BOTON CANCELAR PRESIONADOO")
			"""
			if(chapaMagnetica==True):
				print("Magnetizado")
				if(chapaMagnetica2==True):
					print("cerrado y magnetizado")
				else:
					print("abierto y magnetizado")
					if(accesoAcaja=1):
						#Mostrar mensaje en pantalla... Cerrar puerta!!!  , ALERTA
					else:
						#ALERTA: CAJERO ABIERTO SIN AUTORIZACION
						mensaje=str("ASALTO@ayuda.com")+","+str(NoCajero)+",4,"+"0:0"+","+"0:0"
						resultado=Servidor.configSocket("log inicial", mensaje)
						if(resultado==-1):
							self.lerror1.setText("Problema en la conexion")
							self.lerror1.setVisible(True)
						else:
							pass
			else:
				if(chapaMagnetica2==True):
					print("cerrado y DESmagnetizado")
					#Sin significado, NO ACCION.
				else:
					print("abierto y DESmagnetizado")
					#Se esta retirando el dinero posiblemente... 10 segeundos limite para magnetizar....
			if(sensorMovimiento==True):
				print("OK")
			else:
				if(opcionAdmin==2):
					print("OK2")
				else:
					print("Caja levantada")
					descripciones=self.obtenerDineroActual()
					mensaje=str("sensorCaja@ayuda.com")+","+str(NoCajero)+",4,"+"0:0"+","+"0:0"
					resultado=Servidor.configSocket("log inicial", mensaje)
					if(resultado==-1):
						self.lerror1.setText("Problema en la conexion")
						self.lerror1.setVisible(True)
					else:
						pass
				
			"""
				#self.avisoInserta.setText("Puerta cerrada")
			QtCore.QTimer.singleShot(100, self.leerBotones)

		def imprimeReporte(self):
			global contadorCartuchos
			fec=datetime.now().date()
			fec=str(fec.day)+"/"+str(fec.month)+"/"+str(fec.year)
			k1=self.m1.text()
			k2=self.m2.text()
			k3=self.m5.text()
			k4=self.m10.text()
			k5=self.mt.text()
			k6=self.b20.text()
			k7=self.b50.text()
			k8=self.b100.text()
			k9=self.b200.text()
			k10=self.bt.text()
			k11=self.dm.text()
			k12=self.db.text()
			k13=self.dt.text()
			datos=fec+','+k1+','+k2+','+k3+','+k4+','+k5+','+k6+','+k7+','+k8+','+k9+','+k10+','+k11+','+k12+','+k13+','+str(contadorCartuchos)
			leerArch = open("/home/pi/Documents/reporteCorteCaja.txt", "a+")
			leerArch.write(datos)
			leerArch.close()
			os.system("sudo python3 /home/pi/Documents/cajero/imprimeCorte.py")
		def mueveyManda(self,valor):
			global opcionAdmin
			opcionAdmin=valor
			self.cambia(11)
			self.lerror1.setVisible(False)
			self.lusu.setText("")
			self.lcont.setText("")

		def validaLogin(self):
			global cur,opcionAdmin,accesoAcaja,USUARIO,correoUSUARIO
			nom=self.lusu.text()
			rol_us=""
			indice=0
			contr=self.lcont.text()
			cur.execute("SELECT * FROM \"USUARIO\" WHERE usuario=%s and contra=%s order by \"idUsuario\" ASC",(nom,contr))

			print("nom,contr=",nom,contr)
			for reg in cur:
				print(reg[1],reg[2],reg[3],reg[4],reg[5],reg[6])
				rol_us=reg[1]
				indice=1
			if(indice==0):
				self.lerror1.setText("usuario o contrase??a incorrectos")
				self.lerror1.setVisible(True)
			else:
				USUARIO=str(reg[0])
				correoUSUARIO=str(reg[7])
				if(opcionAdmin==1 and rol_us==1):
					self.seccionTarifas()
				elif(opcionAdmin==2 and rol_us==4):
					self.cortandoLaCaja()
				elif(opcionAdmin==3 and rol_us==3):
					self.calibrando()
				elif(opcionAdmin==4 and rol_us==1):
					self.llenaCamposPlaza()
				elif(opcionAdmin==5 and rol_us==3):
					self.reemplazoPapel()
				elif(opcionAdmin==6 and rol_us==1):
					self.menuPublicidad()
				elif(opcionAdmin==7 and rol_us==1):
					self.cambia(12)
				elif(opcionAdmin==8 and rol_us==5):
					self.seccionAyuda()
				else:
					self.lerror1.setText("Acceso denegado")
					self.lerror1.setVisible(True)


		def calibrando(self):
			global contadorCartuchos,monedas,monedasTotal,dineroTotal,correoUSUARIO,accesoAcaja,NoCajero
			fecha=hora.mostrarFechayHora()
			i=-1
			descripciones=self.obtenerDineroActual()
			mensaje=str(correoUSUARIO)+","+str(NoCajero)+",2,"+descripciones[0]+","+descripciones[1]
			resultado=Servidor.configSocket("log inicial", mensaje)
			if(resultado==-1):
				self.lerror1.setText("Problema en la conexion")
				self.lerror1.setVisible(True)
			else:
				fecha=hora.mostrarFechayHora()
				accesoAcaja=1
				botones.abrirPuerta()
				contadorCartuchos=contadorCartuchos+1
				self.lnumc.setText(str(contadorCartuchos))
				self.lniv.setText(""+str(nivelActual[0])+","+str(nivelActual[1])+","+str(nivelActual[2])+","+str(nivelActual[3]))
				self.cambia(5)
				monedas[0]=monedas[0]+85
				monedas[1]=monedas[1]+78
				monedas[2]=monedas[2]+69
				monedas[3]=monedas[3]+58
				monedasTotal=monedasTotal+290
				dineroTotal=dineroTotal+1166

				consu="insert into \"USUARIO_LOG\"(usuario,log,detalle,fecha) values("+str(USUARIO)+",5,'"+str(contadorCartuchos)+"','"+fecha+"')"
				cur.execute(consu)
				conn.commit()

			#REPORTAR LOG A SERVIDOR....

		def menuPublicidad(self):
			global USUARIO,accesoAcaja
			fecha=hora.mostrarFechayHora()
			accesoAcaja=1
			botones.abrirPuerta()
			botones.configurarPublicidad()
			botones.manteniendoElCero()
			consu="insert into \"USUARIO_LOG\"(usuario,log,detalle,fecha) values("+str(USUARIO)+",8,'Publicidad','"+fecha+"')"
			cur.execute(consu)
			conn.commit()

		def reemplazoPapel(self):
			global correoUSUARIO,accesoAcaja,NoCajero
			descripciones=self.obtenerDineroActual()
			mensaje=str(correoUSUARIO)+","+str(NoCajero)+",2,"+descripciones[0]+","+descripciones[1]
			resultado=Servidor.configSocket("log inicial", mensaje)
			if(resultado==-1):
				self.lerror1.setText("Problema en la conexion")
				self.lerror1.setVisible(True)
			else:
				fecha=hora.mostrarFechayHora()
				accesoAcaja=1
				botones.abrirPuerta()
				consu="insert into \"USUARIO_LOG\"(usuario,log,detalle,fecha) values("+str(USUARIO)+",9,'rollo reemplazado','"+fecha+"')"
				cur.execute(consu)
				conn.commit()

		def seccionAyuda(self):
			global correoUSUARIO,accesoAcaja,NoCajero
			descripciones=self.obtenerDineroActual()
			mensaje=str(correoUSUARIO)+","+str(NoCajero)+",3,"+descripciones[0]+","+descripciones[1]
			resultado=Servidor.configSocket("log inicial", mensaje)
			if(resultado==-1):
				self.lerror1.setText("Problema en la conexion")
				self.lerror1.setVisible(True)
			else:
				fecha=hora.mostrarFechayHora()
				accesoAcaja=1
				botones.abrirPuerta()
				self.cambia(4)
				consu="insert into \"USUARIO_LOG\"(usuario,log,detalle,fecha) values("+str(USUARIO)+",9,'rollo reemplazado','"+fecha+"')"
				cur.execute(consu)
				conn.commit()

		def llenaCamposPlaza(self):
			global rep,nom,loc,nivelDeCambio
			infile = open("/home/pi/Documents/plaza.txt", 'r')
			c=infile.readline()
			arr=c.split(',', 1 )
			infile.close()
			nom=str(arr[0])
			loc=str(arr[1])
			self.lnom.setText(nom)
			self.llol.setText(loc)
			self.cambia(10)
		
		def sustituye(self,archivo,buscar,reemplazar):
			"""

			Esta simple funci??n cambia una linea entera de un archivo

			Tiene que recibir el nombre del archivo, la cadena de la linea entera a

			buscar, y la cadena a reemplazar si la linea coincide con buscar

			"""
			with open(archivo, "r") as f:

				# obtenemos las lineas del archivo en una lista

				lines = (line.rstrip() for line in f)
				print(lines)

		 

				# busca en cada linea si existe la cadena a buscar, y si la encuentra

				# la reemplaza

				

				altered_lines = [reemplazar if line==buscar else line for line in lines]
				f= open(archivo, "w+")
				print(altered_lines[0],len(altered_lines))
				for i in range(len(altered_lines)):
					if(buscar in altered_lines[i]):
						print (altered_lines[i])
						cambia=altered_lines[i]
						f.write(reemplazar+"\n")
					else:
						f.write(altered_lines[i]+"\n")
				f.close()
		

		def cambiaNombre(self):
			global nom,loc,USUARIO
			fecha=hora.mostrarFechayHora()
			outfile = open("/home/pi/Documents/plaza.txt", 'w')
			nn=self.lnom.text()
			ln=self.llol.text()
			outfile.write(str(nn)+","+str(ln))
			outfile.close()
			
			nocaj=self.lcaj.text()
			
			outfile = open("/home/pi/Documents/NoCajero.txt", 'w')
			outfile.write(str(nocaj))
			outfile.close()
			host=self.lhost.text()
			ip=self.lip.text()
			
			self.sustituye("/home/pi/Documents/eum/app/cajeroF/cajero/cliente.py","192.168","	host = '"+host+"'")
			self.sustituye("/etc/dhcpcd.conf","ip_address","static ip_address="+ip+"/24")
			ip=ip.split(".")
			ip=ip[0]+"."+ip[1]+"."+ip[2]+".1"
			self.sustituye("/etc/dhcpcd.conf","routers","static routers="+ip)
			
			nom=self.lnom.text()
			loc=self.llol.text()
			self.cambia(9)
			consu="insert into \"USUARIO_LOG\"(usuario,log,detalle,fecha) values("+str(USUARIO)+",6,'"+str(nn)+","+str(ln)+"','"+fecha+"')"
			cur.execute(consu)
			conn.commit()


		def holi(self,val):
			print(val)
			if(val==3):
				self.lnom.setText("hola")
				self.llol.setText("")
			if(val==6):
				self.llol.setText("hola")
				self.lnom.setText("")


		def tecladoSum(self,val):
			if(val==10):
				self.valvol.setText("$")
			else:
				self.valvol.setText(self.valvol.text()+str(val))


		def volConfirmado(self):
			global aux_tarifa,cambio,aportacionConfirmada
			aportacionConfirmada=1
			if(self.valvol.text()=="$" or self.valvol.text()=="$0"):
				aux_tarifa=0
				#cambio=0
			else:
				valPropuesto=self.valvol.text()[1:]
				print("valvol: ",valPropuesto)
				aux_tarifa=int(self.valvol.text()[1:])
			self.stackedWidget.setCurrentIndex(1)
			"""if(valPropuesto!=0):
				print("ACA")
				self.alerta.setVisible(True)
			else:
				print("ALLA")
				aux_tarifa=int(self.valvol.text()[1:])
				self.stackedWidget.setCurrentIndex(1)"""







		def actualizaMensaje2(self):
			global cur
			vac=2
			idt=self.idtar1.value()
			cur.execute("select estado from \"TARIFA\" where \"idTarifa\"="+str(idt))
			for reg in cur:
				vac=reg[0]
				print(reg[0])
			if(vac==2):
				self.bquitar.setEnabled(False)
				self.bquitar.setText("No existente")
				print("K1",vac)
			else:
				self.bquitar.setEnabled(True)
				self.bquitar.setText("Eliminar")
				print("K2",vac)

		def actualizaMensaje(self):
			global cur
			vac=2
			idt=self.idtar2.value()
			cur.execute("select estado from \"TARIFA\" where \"idTarifa\"="+str(idt))
			for reg in cur:
				vac=reg[0]
				print(reg[0])
			if(vac==1):
				self.bhabilitar.setEnabled(True)
				self.bhabilitar.setText("Deshabilitar")
				print("simon1")
			if(vac==0):
				self.bhabilitar.setEnabled(True)
				self.bhabilitar.setText("Habilitar")

				print("simon0")
			if(vac==2):
				self.bhabilitar.setEnabled(False)
				self.bhabilitar.setText("No existente")
				print("simon2")



		def habilitaTarifa(self):
			global cur,conn,USUARIO
			idt=self.idtar2.value()
			fecha=hora.mostrarFechayHora()
			vac=0
			cur.execute("select estado from \"TARIFA\" where \"idTarifa\"="+str(idt))
			for reg in cur:
				vac=reg[0]
				print(reg[0])

			if(vac==0):

				cur.execute("update \"TARIFA\" set estado=1 where \"idTarifa\"="+str(idt))
				self.bhabilitar.setText("Deshabilitar")
				consu="insert into \"USUARIO_LOG\"(usuario,log,detalle,fecha) values("+str(USUARIO)+",1,'"+str(idt)+"','"+fecha+"')"
				cur.execute(consu)
				conn.commit()
			else:
				cur.execute("update \"TARIFA\" set estado=0 where \"idTarifa\"="+str(idt))
				self.bhabilitar.setText("Habilitar")
				consu="insert into \"USUARIO_LOG\"(usuario,log,detalle,fecha) values("+str(USUARIO)+",2,'"+str(idt)+"','"+fecha+"')"
				cur.execute(consu)
				conn.commit()


			self.llenaTabla()


		def seccionTarifas(self):
			global cur
			self.cambia(6)
			self.llenaTabla()

		def llenaTabla(self):
			global cur
			cur.execute("select * from \"TARIFA\" order by prioridad Desc")
			rowc=self.tablatarifas.rowCount()
			k=0
			while(k<rowc):
				self.tablatarifas.removeRow(0)
				#del self.CB2[0]
				k=k+1
			row=0
			for reg in cur:
				#print(reg[0],reg[1],reg[2],reg[3],reg[4],reg[5],reg[6],reg[7],reg[8],reg[9],reg[10],reg[11])
				self.tablatarifas.insertRow(row)
				idt=QTableWidgetItem(str(reg[0]))
				pri=QTableWidgetItem(str(reg[12]))
				fi=QTableWidgetItem(str(reg[2]))
				ff=QTableWidgetItem(str(reg[3]))
				hi=QTableWidgetItem(str(reg[4]))
				hf=QTableWidgetItem(str(reg[5]))
				ds=QTableWidgetItem(str(reg[6]))
				des=QTableWidgetItem(str(reg[7]))
				cos=QTableWidgetItem(str(reg[8]))
				i1=QTableWidgetItem(str(reg[9]))
				i2=QTableWidgetItem(str(reg[10]))
				if(reg[11]==1):
					state=QTableWidgetItem("Habilitada")
				else:
					state=QTableWidgetItem("Deshabilitada")
				self.tablatarifas.setItem(row,0,state)
				self.tablatarifas.item(row,0).setTextAlignment(4)

				self.tablatarifas.setItem(row,1,idt)
				self.tablatarifas.item(row,1).setTextAlignment(4)
				self.tablatarifas.setItem(row,2,pri)
				self.tablatarifas.item(row,2).setTextAlignment(4)
				self.tablatarifas.setItem(row,3,fi)
				self.tablatarifas.item(row,3).setTextAlignment(4)
				self.tablatarifas.setItem(row,4,ff)
				self.tablatarifas.item(row,4).setTextAlignment(4)
				self.tablatarifas.setItem(row,5,hi)
				self.tablatarifas.item(row,5).setTextAlignment(4)
				self.tablatarifas.setItem(row,6,hf)
				self.tablatarifas.item(row,6).setTextAlignment(4)
				self.tablatarifas.setItem(row,7,ds)
				self.tablatarifas.item(row,7).setTextAlignment(4)
				self.tablatarifas.setItem(row,8,des)
				self.tablatarifas.item(row,8).setTextAlignment(4)
				self.tablatarifas.setItem(row,9,cos)
				self.tablatarifas.item(row,9).setTextAlignment(4)
				self.tablatarifas.setItem(row,10,i1)
				self.tablatarifas.item(row,10).setTextAlignment(4)
				self.tablatarifas.setItem(row,11,i2)
				self.tablatarifas.item(row,11).setTextAlignment(4)
				row=row+1



		def elimina2(self):
			global cur,conn,USUARIO
			fecha=hora.mostrarFechayHora()
			idt=self.idtar1.value()
			print("Eliminado Caon")
			cur.execute("delete from \"TARIFA\" where \"idTarifa\"="+str(idt))
			consu="insert into \"USUARIO_LOG\"(usuario,log,detalle,fecha) values("+str(USUARIO)+",3,'"+str(idt)+"','"+fecha+"')"
			cur.execute(consu)
			conn.commit()
			self.llenaTabla()





		def tarifaConfirmada(self):
			global USUARIO
			fecha=hora.mostrarFechayHora()
			int1=""
			int2=""
			dia1=""
			mes1=""
			anio1=""
			dia2=""
			mes2=""
			anio2=""
			hora1=""
			minuto1=""
			hora2=""
			minuto2=""
			self.prioridad=0
			cons=""
			intok=""
			fecok=""
			horok=""
			dsemok=""
			costo=0
			dsem=""
			dsem2=""
			descr=""
			destar=""
			segundoIndicador=""

			print(cons)
			if(self.ch1.checkState()==2):
				self.prioridad=self.prioridad+1
				int1=","+str(self.i1.value())
				int2=","+str(self.i2.value())
				intok=",int_1,int_2"
				#segundoIndicador=segundoIndicador+"A"
			if(self.ch2.checkState()==2):
				self.prioridad=self.prioridad+1
				mes1=",'"+str(self.f1.date().month())
				dia1="/"+str(self.f1.date().day())
				anio1="/"+str(self.f1.date().year())
				mes2="','"+str(self.f2.date().month())
				dia2="/"+str(self.f2.date().day())
				anio2="/"+str(self.f2.date().year())+"'"
				fecok=",fec_ini,fec_fin"
				#segundoIndicador=segundoIndicador+"B"
			if(self.ch3.checkState()==2):
				self.prioridad=self.prioridad+1
				hora1=",'"+str(self.h1.time().hour())
				minuto1=":"+str(self.h1.time().minute())
				hora2="','"+str(self.h2.time().hour())
				minuto2=":"+str(self.h2.time().minute())+"'"
				horok=",hor_ini,hor_fin"
				#segundoIndicador=segundoIndicador+"C"
			if(self.ch4.checkState()==2):
				self.prioridad=self.prioridad+1
				dsem2=dsem2+",'"
				if(self.chlunes.checkState()==2):
					dsem=dsem+",lunes"
				if(self.chmartes.checkState()==2):
					dsem=dsem+",martes"
				if(self.chmiercoles.checkState()==2):
					dsem=dsem+",miercoles"
				if(self.chjueves.checkState()==2):
					dsem=dsem+",jueves"
				if(self.chviernes.checkState()==2):
					dsem=dsem+",viernes"
				if(self.chsabado.checkState()==2):
					dsem=dsem+",sabado"
				if(self.chdomingo.checkState()==2):
					dsem=dsem+",domingo"
				dsem=dsem.lstrip(",")
				dsem2=dsem2+dsem
				dsem2=dsem2+"'"
				#segundoIndicador=segundoIndicador+"D"





				dsem=dsem.rstrip(",")
				dsemok=",dia_sem"
				print(dsem)

			print(self.prioridad)

			#Determinando prioridad compuesta
			if(self.prioridad!=0):
				#self.prioridad=str(self.prioridad)+segundoIndicador+"'"
				self.prioridad=str(self.prioridad)+"'"
				cost=","+str(self.costo.value())
				descr=",'"+str(self.descripcion.toPlainText())+"'"
				archivo = open("/home/pi/Documents/NoCajero.txt", "r")
				idCajero=str(archivo.readline().rstrip("\n"))
				archivo.close()
				cur.execute("select * from \"CAJERO\" where \"idCajero\"=%s",(idCajero))
				for reg in cur:
					print(reg[0],reg[1])
				plaza=reg[1]


				cons="INSERT INTO \"TARIFA\" (prioridad,des_tar"+intok+fecok+horok+dsemok+",costo,estado,plaza) values ('"+str(self.prioridad)+descr+int1+int2+mes1+dia1+anio1+mes2+dia2+anio2+hora1+minuto1+hora2+minuto2+dsem2+cost+",1,"+str(plaza)+")"
				print("PK",cons)
				cur.execute(cons)
				conn.commit()

				cur.execute("select MAX(\"idTarifa\") from \"TARIFA\"")
				for reg in cur:
					idtar=reg[0]

				consu="insert into \"USUARIO_LOG\"(usuario,log,detalle,fecha) values("+str(USUARIO)+",7,'"+str(idtar)+"','"+fecha+"')"
				cur.execute(consu)
				conn.commit()
				self.cambia(6)
				self.llenaTabla()


		def saliendoAdmin(self):
			global config
			self.stackedWidget.setCurrentIndex(0)
			config=0
			self.lusu.setText('')
			self.lcont.setText('')
			fecha=hora.mostrarFechayHora()
			self.lmodelo.setVisible(False)
			self.lserie.setVisible(False)

		def obtenerDineroActual(self):
			global monedas,billetes
			descripcionMonedas=str(monedas[0])+":1;"+str(monedas[1])+":2;"+str(monedas[2])+":5;"+str(monedas[3])+":10"
			descripcionBilletes=str(billetes[0])+":20;"+str(billetes[1])+":50;"+str(billetes[2])+":100;"+str(billetes[3])+":200"
			return descripcionMonedas,descripcionBilletes

		def cortandoLaCaja(self):
			global accesoAcaja,correoUSUARIO,contadorCartuchos,monedas,monedasTotal,dineroTotal,dineroTotalB,billetesTotales,billetes,NoCajero
			fecha=hora.mostrarFechayHora()
			i=-1
			descripciones=self.obtenerDineroActual()
			mensaje=str(correoUSUARIO)+","+str(NoCajero)+",1,"+descripciones[0]+","+descripciones[1]
			resultado=Servidor.configSocket("log inicial", mensaje)
			if(resultado==-1):
				self.lerror1.setText("Problema en la conexion")
				self.lerror1.setVisible(True)
			else:
				accesoAcaja=1
				botones.abrirPuerta()
				self.cambia(3)
				botones.abrirPuerta()
				self.m1.setText(str(monedas[0]))
				self.m2.setText(str(monedas[1]))
				self.m5.setText(str(monedas[2]))
				self.m10.setText(str(monedas[3]))
				self.mt.setText(str(monedas[0]+monedas[1]+monedas[2]+monedas[3]))
				self.b20.setText(str(billetes[0]))
				self.b50.setText(str(billetes[1]))
				self.b100.setText(str(billetes[2]))
				self.b200.setText(str(billetes[3]))
				self.bt.setText(str(billetes[0]+billetes[1]+billetes[2]+billetes[3]))
				self.dm.setText(str(dineroTotal))
				self.db.setText(str(dineroTotalB))
				self.dt.setText(str(dineroTotal+dineroTotalB))
				self.imprimeReporte()
				consu="insert into \"USUARIO_LOG\"(usuario,log,detalle,fecha) values("+str(USUARIO)+",4,'CC','"+fecha+"')"
				cur.execute(consu)
				conn.commit()
				monedas=[85,78,69,58]
				monedasTotal=290
				dineroTotal=1166
				dineroTotalB=0
				billetesTotales=0
				billetes=[0,0,0,0]
				contadorCartuchos=1

		def generaReporte(self):
			global config
			self.stackedWidget.setCurrentIndex(0)
			config=0

		def boletoPerdido(self):
			global mensajeBoletoPerdido
			mensajeBoletoPerdido=1

		def montos(self):
			global cp,registraPago,comienzaLectura,comienzaCambio,NoCajero,cajeroSuspendido,suspenderCajero,w,conteoPantallaPrincipal,inicioPago,imprime,cambiaColor,nom,loc,nivelDeCambio,cambio,leido,total,aux_cambio,aux_cambio1,pagado,config,monedas,monedasTotal,dineroTotal,avis,dineroTotalB,billetesTotales,billetes,tarifaVoluntaria,mensajeBoletoUsado,mensajeBoletoPerdido,mostrarTiempoDeSalidaRestante,mensajeError,mensajeAyuda
			#self.cambio.display(aux_cambio)
			self.lcobrar.setText("$"+str(aux_tarifa))
			self.ldepositar.setText("$"+str(total))
			#self.fol.setText(fo)
			#self.pen.setText(pe)
			self.he.setText(hh)
			self.hs.setText(hsalida)
			self.ttotal.setText(aux_dif)
			self.he2.setText(hh)
			self.hs2.setText(hsalida)
			self.ttotal2.setText(aux_dif)

			#self.nomPlaza.setText(nom)
			#self.nomLoc.setText(loc)
			#self.nomPlaza_2.setText(nom)
			#self.nomLoc_2.setText(loc)

			#self.aviso.setText(str(avis))
			if(cambiaColor==1):
				cambiaColor=0
				self.gdepositar.setStyleSheet("background-color: rgb(48, 48, 48,80%);")
				self.gfp.setStyleSheet("background-color: rgb(48, 48, 48,80%);border-radius:10%;")
				self.gp.setStyleSheet("background-color:rgb(101, 179, 0);border-radius:10%;")
				self.gav.setStyleSheet("background-color:rgb(101, 179, 0);border-radius:10%;")

			if(leido == 1):
				#DESHABILITAR CAJERO LUEGO DE UN TIEMPO
				#inicioPago=1
				self.stackedWidget.setCurrentIndex(1)
				comienzaLectura=1

				leido = 0
				
				
			if(comienzaCambio==1):
				
				"""self.gcambio.setStyleSheet("background-color:rgb(17, 58, 8);")
				time.sleep(.2)
				self.gcambio.setStyleSheet("background-color:rgb(27, 68, 18);")
				time.sleep(.2)
				self.gcambio.setStyleSheet("background-color:rgb(37, 78, 28);")
				self.gcambio.setStyleSheet("background-color:rgb(47, 88, 38);")
				self.gcambio.setStyleSheet("background-color:rgb(57, 98, 48);")
				self.gcambio.setStyleSheet("background-color:rgb(67, 10, 58);")
				time.sleep(.2)
				self.gcambio.setStyleSheet("background-color:rgb(67, 10, 58);")
				time.sleep(.2)
				self.gcambio.setStyleSheet("background-color:rgb(77, 118, 68);")
				self.gcambio.setStyleSheet("background-color:rgb(87, 128, 78);")
				time.sleep(.2)
				self.gcambio.setStyleSheet("background-color:rgb(97, 138, 88);")
				self.gcambio.setStyleSheet("background-color:rgb(107, 148, 98);")
				self.gdepositar.setStyleSheet("background-color:rgb(255, 255, 255);")
				self.lcobrar.setStyleSheet("background-color:rgb(255, 255, 255);")"""
				#pagado=1
				pass
			if(cajeroSuspendido==1):
				self.stackedWidget.setCurrentIndex(14)
				cajeroSuspendido=0
				
				
			if(pagado==1):
				
				pagado=0
			
			if(pagado==2):
				pagado=0
				if(cajeroSuspendido==1):
					self.stackedWidget.setCurrentIndex(14)
					conteoPantallaPrincipal=1
					inicioPago=0
					w=0
				else:
					if(cp==1):
						self.stackedWidget.setCurrentIndex(13)
					else:
						self.stackedWidget.setCurrentIndex(2)
					conteoPantallaPrincipal=1
					inicioPago=0
					w=0
			if(config==1):
				config=2
				self.lmodelo.setVisible(False)
				self.lserie.setVisible(False)
				self.stackedWidget.setCurrentIndex(9)

			if(mostrarTiempoDeSalidaRestante[0]==1):
				self.avisoInserta.setText("El pago expira en "+mostrarTiempoDeSalidaRestante[1]+" minutos")

			if(mensajeBoletoUsado==1):
				self.avisoInserta.setText("Este boleto ya fue usado")

			if(mensajeBoletoPerdido==1):
				self.avisoInserta.setText("Acude a atencion a clientes")

			if(mensajeError==1):
				self.avisoInserta.setText("Lo sentimos, intentelo de nuevo")

			if(mensajeAyuda==1):
				self.avisoInserta.setText("Tu peticion esta siendo procesada")
				self.bayudaCliente.setEnabled(False)
				self.bayudaCliente2.setEnabled(False)

			if(nivelDeCambio!=0):
				self.aviso2.setText("No cuento con mucho cambio")
				#self.gav.setStyleSheet("background-color: rgb(134, 0, 0);border-radius:10%;")
				
			if(nivelDeCambio==0):
				self.aviso2.setText("")
				#self.gav.setStyleSheet("background-color:rgb(101, 179, 0);border-radius:10%;")
			if(tarifaVoluntaria==1):
				os.system("wmctrl -a 'Dialog'")
				self.stackedWidget.setCurrentIndex(8)
				self.valvol.setText("$")
				tarifaVoluntaria=0

			QtCore.QTimer.singleShot(5,self.montos)

			if(self.chtodos.checkState()==2):
				self.chlunes.setCheckState(2)
				self.chmartes.setCheckState(2)
				self.chmiercoles.setCheckState(2)
				self.chjueves.setCheckState(2)
				self.chviernes.setCheckState(2)
				self.chsabado.setCheckState(2)
				self.chdomingo.setCheckState(2)

			if(self.ch1.checkState()==2):
				self.i1.setEnabled(True)
				self.i2.setEnabled(True)
			if(self.ch1.checkState()==0):
				self.i1.setEnabled(False)
				self.i2.setEnabled(False)
			if(self.ch2.checkState()==2):
				self.f1.setEnabled(True)
				self.f2.setEnabled(True)
			if(self.ch2.checkState()==0):
				self.f1.setEnabled(False)
				self.f2.setEnabled(False)
			if(self.ch3.checkState()==2):
				self.h1.setEnabled(True)
				self.h2.setEnabled(True)
			if(self.ch3.checkState()==0):
				self.h1.setEnabled(False)
				self.h2.setEnabled(False)
			if(self.ch4.checkState()==2):
				self.chtodos.setEnabled(True)
				self.chlunes.setEnabled(True)
				self.chmartes.setEnabled(True)
				self.chmiercoles.setEnabled(True)
				self.chjueves.setEnabled(True)
				self.chviernes.setEnabled(True)
				self.chsabado.setEnabled(True)
				self.chdomingo.setEnabled(True)
			if(self.ch4.checkState()==0):
				self.chtodos.setEnabled(False)
				self.chlunes.setEnabled(False)
				self.chmartes.setEnabled(False)
				self.chmiercoles.setEnabled(False)
				self.chjueves.setEnabled(False)
				self.chviernes.setEnabled(False)
				self.chsabado.setEnabled(False)
				self.chdomingo.setEnabled(False)
			#botones.manteniendoElCero()



		def contadorSegundos(self):
			global cp,varc,comienzaCambio,cajeroSuspendido,suspenderCajero,tarifasAplicadas,ma,preguntarPorEstado,accesoAcaja,c,conteoPantallaPrincipal,aux_cambio,cambio,total,w,killer,aux_tarifa,inicioPago,tiempoAgotadoDePago,cs2,cs1,v,a,p,q,y,z,mostrarTiempoDeSalidaRestante,mensajeBoletoPerdido,mensajeBoletoUsado,mensajeError,mensajeAyuda
			#QtCore.QTimer.singleShot(1000,self.contadorSegundos)
			
			fehoy=str(datetime.now().date()).split('-',2)
			fehoy=fehoy[2]+"/"+fehoy[1]+"/"+fehoy[0]
			#self.ldate.setText(fehoy)
			self.ldate2.setText(fehoy)
			#self.ltime.setText(time.strftime("%H:%M:%S"))
			self.ltime2.setText(time.strftime("%H:%M:%S"))
			
			if(suspenderCajero==1):
				cs2=cs2+1
				if(cs2==7): #3 MINUTOS TOLERANCIA
					cs2=0
					suspenderCajero=0
					cajeroSuspendido=1
					
			if(preguntarPorEstado==0):
				cs1=cs1+1
				if(cs1==1): #3 MINUTOS TOLERANCIA
					cs1=0
					preguntarPorEstado=1
			if(mensajeError==1):
				v=v+1
				if(v==3): #3 MINUTOS TOLERANCIA
					v=0
					mensajeError=0
					self.avisoInserta.setText("---> Inserta tu boleto <---")

			if(mensajeAyuda==1):
				ma=ma+1
				if(ma==3): #3 MINUTOS TOLERANCIA
					ma=0
					mensajeAyuda=0
					self.bayudaCliente.setEnabled(True)
					self.bayudaCliente2.setEnabled(True)
					#botones.prenderMonedero()
					self.avisoInserta.setText("---> Inserta tu boleto <---")

			if(mensajeBoletoUsado==1):
				p=p+1
				if(p==3): #3 MINUTOS TOLERANCIA
					p=0
					mensajeBoletoUsado=0
					self.avisoInserta.setText("---> Inserta tu boleto <---")

			if(mensajeBoletoPerdido==1):
				c=c+1
				if(c==3): #3 MINUTOS TOLERANCIA
					c=0
					mensajeBoletoPerdido=0
					self.avisoInserta.setText("---> Inserta tu boleto <---")

			if(mostrarTiempoDeSalidaRestante[0]==1):
				q=q+1
				if(q==3): #3 MINUTOS TOLERANCIA
					q=0
					mostrarTiempoDeSalidaRestante[0]=0
					self.avisoInserta.setText("---> Inserta tu boleto <---")

			if(inicioPago==1):
				w=w+1
				if(w==300): #3 MINUTOS TOLERANCIA
					w=0
					tiempoAgotadoDePago=1
					inicioPago=0
					aux_tarifa = 0
					aux_tarifa1 = 0
					total = 0
					aux_tarifa=0
					aux_cambio=0
					registraPago=0
					tarifasAplicadas=""
					self.aviso1.setText("")
					self.stackedWidget.setCurrentIndex(0)
					leerArch = open("/home/pi/Documents/ticket.txt", "w")
					leerArch.write('')
					leerArch.close()
					killer=0
			if(conteoPantallaPrincipal == 1):
				y=y+1
				if(y==4):
					y=0
					conteoPantallaPrincipal=0
					aux_tarifa = 0
					aux_tarifa1 = 0
					total = 0
					cp=0
					self.lscan.setText('')
					registraPago=0
					aux_tarifa=0
					aux_cambio=0
					tarifasAplicadas=""
					self.aviso1.setText("")
					self.lcambio.setText("$0")
					os.system("wmctrl -a 'zbar'")
					#self.labelCambio.setText("$0")
					if(cajeroSuspendido==1):
						self.stackedWidget.setCurrentIndex(14)
					else:
						self.stackedWidget.setCurrentIndex(0)
					leerArch = open("/home/pi/Documents/ticket.txt", "w")
					leerArch.write('')
					leerArch.close()
					killer=0

			if(accesoAcaja==1):
				z=z+1
				if(z==60):
					z=0
					accesoAcaja=0
					botones.cerrarPuerta()

			QtCore.QTimer.singleShot(1000,self.contadorSegundos)
			
		def contadorMiliSegundos(self):
			global varl,comienzaCobro,comienzaCambio,varc,red,green,blue,leido,comienzaLectura,rrr
			
			if(comienzaLectura==1):
				self.aviso1.setText("")
				varl=varl+1
				if(red<59):
					rrr=1
				if(red>150):
					rrr=0
				if(rrr==0):
					red=red-10
					green=green-10
					blue=blue-10
				else:
					red=red+5
					green=green+5
					blue=blue+5
				self.gcambio.setStyleSheet("background-color:rgb(220, 220, 220);color:rgb(105,105,105);")
				self.lcambio.setStyleSheet("background-color:rgb(220, 220, 220);color:rgb(105,105,105);")
				#self.gcobrar.setStyleSheet("background-color:rgb("+str(red)+", "+str(green)+", "+str(blue)+");")
				self.lcobrar.setStyleSheet("color:rgb("+str(red)+", "+str(green)+", "+str(blue)+");")
				#self.lcobrar.setStyleSheet("background-color:rgb("+str(red)+", "+str(green)+", "+str(blue)+");")
				#print("red",red,green,blue)
				#self.gcambio.setStyleSheet("background-color:rgb(107, 148, 98);")
				if(varl==30):
					varl=0
					
			if(comienzaCobro==1):
				self.aviso1.setText("")
				comienzaLectura=0
				varl=varl+1
				if(red<59):
					rrr=1
				if(red>105):
					rrr=0
				if(rrr==0):
					red=red-5
					green=green-5
					blue=blue-5
				else:
					red=red+5
					green=green+5
					blue=blue+5
				"""self.gcobrar.setStyleSheet("background-color:rgb(220, 220, 220);")
				self.lcobrar.setStyleSheet("background-color:rgb(220, 220, 220);")
				self.gdepositar.setStyleSheet("background-color:rgb("+str(red)+", "+str(green)+", "+str(blue)+");")
				self.ldepositar.setStyleSheet("background-color:rgb("+str(red)+", "+str(green)+", "+str(blue)+");")
				"""
				self.gcobrar.setStyleSheet("background-color:rgb(220, 220, 220);")
				self.lcobrar.setStyleSheet("background-color:rgb(220, 220, 220);color:rgb(105,105,105);")
				self.ldepositar.setStyleSheet("color:rgb("+str(red)+", "+str(green)+", "+str(blue)+");")
				#print("red",red,green,blue)
				#self.gcambio.setStyleSheet("background-color:rgb(107, 148, 98);")
				if(varl==30):
					varl=0
					
			
					
					
			
			if(comienzaCambio==1):
				comienzaLectura=0
				comienzaCobro=0
				self.aviso1.setText("Espere su cambio... "+str(aux_cambio))
				#self.labelCambio.setText("$"+str(aux_cambio))
				self.lcambio.setText("$"+str(aux_cambio))
				varc=varc+1
				if(red<59):
					rrr=1
				if(red>105):
					rrr=0
				if(rrr==0):
					red=red-5
					green=green-5
					blue=blue-5
				else:
					red=red+5
					green=green+5
					blue=blue+5
				"""self.gdepositar.setStyleSheet("background-color:rgb(220, 220, 220);")
				self.ldepositar.setStyleSheet("background-color:rgb(220, 220, 220);")
				self.gcobrar.setStyleSheet("background-color:rgb(220, 220, 220);")
				self.lcobrar.setStyleSheet("background-color:rgb(220, 220, 220);")
				self.gcambio.setStyleSheet("background-color:rgb("+str(red)+", "+str(green)+", "+str(blue)+");")
				self.lcambio.setStyleSheet("background-color:rgb("+str(red)+", "+str(green)+", "+str(blue)+");")"""
				self.gdepositar.setStyleSheet("background-color:rgb(220, 220, 220);color:rgb(105,105,105);")
				self.ldepositar.setStyleSheet("background-color:rgb(220, 220, 220);color:rgb(105,105,105);")
				self.gcobrar.setStyleSheet("background-color:rgb(220, 220, 220);color:rgb(105,105,105);")
				self.lcobrar.setStyleSheet("background-color:rgb(220, 220, 220);color:rgb(105,105,105);")
				self.lcambio.setStyleSheet("color:rgb("+str(red)+", "+str(green)+", "+str(blue)+");")
				self.aviso1.setStyleSheet("color:rgb("+str(red)+", "+str(green)+", "+str(blue)+");")
				self.avisoInserta_2.setStyleSheet("color:rgb("+str(red)+", "+str(green)+", "+str(blue)+");")
				
				#print("red",red)
				#self.gcambio.setStyleSheet("background-color:rgb(107, 148, 98);")
				if(varc==10):
					varc=0
					pagado=1
					#red=17
					#green=58
					#blue=8
			if(aux_tarifa==0):
				comienzaCambio=0
				varl=varl+1
				if(red<50):
					rrr=1
				if(red>150):
					rrr=0
				if(rrr==0):
					red=red-10
					green=green-10
					blue=blue-10
				else:
					red=red+10
					green=green+10
					blue=blue+10
				
				#self.gbol.setStyleSheet("background-color:rgb("+str(red)+", "+str(green)+", "+str(blue)+");")
				#self.avisoInserta.setStyleSheet("background-color:rgb("+str(red)+", "+str(green)+", "+str(blue)+");")
				self.avisoInserta.setStyleSheet("color:rgb("+str(red)+", "+str(green)+", "+str(blue)+");background-color:transparent;")
				#print("red",red)
			QtCore.QTimer.singleShot(.005,self.contadorMiliSegundos)
			


		def actualiza(self,val):
			print(val)

		def cambia(self,num):
			self.stackedWidget.setCurrentIndex(num)



	app = QApplication(sys.argv)
	_ventana = Ventana()
	_ventana.show()
	app.exec_()



def restar_hora(horab,fechab):
		global aux_dif
		"""formato = "%H:%M:%S"
		h1 = datetime.strptime(hora1, formato)
		h2 = datetime.strptime(hora2, formato)
		resultado = h1 - h2
		aux_dif=str(resultado)
		print("res:",h1,h2,resultado,type(str(resultado)))
		return str(resultado)"""
		fechaBoleto = datetime.strptime(str(fechab[0]) + str(fechab[1]) + str(fechab[2]), '%Y%m%d').date()
		horaBoleto = datetime.strptime(str(horab[0]) +':'+str(horab[1]) +':'+ str(horab[2]), '%H:%M:%S').time()
		fechaActual=datetime.now().date()
		horaActual=datetime.now().time()
		horayFechaBoleto = datetime.now().combine(fechaBoleto, horaBoleto)
		horayFechaActual = datetime.now().combine(fechaActual, horaActual)
		restaFechas = horayFechaActual - horayFechaBoleto
		aux_dif=(str(restaFechas).split('.',1))[0]
		dias = int(restaFechas.days)
		horas = int(restaFechas.seconds / 3600)
		print("****RES:",restaFechas)
		return dias,horas



def calculaTarifa(tiempoEstacionado,descuento):
	global costillo,tarifa,aux_tarifa,aux_tarifa1,aux_dif,tarifaVoluntaria,tarifaSeleccionada
	aplicaDescuento=0
	indicador=0
	costillo=0
	horasRestantes=0
	dicdias = {'MONDAY':'lunes','TUESDAY':'martes','WEDNESDAY':'miercoles','THURSDAY':'jueves','FRIDAY':'viernes','SATURDAY':'sabado','SUNDAY':'domingo'}
	fechaActual = datetime.now().date()
	tiempoActual = datetime.now().time()
	#print("222",ahora,ahora2)
	t=time.localtime()
	dias=time.strftime("%A",t)
	diaDeLaSemana=dicdias[dias.upper()]
	print("cuatro datos:)----->",fechaActual,tiempoActual,tiempoEstacionado,diaDeLaSemana)
	print("El descuento ES:::::::::",descuento,type(descuento))
	if(descuento==1):
		print("-.-.-.NO DESCUENTO",descuento)
		#cur.execute("select * from \"TARIFA\" where estado=1 order by costo Asc")
		cur.execute("select * from \"TARIFA\" where estado=1 and descuento=%s order by prioridad Desc",(str(descuento)))
	else:
		print("-.-.-.SI DESCUENTO",descuento)
		cur.execute("select * from \"TARIFA\" where estado=1 and descuento=%s order by prioridad Desc",(str(descuento)))
		#aplicaDescuento=1


	for reg in cur:
		print(reg[0],reg[1],reg[2],reg[3],reg[4],reg[5],reg[6],reg[7],reg[8],reg[9],reg[10],reg[11])
		if(str(reg[2])!="None"):
			if(fechaActual>=reg[2] and fechaActual<=reg[3]):
				print("FECHA ENTRA")
			else:
				indicador=indicador+1
		if(str(reg[4])!="None"):
			if(tiempoActual>=reg[4] and tiempoActual<=reg[5]):
				print("HORA ENTRA")
			else:
				indicador=indicador+1

		if(str(reg[6])!="None"):
			if(diaDeLaSemana in str(reg[6])):
				print("Dia de la semana entra")
			else:
				indicador=indicador+1

		if(str(reg[9])!="None"):
			if(tiempoEstacionado>=int(reg[9]) and tiempoEstacionado<int(reg[10])):
				print("INTERVALO ENTRA")
			else:
				indicador=indicador+1

		print("!!!!!",indicador)
		if(aplicaDescuento==1):
			indicador=0
		if(indicador==0):
			aplicaDescuento=0
			cantidadDeHor=reg[10]
			horasRestantes=tiempoEstacionado-cantidadDeHor
			tarifaSeleccionada=reg[0]
			costillo=reg[8]
			break
		else:
			indicador=0



	print("costillo=",costillo)
	if(costillo!=0):
		aux_tarifa=aux_tarifa+costillo
	else:
		print("NO SE APLICO NINGUNA TARIFA")
		#aux_tarifa=0
		tarifaVoluntaria=1
	print(aux_tarifa)
	print("respuesta: ")
	return tarifaSeleccionada,horasRestantes


def buscaCamara():
	global camInicial
	while(1):
		lee2 = os.system("sudo find /dev -name 'video*' > cam.txt")
		a = open("cam.txt", "r")
		cam=(a.readline().rstrip("\n")).lstrip("\x00")
		a.close()
		a = open("cam.txt", "w")
		a.write('')
		#time.sleep(1)
		#print('Cammmmmmmmm',cam,camInicial)
		if(cam!=camInicial):
			#print('Camara desconectadaaaaaaaaa')
			os.system("sudo pkill zbarcam")

def leerArchivo():
	global aportacionConfirmada,tarifaVoluntaria,cajeroSuspendido,preguntarPorEstado,leido,fo,pe,fe,hh,hsalida,kill,killer,killbill,config,fechaAMD,nivelDeCambio,h,nivelActual,aux_tarifa,imprime,NoCajero,tarifaSeleccionada,mostrarTiempoDeSalidaRestante,mensajeBoletoPerdido,mensajeBoletoUsado,tarifasAplicadas,mensajeError
	tarifaSeleccionada=0
	A=0
	mixer.init()
	mixer.music.load('/home/pi/Downloads/beep-08b.wav')
	while(kill == 0):
		#if(imprime==1):
		if(imprime==5):
			#imp()
			fe=fe+" "+hh
			fec=datetime.now().date()
			fec=str(fec.day)+"/"+str(fec.month)+"/"+str(fec.year)+','+hh+','+str(aux_tarifa)+','+fo+','+pe
			leerArch = open("/home/pi/Documents/pago.txt", "a+")
			leerArch.write(fec)
			leerArch.close()
			os.system("sudo python3 /home/pi/Documents/cajero/archimp.py")
			
			#REGISTRA BOLETO EN BD.......
		#	consu="insert into \"BOLETO\"(tarifa,cajero,tipo,estado,pago,expedidora,\"fechaExpedicion\") values("+str(tarifaSeleccionada)+","+str(NoCajero)+",1,2,1,'"+str(pe)+"','"+fe+"')"
			#cur.execute(consu)
			#conn.commit()

			imprime=0


		while(killer == 0 and kill == 0):
			leerArch = open("/home/pi/Documents/ticket.txt", "r")
			folio=leerArch.readline().rstrip("\n")
			#time.sleep(.2)
			if(folio != ''):
				print("{}  ==  {}".format(folio,"Estacionamientos unicos de Mexico"))
				#booleana=str("Estacionamientos unicos de Mexico") in str(folio)
				booleana=str("M") in str(folio)
				booleana2=str("M") in str(folio)
				if(booleana):
					#os.system('sudo python3 /home/pi/scanner/buz.py')
					#mixer.music.play()
					#time.sleep(1)
					mixer.init()
					mixer.music.load('/home/pi/Downloads/beep-08b.wav')
					mixer.music.play()
					
					print(folio)
					if(folio == 'boleto perdido'):
						leerArch.close()
						leerArch = open("/home/pi/Documents/ticket.txt", "w")
						leerArch.write('')
						leerArch.close()

						cur.execute("select * from \"TARIFA\" where des_tar='boleto perdido' order by prioridad Desc")
						for reg in cur:
							print(reg[0],reg[1],reg[2],reg[3],reg[4],reg[5],reg[6],reg[7],reg[8],reg[9],reg[10],reg[11])
							if(str(reg[7])=="boleto perdido"):
								aux_tarifa=reg[8]
								leido = 1
								enable_coin(ser)
								enable_sequence(ser)
								killbill = 0
								billf()
					else:

						#impresora.imprimirBoletoC2("12/12/17","02:00:00",9)
						killer = 1
						leerArch.close()
						leerArch = open("/home/pi/Documents/ticket.txt", "r")
						leyenda=(leerArch.readline().rstrip("\n")).lstrip("\x00")
						folio=(leerArch.readline().rstrip("\n")).lstrip("\x00")
						inTerminal=leerArch.readline().rstrip("\n")
						inFecha=leerArch.readline().rstrip("\n")
						inHora=leerArch.readline().rstrip("\n")
						readQR = []
						readQR.append(folio)
						readQR.append(inTerminal)
						readQR.append(inFecha)
						readQR.append(inHora)
						print(readQR,"len=",readQR.__len__())
						fo=readQR[0]
						pe=readQR[1]
						hh=readQR[3]
						hsalida=hora.mostrarHoraSinFormato()[0]+":"+hora.mostrarHoraSinFormato()[1]+":"+hora.mostrarHoraSinFormato()[2]
						h=readQR[3].rstrip("\n")
						fe = readQR[2].rstrip("\n")
						#Se obtiene hora actual
						
						"""
						#####CONVERSON DATASYMBOL
						fo=fo.split(",")
						rango=range(0,len(fo))
						for x in rango:
							if("*" not in str(fo[x])):
								fol=fo[x]
								
						pe=pe.split(",")
						rango=range(0,len(pe))
						for x in rango:
							if("*" not in str(pe[x])):
								exp=pe[x]
								break
								
						h=h.split(",")
						rango=range(0,len(h))
						for x in rango:
							if("*" not in str(h[x])):
								horaBol=h[x]
								break
								
						fe=fe.split(",")
						rango=range(0,len(fe))
						for x in rango:
							if("*" not in str(fe[x])):
								fechaBol=fe[x]
								break
								
								
						fo=fol
						pe=exp
						hh=horaBol
						hsalida=hora.mostrarHoraSinFormato()[0]+":"+hora.mostrarHoraSinFormato()[1]+":"+hora.mostrarHoraSinFormato()[2]
						h=horaBol
						fe = fechaBol
						#####FIN CONVERSION
						"""
						print(h)
						leerArch.close()
						leerArch = open("/home/pi/Documents/ticket.txt", "w")
						leerArch.write('')
						leerArch.close()
						print("FEEEE>>>>>",fo)
						#Verificar nivel de cambio
						while(1):
							print(ser.inWaiting())
							ser.flushOutput()
							ser.flushInput()
							time.sleep(.1) #Para completar los 500 ms
							ser.parity = change_parity(0x0A, 1)
							ser.write(bytes([10]))
							ser.parity = change_parity(0x0A, 0)
							ser.write(bytes([10]))
							time.sleep(.1)
							r = ser.read(18) #Verificar en el simulador se ven 19
							if(r):
								print("h", r)
								if (r[0] == 0):
									nivelActual[0]=r[4]
									nivelActual[1]=r[5]
									nivelActual[2]=r[6]
									nivelActual[3]=r[7]

									#Si el nivel es bajo , se muestra advertencia en pantalla

									if(r[4]<20):
										nivelDeCambio=1
									elif(r[5]<20):
										nivelDeCambio=1
									elif(r[6]<20):
										nivelDeCambio=1
									elif(r[7]<20):
										nivelDeCambio=1
									else:
										nivelDeCambio=0
									
									if(nivelDeCambio!=0):
										mensaje=str("ayuda@ayuda.com")+","+str(NoCajero)+",3,"+"Cambio bajo"+","+"0:0"
										resultado=Servidor.configSocket("log inicial", mensaje)
									

									##Si el nivel es muy bajo , se muestra advertencia en pantalla

									if(r[4]<10):
										suspenderCajero=1
									elif(r[5]<10):
										suspenderCajero=1
									elif(r[6]<10):
										suspenderCajero=1
									elif(r[7]<10):
										suspenderCajero=1
									else:
										pass



										
									ser.parity = change_parity(0x00, 0)
									ser.write(b'\x00')
									break

						if(str("Admin") in str(fo)):
						#if(int(fo)==1566):

							print("Modo admin ON")
							config=1
							while(config!=0):
								if(preguntarPorEstado==1):
									monitorearChanger()
									preguntarPorEstado=0
								time.sleep(.5)
								killer=0
							print("Modo admin OFF")
							break

							#	time.sleep(0.005)
							#Init(ser)
							#return
						else:
							if(cajeroSuspendido==1):
								A=-1
								#self.cambia(13)
								pass
							else:
								h1=str(hora.mostrarHoraSinFormato()[0])+":"+str(hora.mostrarHoraSinFormato()[1])+":"+str(hora.mostrarHoraSinFormato()[2])
								#Se obtiene la cantidad de horas y minutos que el cliente estuvo en el estacionamiento
								horaBoleto=h.split(':',2)
								fechaAMD=fe.split('-',2)
								print("fechas----->",fe,fechaAMD)
								fechaAMD=fechaAMD[2]+"-"+fechaAMD[1]+"-"+fechaAMD[0]
								mensaje = str(fo) + "," + str(pe) + "," + fechaAMD +" "+h
								print(mensaje,type(mensaje))
								#return 2
								resultado=Servidor.configSocket("informacion boleto", mensaje)

								if(resultado==-1):
									print("ERROR EN LA COMUNICACION")
									A=-1
									mensajeError=1
								else:
									estadoBoleto=int(resultado[1])#ESTADO=2,FECHA=MINUTOS RESTANTES PARA SALIR....E=4,F=NULL,D=0....E=1,COBRAR NORMAL....
									descuento=int(resultado[0])
									fechaBoleto=resultado[2]
									print(fechaAMD,horaBoleto)
									dh=restar_hora(horaBoleto,fechaAMD.split('-'))
									#ESTE IF ES PARA APLICAR TARIFA MAXIMA
									dias=dh[0]
									horas=dh[1]
									tiempoEstacionado=horas
									if(dias!=0):
										tiempoEstacionado=15
									if(descuento==2):
										A=0
										respuesta=calculaTarifa(tiempoEstacionado,2)
										tarifasAplicadas=tarifasAplicadas+str(respuesta[0])
									elif(int(estadoBoleto)==1):
										A=0
										print("<<<<>>>> DIAS, TE , Estado B,descuento :",dias,tiempoEstacionado,estadoBoleto,descuento)
										#BOLETO NO PAGADO, SI PAGADO=AUN TIENES TIEMPO X PARA SALIR, TIEMPO EXCEDIDO, BOLETO USADO
										respuesta=calculaTarifa(tiempoEstacionado,descuento)
										tarifasAplicadas=tarifasAplicadas+str(respuesta[0])
										print(tarifasAplicadas)
										if(respuesta[1]<0):
											print("respuesta de tarifa =",respuesta)
										else:
											segundaRespuesta=calculaTarifa(respuesta[1],1)
											tarifasAplicadas=tarifasAplicadas+";"+str(segundaRespuesta[0])
									elif(int(estadoBoleto)==2):
										A=-1
										mostrarTiempoDeSalidaRestante[0]=1
										mostrarTiempoDeSalidaRestante[1]=str(resultado[2])
									elif(int(estadoBoleto)==3):
										A=0
										fechaBoleto=fechaBoleto.split(" ",1)
										fechaAMD=fechaBoleto[0].split('-',2)
										fechaAMD=fechaAMD[0]+"-"+fechaAMD[1]+"-"+fechaAMD[2]
										#fechaAMD=fechaAMD[2]+"-"+fechaAMD[1]+"-"+fechaAMD[0]
										print(fechaBoleto[1].split(':',2),fechaAMD)
										dh2=restar_hora(fechaBoleto[1].split(':',2),fechaAMD.split('-'))
										dias=dh2[0]
										horas=dh2[1]
										if(dias!=0):
											tiempoEstacionado=23
										tiempoEstacionado=horas
										r=calculaTarifa(tiempoEstacionado,1)
										tarifasAplicadas=str(r[0])
									elif(int(estadoBoleto)==4):
										A=-1
										mensajeBoletoUsado=1
									elif(int(estadoBoleto)==5):
										A=0
										respuesta=calculaTarifa(tiempoEstacionado,1)
										tarifasAplicadas=tarifasAplicadas+str(respuesta[0])
								#A=calculaTarifa(tiempoEstacionado)

								#A=calculaTarifa("10:01:00")
						if(A!=-1):
							print("Iniciando cobro....",aux_tarifa,tarifasAplicadas)
							while(aux_tarifa==0):
								time.sleep(.5)
								if(aportacionConfirmada==1):
									aportacionConfirmada=0
									
									break
							
							if(aux_tarifa==0):
								count(ser)
							else:
								leido = 1
								os.system("wmctrl -a 'Dialog'")
								enable_coin(ser)
								enable_sequence(ser)
								killbill = 0
								billf()
								
							
						else:
							killer=0

				else:
					leerArch.close()
					leerArch = open("/home/pi/Documents/ticket.txt", "w")
					leerArch.write('')
					leerArch.close()
			else:
				leerArch.close()
				#time.sleep(.5)


def billf():
	global tarifaVoluntaria,cp,tiempoAgotadoDePago,cambiaColor,total,bill,cambio,tarifa,aux_cambio,aux,rep,estatus,ser,killbill,aux_tarifa,bill,pagado,billetesTotales,dineroTotal,billetes,dineroTotalB,billetesPago

	print("Otra y otra")
	while(killbill == 0):
		#count(ser)
		#time.sleep(.050)
		if(cp==1):
			count(ser)
		
		else:	
			ser.parity = change_parity(0x0B, 1)
			ser.write(b'\x0B')
			ser.parity = change_parity(0x0B, 0)
			ser.write(b'\x0B')
			
			time.sleep(.05)
			r = ser.read(6)
			print("mo",r)
			
			if(r):
				print("A")
				if(r.__sizeof__() > 18):
					print("B")
					if (r[0] == 11):
						ser.parity = change_parity(0x00, 0)
						ser.write(b'\x00')
					elif(r[0] != 0 and r[0] !=11 and r[0]!=2 and r.__sizeof__() > 18):
						print("C")
						print(r)
						ser.parity = change_parity(0x00, 0)
						ser.write(b'\x00')
						if (rep == 0):
							print("D")
							palPoll(ser,r[0], r)

							cambio = total - aux_tarifa
							aux_cambio=cambio
							count(ser)

							rep = 0
							#rep=1
					if (r[0] == 0):
						rep = 0
			time.sleep(.002)
			time.sleep(.002)
			ser.parity = change_parity(0x33, 1)
			ser.write(b'\x33')
			ser.parity = change_parity(0x33, 0)
			ser.write(b'\x33')
			time.sleep(.05)
			rBill = ser.read(6)
			print("bi",rBill)
			if(rBill):
				if(rBill[0]==144 or rBill[0]==145 or rBill[0]==146 or rBill[0]==147 or rBill[0]==148):
					billeteConfirmado=1
					#cambiaColor=1
					disable_coin(ser)
					cambio = 0
					if(rBill[0]==144):
						bill = 20
						billetes[0]=billetes[0]+1
						billetesPago[0]=billetesPago[0]+1
					if(rBill[0]==145):
						bill = 50
						billetes[1]=billetes[1]+1
						billetesPago[1]=billetesPago[1]+1
					if(rBill[0]==146):
						bill = 100
						billetes[2]=billetes[2]+1
						billetesPago[2]=billetesPago[2]+1
					if(rBill[0]==147):
						bill = 200
						billetes[3]=billetes[3]+1
						billetesPago[3]=billetesPago[3]+1
					if(rBill[0]==148):
						bill = 500

					total = total+ bill
					dineroTotalB=dineroTotalB+bill

					print(total)
					#time.sleep(.005)
					ser.parity = change_parity(0x00, 0)
					ser.write(b'\x00')
					cambio = total - aux_tarifa
					accept_sequence(ser)
					count(ser)
					if(aux_cambio<0):
						enable_coin(ser)
						#enable_sequence(ser)

def monitorearChanger():
	global cartuchoRemovido
	ba = [0x0F, 0x05]
	ckInt = checkSum(ba)
	ser.parity = change_parity(0x0F, 1)
	ser.write(b'\x0F')
	ser.parity = change_parity(0x05, 0)
	ser.write(b'\x05')
	ser.parity = change_parity(int(ckInt), 0)
	ser.write(bytes([int(ckInt)]))
	time.sleep(.005)
	r = ser.read(8)
	print("rut->",r)
	if(r):
		if(r[0]==21 and r[1]==2):
			cartuchoRemovido=1

def enable_sequence(ser):
		#STAKER
	print("Stacker")
	while(1):
		ser.flushOutput()
		ser.flushInput()
		time.sleep(.09)
		ser.parity = change_parity(0x36, 1)
		ser.write(b'\x36')
		ser.parity = change_parity(0x36, 0)
		ser.write(b'\x36')
		time.sleep(.09)
		ask = ser.read(2)
		print(ask)
		if (ask):
			if(ask[0]==254):
				print("Pila llena")
			elif(ask[0]==00):
				print("Pila Vacia")
				time.sleep(.2)
				ser.parity = change_parity(0x00, 0)
				ser.write(b'\x00')
				break

	#Bill-type
	
	while(1):
		time.sleep(.09)
		ser.parity = change_parity(0x34, 1)
		ser.write(b'\x34')
		ser.parity = change_parity(0x00, 0)
		ser.write(b'\x00')
		ser.parity = change_parity(0x07, 0)
		ser.write(b'\x07')
		ser.parity = change_parity(0x00, 0)
		ser.write(b'\x00')
		ser.parity = change_parity(0x07, 0)
		ser.write(b'\x07')
		ser.parity = change_parity(0x42, 0)
		ser.write(b'\x42')
		ask = ser.read(1)
		print(ask)
		if (ask):
			print("Bill Habilitado",ask)
			if(ask==b'\x00'):
				time.sleep(.09)
				break



def palPoll(ser,r1,r):
	global cambiaColor,total,tarifa,cambio,rep,monedas,monedasTotal,dineroTotal,avis,aux_cambio,monedasPago
	entregadas=0
	tipoMoneda=0
	valorMoneda=0
	status=""
	if (128&r1 == 0 and 64&r1 != 0):
		if(32&r1==0 and 16&r1==0):
			print("ruta: Caja")
		elif (32 & r1 == 0 and 16 & r1 != 0):
			print("ruta: Tubos")
		elif (32 & r1 != 0 and 16 & r1 == 0):
			print("ruta: Sin uso")
		elif (32 & r1 != 0 and 16 & r1 != 0):
			print("ruta: Retornada")

	else:
		if(r1==1):
			status="Escrow request --- 1"
		if(r1==2):
			status="Entregaando cambio : "+str(aux_cambio)
		if(r1==3):
			status="No credit --- 3"
		if(r1==4):
			status="Defective tube sensor --- 4"
		if(r1==5):
			status="Double arrival --- 5"
		if(r1==6):
			status="Aceptor unplugged --- 6"
		if(r1==7):
			status="Tube Jam --- 7"
		if(r1==8):
			status="Checksum Error --- 8"
		if(r1==9):
			#status=""
			ms="Coin routing Error --- 9"
		if(r1==10):
			status="Changer Busy --- 10"
		if(r1==12):
			status="Coin Jam in the acceptance path --- 12"
		if(r1==13):
			status="Posible credited coin removal --- 13"
		print(status)
		avis=status
		return
	b=8
	while (b != 0):
		if (b & r1 != 0):
			tipoMoneda+=b
		b=b>>1
	if(tipoMoneda==2):
		valorMoneda=1
		monedas[0]=monedas[0]+1
		monedasPago[0]=monedasPago[0]+1
	if (tipoMoneda == 3):
		valorMoneda = 2
		monedas[1]=monedas[1]+1
		monedasPago[1]=monedasPago[1]+1
	if (tipoMoneda == 4):
		valorMoneda = 5
		monedas[2]=monedas[2]+1
		monedasPago[2]=monedasPago[2]+1
	if (tipoMoneda == 5):
		valorMoneda = 10
		monedas[3]=monedas[3]+1
		monedasPago[3]=monedasPago[3]+1
	print("Moneda insertada: ",valorMoneda)

	#cambiaColor=1
	#print("Monedas en tubo: ",r2)
	total=total+valorMoneda
	dineroTotal=dineroTotal+valorMoneda
	monedasTotal=monedasTotal+1
	print("Monto actual: ",total)


def accept_sequence(ser):
	time.sleep(.3)
	while(1):
		ser.parity = change_parity(0x35, 1)
		ser.write(b'\x35')
		ser.parity = change_parity(0x01, 0)
		ser.write(b'\x01')
		ser.parity = change_parity(0x36, 0)
		ser.write(b'\x36')
		r = ser.read(1)
		print("1: ",r)
		time.sleep(.005)
		if(r==b'\x00'):
			break
	while(1):
		ser.parity = change_parity(0x33, 1)
		ser.write(b'\x33')
		ser.parity = change_parity(0x33, 0)
		ser.write(b'\x33')
		r = ser.read(1)
		if(r):
			print("2:",r)
			time.sleep(.05)
			aux = BitArray(r)
			if(aux.bin[0:4]=="1000"):
					ser.parity = change_parity(0x00,0)
					#ser.write(b'\x00')
					break
			elif(aux.bin[0:4]=="1001"):
					ser.parity = change_parity(0x00,0)
					#ser.write(b'\x00')
					break
			elif(aux.bin[0:4]=="1010"):
					ser.parity = change_parity(0x00,0)
					#ser.write(b'\x00')
					break
			elif(aux.bin[0:4]=="1100"):
					ser.parity = change_parity(0x00,0)
					#ser.write(b'\x00')
					break
	while(1):
		ser.parity = change_parity(0x33, 1)
		ser.write(b'\x33')
		ser.parity = change_parity(0x33, 0)
		ser.write(b'\x33')
		r = ser.read(1)
		#print("Espera Otra respuesta: ",r)
		
		if(r):
			print("3",r)
			ser.write(b'\x00')
			"""time.sleep(.005)
			aux = BitArray(r)
			if(aux.bin[0:4]=="1000"):"""
			if(r==b'\x00'):
				break

def disable_coin(ser):
	while (1):
		#print("asdddd")
		ser.parity = change_parity(0x0C, 1)
		ser.write(b'\x0C')
		ser.parity = change_parity(0x00, 0)
		ser.write(b'\x00')
		ser.parity = change_parity(0x00, 0)
		ser.write(b'\x00')
		ser.parity = change_parity(0x00, 0)
		ser.write(b'\x00')
		ser.parity = change_parity(0x00, 0)
		ser.write(b'\x00')
		ser.parity = change_parity(0x0C, 0)
		ser.write(b'\x0C')
		r = ser.read(1)
		print(r)
		if(r):
			if (r[0] == 0):  # Verificar la respuesta <----------
				print("Deshabilitacion de Monedas Exitosa")
				time.sleep(.005)
				break


def enable_coin(ser):
	global mona,mond
	mona=60
	mond=60
	ba = [0x0C, mona, mond]
	ckInt = checkSum(ba)
	print("vals...>>>",mona,mond,ckInt)
	#time.sleep(1)
	while (1):
		#print("asdddd")
		ser.parity = change_parity(0x0C, 1)
		ser.write(b'\x0C')
		ser.parity = change_parity(0x00, 0)
		ser.write(b'\x00')
		ser.parity = change_parity(mona, 0)
		ser.write(bytes([int(mona)]))
		ser.parity = change_parity(0x00, 0)
		ser.write(b'\x00')
		ser.parity = change_parity(mond, 0)
		ser.write(bytes([int(mond)]))
		ser.parity = change_parity(ckInt, 0)
		ser.write(bytes([int(ckInt)]))
		#time.sleep(.05)
		r = ser.read(1)
		print(r)
		if(r):
			if (r[0] == 0):  # Verificar la respuesta <----------
				print("Habilitacion de Monedas Exitosa")
				time.sleep(.005)
				break

def obtenerPlazaYLocalidad():
	global nom, loc
	try:
		connection = psycopg2.connect(database='CajerOk',user='postgres',password='Postgres3UMd6', host='localhost')
		#connection = psycopg2.connect(user=usuario, password=contrasenia, database=bd, host='localhost')
		with connection.cursor() as cursor:
			cursor.execute(
				' SELECT nombre_plaza,estado FROM plaza WHERE idplaza = 1')
			row = cursor.fetchone()
			if row is not None:
				print("columns: {}, {}".format(row[0], row[1]))
				nom = str(row[0])
				loc = str(row[1])
				connection.commit()
				connection.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
		
		



def Init(ser):
	#RESET COIN CHANGER
	global rep,nivelDeCambio,NoCajero
	print(ser.inWaiting())
	ser.flushOutput()
	ser.flushInput()
	rep=0
	botones.prenderMonedero()
	time.sleep(5)
	infile = open("/home/pi/Documents/plaza.txt", 'r')
	c=infile.readline()
	arr=c.split(',', 1 )
	infile.close()
	obtenerPlazaYLocalidad()
	infile = open("/home/pi/Documents/NoCajero.txt", 'r')
	NoCajero=infile.readline()
	infile.close()


	while (1):
		ser.flushOutput()
		ser.flushInput()
		ser.parity = change_parity(0x08, 1)
		ser.write(b'\x08')
		ser.parity = change_parity(0x08, 0)
		ser.write(b'\x08')
		time.sleep(.005)
		r = ser.read(1)
		print("RE,",r)
		if(r):
			if (r[0] == 0):
				break
	while (1):
		ser.parity = change_parity(0x0F, 1)
		ser.write(b'\x0F')
		ser.parity = change_parity(0x00, 0)
		ser.write(b'\x00')
		ser.parity = change_parity(0x0F, 0)
		ser.write(b'\x0F')
		time.sleep(.2)
		r = ser.read(33)  # Verificar en el simulador se ve que devuelve 34
		print(r)
		if (r):
			if (r[0] == 77):  # Verificar la respuesta (4D = M, 45 = E, 49 = I) <----------
				ser.parity = change_parity(0x00, 0)
				ser.write(b'\x00')  # Devuelve ACK
				break

	ser.flushInput()
	ser.flushOutput()
	disable_coin(ser)
	cont=0
	while(1):

		ser.parity = change_parity(0x0F, 1)
		ser.write(b'\x0F')
		ser.parity = change_parity(0x05, 0)
		ser.write(b'\x05')
		ser.parity = change_parity(0x14, 0)
		ser.write(b'\x14')
		#time.sleep(.02)
		r = ser.read(2)
		if(r):
			print("rrrrr__:",r)
			if(cont==2):
				print("LISTO!---")
				break
			else:
				cont=cont+1
				print("DESHINIBIENDO!---",cont)
				enable_coin(ser)
				time.sleep(2)
	






def count(ser):
	global registraPago,comienzaCobro,comienzaCambio,Sinpago,DA,costillo,cajeroSuspendido,cs2,suspenderCajero,cp,total,bill,cambio,tarifa,aux_cambio,killbill,pagado,monedas,monedasTotal,dineroTotal,nivelDeCambio,imprime,monedasPago,billetesPago,NoCajero,tarifasAplicadas,fechaAMD,fo,pe,h,monedasCambio
	i=-1
	comienzaCobro=1
	registraPago=0
	valoresMonedas=[1,2,5,10]
	valoresBilletes=[20,50,100,200]
	if(cp==1):
		cambio = total - aux_tarifa
		cambio=aux_tarifa+cambio
		print("-.-.-.-.-.cancelando pago")
	else:
		cambio = total - aux_tarifa
	aDar=0
	desconteo=0
	aux_cambio = cambio
	mm1=0
	mm2=0
	mm3=0
	mm4=0
	mmc=0
		
	if (cambio > 0):
		print("hay cambio")
		imprime=1
		comienzaCambio=1
		#dineroTotal=dineroTotal+aux_tarifa
		disable_sequence(ser)
		print(ser.inWaiting())
		ser.flushOutput()
		ser.flushInput()
		#ESTATUS TUBOS
		while(1):
			time.sleep(.1) #Para completar los 500 ms
			ser.parity = change_parity(0x0A, 1)
			ser.write(bytes([10]))
			ser.parity = change_parity(0x0A, 0)
			ser.write(bytes([10]))
			time.sleep(.1)
			r = ser.read(18) #Verificar en el simulador se ven 19
			if(r):
				print("h", r[4],r[5],r[6],r[7],r)
				if (r[0] == 0):  # Verificar la respuesta <----------
					if(r.__sizeof__()>=30):
						if(r[4] == 0 or r[5] == 0 or r[6] == 0 or r[7] == 0):
							print("errinfo...")
							suspenderCajero=1
							if(cajeroSuspendido==1):
								suspenderCajero=0
								cs2=0
								break
						else:
							suspenderCajero=0
							cs2=0
							cajeroSuspendido=0
							print("Estatus de Llenado de Tubo: ", r[0], r[1]) #Verificar si se debe imprimir en Decimal o Ascii
							mm1=r[4]
							mm2=r[5]
							mm3=r[6]
							mm4=r[7]
							print("Monedas antes de...",mm1,mm2,mm3,mm4,monedas)
							ser.parity = change_parity(0x00, 0)
							ser.write(b'\x00')
							break
					


		if(cajeroSuspendido==1):
			registraPago=1
			killbill = 1
			pagado=2
			
		
		else:
			while(1):
				if(cambio<=20):
					#pagado=1
					if(cambio!=0):
						darCambio(ser,cambio)
					killbill = 1
					pagado=2
					break
				else:
					darCambio(ser,20)
					cambio=cambio-20



			while(1):
				time.sleep(.1) #Para completar los 500 ms
				ser.parity = change_parity(0x0A, 1)
				ser.write(bytes([10]))
				ser.parity = change_parity(0x0A, 0)
				ser.write(bytes([10]))
				time.sleep(.1)
				r = ser.read(18) #Verificar en el simulador se ven 19
				if(r):
					print("h", r)

					if (r[0] == 0):  # Verificar la respuesta <----------
						if(r.__sizeof__()>=30):
							if(r[4] == 0 or r[5] == 0 or r[6] == 0 or r[7] == 0):
								print("errinfo2...")
								suspenderCajero=1
								if(cajeroSuspendido==1):
									suspenderCajero=0
									cs2=0
									break
							else:
								suspenderCajero=0
								cs2=0
								cajeroSuspendido=0
								print("Estatus de Llenado de Tubo: ", r[0], r[1]) #Verificar si se debe imprimir en Decimal o Ascii
								mm1=mm1-r[4]
								mm2=mm2-r[5]
								mm3=mm3-r[6]
								mm4=mm4-r[7]
								monedasTotal=monedasTotal-(mm1+mm2+mm3+mm4)
								monedas[0]=monedas[0]-mm1
								monedas[1]=monedas[1]-mm2
								monedas[2]=monedas[2]-mm3
								monedas[3]=monedas[3]-mm4
								#Monedas dispensadas como cambio
								monedasCambio[0]=mm1
								monedasCambio[1]=mm2
								monedasCambio[2]=mm3
								monedasCambio[3]=mm4

								dineroTotal=dineroTotal-((mm1*1)+(mm2*2)+(mm3*5)+(mm4*10))
								print("Monedas despues de...",r[4],r[5],r[6],r[7],mm1,mm2,mm3,mm4,monedas)
								ser.parity = change_parity(0x00, 0)
								ser.write(b'\x00')
								break

		
		if(cp==1):
			print("Pago canceladoA")
			#cp=0
		else:
			registraPago=1
	print("1111cp",cp," registrapago-",registraPago,"CAMBIO...",cambio)
	if(cambio==0): # if(total==aux_tarifa):
		imprime=1
		killbill = 1
		comienzaCambio=1
		time.sleep(.05)
		pagado=2
		if(cp==1):
			print("Pago cancelado")
			#cp=0
			
		else:
			registraPago=1
		disable_coin(ser)
		disable_sequence(ser)

	if(registraPago==1):
		#REGISTRAR PAGO EN SERVIDOR
		#idcaj,mediopago,monto, descripcion de las monedas pagadas, descripcion de los billetes pagados, tarifas implementadas
		DA=DA+costillo
		descripcionMonedas=""
		descripcionBilletes=""
		descripcionMonedasCambio=""
		print("--------*******",monedasPago)
		if(monedasPago[0]==0 and monedasPago[1]==0 and monedasPago[2]==0 and monedasPago[3]==0):
			descripcionMonedas="0:0"
		else:
			for moneda in monedasPago:
				i=i+1
				if(moneda!=0):
					descripcionMonedas=descripcionMonedas+str(moneda)+":"+str(valoresMonedas[i])+","

		descripcionMonedas=descripcionMonedas.rstrip(',')

		print("i={}, descMon={}, valMon={}, monedasPago={}".format(i,descripcionMonedas,valoresMonedas,monedasPago))
		i=-1

		print("--------*******",billetesPago)
		if(billetesPago[0]==0 and billetesPago[1]==0 and billetesPago[2]==0 and billetesPago[3]==0 ):
			descripcionBilletes="0:0"
		else:
			for billete in billetesPago:
				i=i+1
				if(billete!=0):
					descripcionBilletes=descripcionBilletes+str(billete)+":"+str(valoresBilletes[i])+","
		descripcionBilletes=descripcionBilletes.rstrip(',')
		print("i={}, descBill={}, valBill={}, billPago={}".format(i,descripcionBilletes,valoresBilletes,billetesPago))


		#----------------------DESCRIPCION DE MONEDAS DISPENSADAS COMO CAMBIO-------------------
		i=-1

		print("--------*******",monedasCambio)
		if(monedasCambio[0]==0 and monedasCambio[1]==0 and monedasCambio[2]==0 and monedasCambio[3]==0 ):
			descripcionMonedasCambio="0:0"
		else:
			for monedaC in monedasCambio:
				i=i+1
				if(monedaC!=0):
					descripcionMonedasCambio=descripcionMonedasCambio+str(monedaC)+":"+str(valoresMonedas[i])+","
		descripcionMonedasCambio=descripcionMonedasCambio.rstrip(',')
		print("-------MONEDAS DISPENSADAS: ------",descripcionMonedasCambio)


		msj1=str(fo) + "," + str(pe) + "," + fechaAMD +" "+h
		print("*************      ",msj1)
		#mensaje=str(NoCajero)+";"+"1"+";"+str(aux_tarifa)+";"+descripcionMonedas+";"+descripcionBilletes+";"+tarifasAplicadas
		if(tarifasAplicadas==""):
			tarifasAplicadas="13"
		mensaje=str(NoCajero)+";"+"1"+";"+str(costillo)+";"+str(DA)+";"+descripcionBilletes+";"+descripcionMonedasCambio+";"+tarifasAplicadas
		print("Mensaje pago: ,tarifasAplicadas ",mensaje,tarifasAplicadas)

		g=Servidor.configSocket("pago boleto", msj1+"*"+mensaje)
		if(g==-1):
			Sinpago=Sinpago+1
		#s.send("1;1;20.00;2:5,1:10;0:0;2,5".encode('utf-8'))
		monedasPago[0]=0
		monedasPago[1]=0
		monedasPago[2]=0
		monedasPago[3]=0
		billetesPago[0]=0
		billetesPago[1]=0
		billetesPago[2]=0
		billetesPago[3]=0
		monedasCambio[0]=0
		monedasCambio[1]=0
		monedasCambio[2]=0
		monedasCambio[3]=0
		tarifasAplicadas=""
	else:
		print("pausillaJA",aux_tarifa,aux_cambio)
	print("pausilla",DA,Sinpago,"cp",cp," registrapago-",registraPago)
	




def darCambioManual(ser,valor):
	while(1):
		time.sleep(.05)
		print(valor,"<--- aDar")
		ba = [0x0D, int(valor)]
		ckInt = checkSum(ba)
		ser.parity = change_parity(0x0D, 1)
		ser.write(b'\x0D')
		ser.parity = change_parity(int(valor), 0)
		ser.write(bytes([int(valor)]))
		ser.parity = change_parity(int(ckInt), 0)
		ser.write(bytes([int(ckInt)]))

		time.sleep(.05)
		ser.parity = change_parity(0x0B, 1)
		ser.write(b'\x0B')
		ser.parity = change_parity(0x0B, 0)
		ser.write(b'\x0B')
		time.sleep(.005)
		k = ser.read(4)
		if(k):
			print(k)
			if(k.__sizeof__()==18):
				if(k[0]==2):
					print("insistir",k)
					break
			if(k.__sizeof__()==19):
				if(k[0]==2 or k[1]==2):
					print("insistir",k)
					break
			if(k.__sizeof__()==20):
				if(k[0]==2 or k[1]==2 or k[2]==2):
					print("insistir",k)
					break
	while(1):
		ser.parity = change_parity(0x0B, 1)
		ser.write(b'\x0B')
		ser.parity = change_parity(0x0B, 0)
		ser.write(b'\x0B')
		time.sleep(.005)
		k = ser.read(3)
		print("poll",k)
		if(k):
			if(k[0]==0):
				print("roto")
				time.sleep(.005)
				break


def darCambio(ser,monto):
	while(1):
		print("NO")
		global total,cambio
		#print(monto)
		dar=monto/factorDeEscala
		print(dar)
		ba = [0x0F, 0x02, int(dar)]
		ckInt = checkSum(ba)
		#print("cambio->", cambio, "check->", ckInt)
		ser.parity = change_parity(0x0F, 1)
		ser.write(b'\x0F')
		ser.parity = change_parity(0x02, 0)
		ser.write(b'\x02')
		ser.parity = change_parity(int(dar), 0)
		ser.write(bytes([int(dar)]))
		ser.parity = change_parity(int(ckInt), 0)
		ser.write(bytes([int(ckInt)]))
		time.sleep(.009)
		ser.parity = change_parity(0x0B, 1)
		ser.write(b'\x0B')
		ser.parity = change_parity(0x0B, 0)
		ser.write(b'\x0B')
		time.sleep(.005)
		k = ser.read(3)

		if(k):

			print(k)
			if(k.__sizeof__()>18):

				if(k[0]==2 or k[1]==2):
					print("Comenzando pago..",k)

					break
	while(1):
		ser.parity = change_parity(0x0B, 1)
		ser.write(b'\x0B')
		ser.parity = change_parity(0x0B, 0)
		ser.write(b'\x0B')
		time.sleep(.005)
		k = ser.read(6)
		print("poLL",k)
		if(k):
			if(k[0]!=2):
				palPoll(ser,k[0], k)
				if(k[0]==0):
					print("roto")
					time.sleep(.005)
					break
				else:
					ser.flushOutput()
					ser.flushInput()
					print("Error al finalizar el pago...")
					ser.parity = change_parity(0x00, 0)
					ser.write(b'\x00')





			#if(k[0]==0):
			#	break;


def change_parity(comando,paridad):
	b=128
	cont=0
	while b!=0 :
		if b&comando!=0:
			cont=+cont+1
		b=b>>1
	if paridad == 1:
		if cont % 2 == 0:
			return serial.PARITY_ODD
		else:
			return serial.PARITY_EVEN
	elif paridad == 0:
		if cont % 2 == 0:
			return serial.PARITY_EVEN
		else:
			return serial.PARITY_ODD

def checkSum(arr):
	j=0
	sum=0
	tam=arr.__len__()
	while(j<tam):
		#print(j, tam)
		sum=sum+arr[j]
		j=j+1
	return 255&sum

def leerCodQR():
	global mensajeError
	print("Mensaje bandera camara !!!!!!!!********")
	#lee = os.system("zbarcam --raw  --nodisplay /dev/video0 > /home/pi/Documents/ticket.txt")
	try:
		#so=os.system("./dsreader -l 1 -s 500 > /home/pi/Documents/ticket.txt")
		#lee = os.system("zbarcam --raw --prescale=10x10  /dev/video0 > /home/pi/Documents/ticket.txt")
		lee = os.system("zbarcam --raw  --prescale=280x150 /dev/video0 > /home/pi/Documents/ticket.txt")
		pass
	except e:
		mensajeError=1
		print("Error al crear el socket: ",e)
		
def leerCodQR2():
	global camInicial
	#time.sleep(1)
	lee2 = os.system("sudo find /dev -name 'video*' > cam.txt")
	a = open("cam.txt", "r")
	cam=(a.readline().rstrip("\n")).lstrip("\x00")
	a.close()
	a = open("cam.txt", "w")
	a.write('')
	camInicial=cam
	print('CamInicial',camInicial)
	while(1):
		time.sleep(1)
		lee2 = os.system("sudo find /dev -name 'video*' > cam.txt")
		a = open("cam.txt", "r")
		cam=(a.readline().rstrip("\n")).lstrip("\x00")
		a.close()
		a = open("cam.txt", "w")
		a.write('')
		print('Cam',cam,camInicial)
		if(cam==camInicial):

			try:
				#print('Camara Detectada')
				lee = os.system("zbarcam --raw --prescale=280x150   "+cam+" > /home/pi/Documents/ticket.txt")
				#lee = os.system("zbarcam --raw  --prescale=10x10 /dev/video0 > /home/pi/Documents/eum/app/caseta/ticket.txt")
				#lee = os.system("/home/pi/Documents/eum/app/caseta/dsreader -l 27 -b 14 -r 30 -s 100 -u 50  > /home/pi/Documents/eum/app/caseta/ticket.txt")
				#lee = os.system("cd /home/pi/scanner/dsreader")
				#lee = os.system("./dsreader -l 27 -b 14 -r 30 -s 100 -u 50  > /home/pi/Documents/eum/app/caseta/ticket.txt")

			except e:
				mensajeTolerancia=1
				#print("Error al crear el socket: ",e)
		else:
			
			if(cam!=''):
				camInicial=cam
			else:
				#print('Camara desconectada')
				pass

def disable_sequence(ser):
#Bill-type-
	print("Bill-Type-disable")
	while(1):
		time.sleep(1)
		ser.parity = change_parity(0x34, 1)
		ser.write(b'\x34')
		ser.parity = change_parity(0x00, 0)
		ser.write(b'\x00')
		ser.parity = change_parity(0x00, 0)
		ser.write(b'\x00')
		ser.parity = change_parity(0x00, 0)
		ser.write(b'\x00')
		ser.parity = change_parity(0x00, 0)
		ser.write(b'\x00')
		ser.parity = change_parity(0x34, 0)
		ser.write(b'\x34')
		ask = ser.read(1)
		print(ask)
		if (ask):
			if(ask==b'\x00'):
				time.sleep(.25)
		break

#MAIN
if __name__ == "__main__":
	global ser
	time.sleep(3)
	ser = serial.Serial("/dev/ttyAMA0")  # Open named port
	ser.baudrate = 9600  # Set baud rate
	ser.parity = serial.PARITY_NONE
	ser.stopbits = serial.STOPBITS_ONE
	ser.bytesize = serial.EIGHTBITS
	#ser.timeout = .005 GOOD
	ser.timeout = .004

	leerArch = open("/home/pi/Documents/ticket.txt", "w")
	leerArch.write('')
	leerArch.close()


	Init(ser)
	#enable_coin(ser)
	disable_sequence(ser)
	#INICIALIZAMOS EL HILO DE LA INTERFAZ
	thread1 = Thread(target=interface,args=())
	#time.sleep(5)
	thread3 = Thread(target=leerCodQR, args = ())
	#thread5 = Thread(target=buscaCamara, args=())
	thread4 = Thread(target=leerArchivo, args=())
	
	#os.system("sudo nice -n -19 python3 archimp.py")
	try:

		thread1.start()
		time.sleep(.4)
		
		#thread5.start()
		time.sleep(.4)
		thread3.start()
		thread4.start()



	except Exception as e:
		pass

	while(thread1.is_alive()):
		kill = 0
	kill = 1

	print("termine")
