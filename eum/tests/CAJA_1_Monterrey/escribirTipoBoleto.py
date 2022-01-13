# -*- coding: utf-8 -*-

"""
Funciones para leer datos
"""
PATH_ARCHIVO_CONFIGURACION_TERMINAL="/home/pi/Documents/CAJA_1_Monterrey/tipoBoleto.txt"
PATH_ARCHIVO_VOLUNTARIO="/home/pi/Documents/CAJA_1_Monterrey/montoVoluntario.txt"

configuracion=''

def getDato():
	archivo=open(PATH_ARCHIVO_CONFIGURACION_TERMINAL, "r")
	for linea in archivo.readlines():
		configuracion =linea
	archivo.close()
	return configuracion
	pass
	
def putDato(boleto):
	archivo=open(PATH_ARCHIVO_CONFIGURACION_TERMINAL, "w")
	archivo.write(boleto)
	archivo.close()

def getVoluntario():
	archivo=open(PATH_ARCHIVO_VOLUNTARIO, "r")
	for linea in archivo.readlines():
		configuracion =linea
	archivo.close()
	return configuracion
	pass

#putDato("Suburbia")
#print getDato()
