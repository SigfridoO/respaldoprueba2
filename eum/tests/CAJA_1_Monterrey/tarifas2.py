# -*- coding: utf-8 -*-

import math

import escribirTipoBoleto as boleto
import os

COSTO_POR_HORA_EXTRA=10
COSTO_MAXIMO=120
COSTO_POR_HORA_SIN_SELLO=10
HORAS_DE_COOPERACION_VOLUNTARIA=120
COSTO_BOLETO_PERDIDO=100
PATH_INTERFAZ_TIPO_BOLETO="/home/pi/Documents/CAJA_1_Monterrey/tipoBoleto.py"


def preguntarPorVoluntario():
	#LLAMO A A¿LA INTERFAZ
	os.system("python "+PATH_INTERFAZ_TIPO_BOLETO)
	return boleto.getDato()


def calcularMonto(purosMinutos,tar):
	total=0
	tarifa=int(tar)
	tiempo=int(purosMinutos)
	dato2=0
	print tiempo
	#Tarifa 1: bodega aurrera vips y suburbia $5 dos primeras horas
	if tarifa==1:
		if tiempo<=120:
			total=5
		else:
			total=5+((tiempo-61)//60)*(COSTO_POR_HORA_EXTRA)
		dato2=1
	#Tarifa 2: cinemex $8 por hora las primeras 3 horas
	if tarifa==2:
		if tiempo<=180:
			total=((tiempo+59)//60)*8
		else:
			total=(8*3)+((tiempo-121)//60)*COSTO_POR_HORA_EXTRA
		dato2=2
	#Tarifa 3: $10 hora o fraccion
	if tarifa==3:
		total=((tiempo+59)//60)*COSTO_POR_HORA_SIN_SELLO
		dato2=3
	#Tarifa 4: boleto perdido
	if tarifa==4:
		total=total+COSTO_BOLETO_PERDIDO
		dato2=4
	#Regla de costo maximo
	if total>COSTO_MAXIMO:
		total=COSTO_MAXIMO
	print(total)
	return float(total),dato2
	
print calcularMonto(720,2)
