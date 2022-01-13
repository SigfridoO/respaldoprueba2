# -*- coding: utf-8 -*-
"""
Estacionamientos unicos de México
Este archivo es para remplaar a acceso4.py
Funcion: 		Funcion de leerBotones
Descripcion:	Leer los pines de la rasp e imprimir folio
				tambien validamos los bones y falta diseñar la
				señal de sos

Funciones que se pueden usar:
	1) leerBotones()
	2) validarBotones()		
	3) leerBotonesEntrada()
	4) configurarPinesGPIO()
	*) SOS()

"""
import RPi.GPIO as GPIO

import time
import generarFolio as folio



def configurarPinesGPIO():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(26,GPIO.IN)
	GPIO.setup(19,GPIO.IN)
	GPIO.setup(13,GPIO.OUT)
	GPIO.setup(6,GPIO.OUT)
	pass
def configurarPinesGPIOBobina():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(5,GPIO.IN)
	pass

def abrir():
	GPIO.output(13,True)
	time.sleep(0.5)
	GPIO.output(13,False)
	
def leerBobina2Subida():
	bobina2Subida=GPIO.input(5)	#5
	print "		Boton bobina=",bobina2Subida
	if bobina2Subida == 1:
		return True
	else:
		return False
	pass

def abrirBarrera():
	print "		Barrera abierta... "
	bobina2Bajada=GPIO.input(5) #5 Leeo para esperar la señal de bajada
	if bobina2Bajada == 1:
		print "	Se mantiene arriba por que hay carro=",bobina2Bajada
		return False
	else:
		print "	Se baja, ya recibì la señal =",bobina2Bajada
		return True

def CerrarBarrera():
	print "		Esperando a cerrar barrera... "
	bobina2Bajada=GPIO.input(5) #5 Leeo para esperar la señal de bajada
	if bobina2Bajada == 1: #cambiar po ceros
		print "	Se mantiene arriba por que hay carro=",bobina2Bajada
		return False
	else:
		print "	Se baja, ya recibì la señal =",bobina2Bajada
		return True

def leerBotonesEntrada():
	valorentrada1=GPIO.input(26)
	valorentrada2=GPIO.input(19)
	print "	Boton1 =",valorentrada1
	print "	Boton2 =",valorentrada2	
	#valorentrada1=1
	#valorentrada2=1
	return valorentrada1,valorentrada2
	pass
def validarBotones(b1,b2):
	if b1==True and b2==True:
		global contadorPresionarBoleto
		contadorPresionarBoleto=contadorPresionarBoleto+1
		return True
	else:
		return False
	pass


	
def abririCerrar():
	print "Abrir Cerrar"
	GPIO.output(13,True)
	time.sleep(0.5)
	GPIO.output(13,False)
	time.sleep(10)
	GPIO.output(6,True)
	time.sleep(0.5)
	GPIO.output(6,False)
	pass


contadorPresionarBoleto=0	
#leerBotones()
