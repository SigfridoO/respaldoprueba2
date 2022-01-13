

import pyqrcode
import time, os
import commands
import sys
import getpass

PATH_PONER_DATOS_TICKET="zbarcam --raw /dev/video0 > /home/pi/Documents/CAJA_1_Monterrey/datos_tikets/ticket.txt"
PATH_LEER_DATOS_TICKET="/home/pi/Documents/CAJA_1_Monterrey/datos_tikets/ticket.txt"

def leerCodQR():
	resultado = commands.getoutput(PATH_PONER_DATOS_TICKET)
	leerArch = open(PATH_LEER_DATOS_TICKET, "r")
	folio=leerArch.readline()
	inTerminal=leerArch.readline()
	inFecha=leerArch.readline()
	inHora=leerArch.readline()
	readQR = []
	readQR.append(folio)
	readQR.append(inTerminal)
	readQR.append(inFecha)
	readQR.append(inHora)

	print(readQR)
	print(readQR[1])
	
	leerArch.close()
	return readQR
	pass

#print leerCodQR()
