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



def botonApagarGPIO():
	btn=GPIO.input(16)	#5
	if btn == 1:
		return True
	else:
		return False
	pass
