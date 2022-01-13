# -*- coding: utf-8 -*-
"""
Funciones para escribir en archivo de cONFIGURACION
Formato Mar 5 2015 12:46:00
"""
PATH_ESCRIBIR_ARCHIVO="/home/pi/Documents/EUM_CONFIGURACION_EXP/ArchivosConfig/configuracionTerminal.txt"
PATH_ESCRIBIR_FECHA_HORA="/home/pi/Documents/EUM_CONFIGURACION_EXP/ArchivosConfig/configuracionFechaHora.txt"

def escribirArchivoDatosDeTerminal(plazaName,estado,muni,numTer):
	plazaName=str(plazaName)
	estado=str(estado)
	muni=str(muni)
	numTer=str(numTer)
	# Abrimos el archivo 
	fo = open(PATH_ESCRIBIR_ARCHIVO, "wb")
	fo.write( plazaName+"\n"+estado+"\n"+muni+"\n"+numTer+"\n");
	# Cerramos el archivo 
	fo.close()
	pass

def escibirArchivoFechaHora(fecha,hora):
	fecha=str(fecha)
	hora=str(hora)
	# Abrimos el archivo 
	fo = open(PATH_ESCRIBIR_FECHA_HORA, "wb")
	fo.write( fecha+"\n"+hora);
	# Cerramos el archivo 
	fo.close()
	pass

#escribirArchivoDatosDeTerminal("PLAZA PACHUCOS","mexico","neza",10)
#escibirArchivoFechaHora("02/02/2017","23:59:20")
