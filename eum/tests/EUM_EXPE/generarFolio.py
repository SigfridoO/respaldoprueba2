# -*- coding: utf-8 -*-
"""
Estacionamientos unicos de México
Este archivo es para remplaar a acceso4.py
Funcion: 		Funcion de saberFolio
Descripcion:	Con estas funciones podemos modificar la
				la forma en que se hacen los folios, 
				ya sea por hora o fecha o bien se puede
				conectar a la base de datos para que se genere un identificador
				Tambien esribe todos los folios en el archivo
Funciones que se pueden usar:
	1)saberFolio()
	2)escribirArchivoFolios()		


"""
import fechaUTC as tiempo

PATH_EXTRAER_ULTIMO_FOLIO="/home/pi/Documents/EUM_EXPE/Tickets/UltimoFolio.txt"
PATH_BITACORA_FOLIOS="/home/pi/Documents/EUM_EXPE/Tickets/foliosBitacoras.txt"



def extraerBoleto():
	archi = open(PATH_EXTRAER_ULTIMO_FOLIO,"r")
	linea=archi.readline()
	archi.close()
	linea=int(linea)
	linea=linea+1
	return linea
	pass


def saberFolio():
	idBolteto= extraerBoleto()
	folioCompleto= "GM:"+str(idBolteto)
	escribirArchivoFolios(folioCompleto,idBolteto)
	return folioCompleto
	pass
	
	
def escribirArchivoFolios(f,idB):
	#Bitacora
	escribeArch = open(PATH_BITACORA_FOLIOS,"a")
	escribeArch.write(str(f)+"\n")
	escribeArch.close()
	#Escrbimos el ultimo boleto
	escribeArch = open(PATH_EXTRAER_ULTIMO_FOLIO,"w")
	escribeArch.write(str(idB)+"\n")
	escribeArch.close()
	
	pass
