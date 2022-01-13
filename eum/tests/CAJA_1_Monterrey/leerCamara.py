# -*- coding: utf-8 -*-
"""
Funciones para leer datos de camara
"""
PATH_ARCHIVO_CONFIGURACION_TERMINAL="/home/pi/Documents/CAJA_1_Monterrey/datos_tikets/ticket.txt"
PATH_ARCHIVO_CONFIGURACION_TERMINAL_ARCHIVO_AUX="/home/pi/Documents/CAJA_1_Monterrey/datos_tikets/ticketAux.txt"
configuracion=[]

def getDatos():
	archivo=open(PATH_ARCHIVO_CONFIGURACION_TERMINAL, "r")
	contenido=archivo.readlines()
	if len(contenido)==0:
		global configuracion
		configuracion=[]
	else:
		for linea in contenido:
			configuracion.append(linea)
	archivo.close()
	pass

def getArreglo():
	archivo=open(PATH_ARCHIVO_CONFIGURACION_TERMINAL_ARCHIVO_AUX, "r")
	#iden=archivo.readline()
	folio=archivo.readline()
	inTerminal=archivo.readline()
	inFecha=archivo.readline()
	inHora=archivo.readline()
	readQR = []
	i = 0
	aux = ""
	for dato in inFecha:
		if i < 2:
			aux = aux + dato
		if i == 2 or i == 5:
			aux = aux + "/"
		if i < 5 and i > 2:
			aux = aux + dato
		if i < 10 and i > 5:
			aux = aux + dato
		i = i + 1
	inFecha = aux
	print (inFecha)
	readQR.append(folio)
	readQR.append(inTerminal)
	readQR.append(inFecha)
	readQR.append(inHora)
	print(readQR)
	archivo.close()
	return readQR
	pass

def getEstado():
	getDatos()
	return configuracion[0]
	pass
def getCuerpo():
	getDatos()
	return configuracion[1:]
def getTodo():
	getDatos()
	return configuracion[0:]
	pass

def respaldaArchivoTicket():
	archivo1=open(PATH_ARCHIVO_CONFIGURACION_TERMINAL, "r")
	archivo2=open(PATH_ARCHIVO_CONFIGURACION_TERMINAL_ARCHIVO_AUX, "w")
	for linea in archivo1.readlines():
		archivo2.write(linea)
	archivo1.close()
	archivo2.close()

def borrarArchivo():
	archivo=open(PATH_ARCHIVO_CONFIGURACION_TERMINAL, "w")
	archivo.write("")
	archivo.close



