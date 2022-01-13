# -*- coding: utf-8 -*-
"""
Estacionamientos unicos de México

"""
import RPi.GPIO as GPIO

import time



def configurarPinesGPIO():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(26,GPIO.IN)# TICKET
	GPIO.setup(19,GPIO.IN)# MASA
	GPIO.setup(13,GPIO.OUT) #LEVANTA
	GPIO.setup(6,GPIO.OUT) # BAJA
	GPIO.setup(20,GPIO.IN) #CONFIG 1
	GPIO.setup(21,GPIO.IN) #CONFIG 2
	GPIO.setup(16,GPIO.IN) #APAGAR
	pass
def configurarPinesGPIOBobina():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(5,GPIO.IN)
	pass

def abrir():
	GPIO.output(13,True)
	time.sleep(0.5)
	GPIO.output(13,False)
	
def cerrar():
	GPIO.output(6,True)
	time.sleep(0.5)
	GPIO.output(6,False)
	
	
def leerLevanta():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(13,GPIO.IN)
	boton=GPIO.input(13)
	print boton
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(13,GPIO.OUT)
	
def leerBaja():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(6,GPIO.IN)
	boton=GPIO.input(6)
	print boton
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(6,GPIO.OUT)

def leerMasa():
	pin=GPIO.input(19)
	print pin
	return pin
	
def leerTicket():
	pin=GPIO.input(26)
	print pin
	return pin


def leer2bobina():
	pin=GPIO.input(5)	#5
	print pin
	return pin

def leerConfiguracion():
	config1 = GPIO.input(20)
	config2 = GPIO.input(21)
	print config1 
	print config2
	return config1,config2

def gpiocleanup():
	GPIO.cleanup()
	print "LImpio GPIO"
	
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

