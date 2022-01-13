# -*- coding: utf-8 -*-
#cortesExpFun para base de datos eumDataExp

from datetime import datetime
import time, os
import commands
import sys
#import psycopg2	
from escposprinter import *
import coneccionExp as con
import leerTXTconfiguracion as configTXT

import configuracionEXP as archivoConfiguracion
PATH_NOMBRE_PLAZA=str(archivoConfiguracion.getName()).replace('\n','')
DIRECCION_PLAZA=str(archivoConfiguracion.getDireccion())
terminalEnt=int(archivoConfiguracion.getNumTer())


Generic = printer.Usb(0x0519,0x0001)

def header():
	FECHA_ACTUAL=time.strftime("%d:%m:%Y")
	HORA_ACTUAL= time.strftime("%H:%M:%S")
	Generic.set(size='2x', align='center')
	Generic.text(PATH_NOMBRE_PLAZA+"\n")
	Generic.set(size='normal')
	Generic.text('Corte de Terminal \n')
	Generic.text('Fecha:'+FECHA_ACTUAL+'\n')
	Generic.text('Hora: '+HORA_ACTUAL+'\n')
	Generic.text('Terminal #'+str(terminalEnt))

def footer():
	Generic.set(align='left')
	Generic.text("    					  \n")
	Generic.text("     Firma Supervisor        Firma Cajero\n")
	Generic.text("    					  \n")
	Generic.text("    					  \n")
	Generic.text("   ===================	  ======================\n")
	Generic.cut()


"""
Query's de eumDataExp 
"""
def agregarCentroComercial(nombrePlaza,localidad_Estado,localidad_Muni,numeroTerminal):
	direccionCentroComercial=localidad_Muni+" "+localidad_Estado
	print "Nombre de la plaza: "+ nombrePlaza 
	print "Direccion de la plaza: "+direccionCentroComercial
	print "Numero de terminal: "+ numeroTerminal

	#fALTAN VALIDACIONES DE CONSISTENCIA DE DATOS

	#Insertamos en la tabla Centro Comercial
	query="INSERT INTO \"CentroComercial\" ( cen_com_nom, cen_com_dir) VALUES ('"+nombrePlaza+"',  '"+direccionCentroComercial+"');"
	#print(query)
	print "\t Comienza el query..."
	objetoConexion = con.Conexion()
	f = objetoConexion.execQuery(query)
	if(f<0):
		print("Error: Los datos no se guardaron en Centro comercial")
	else:
		print "\t----Exito al insertar en centro comercial"
		#Insertamos en la expedidora primero necesitamos saber cual es el ID DE CENTRO COMERCIAL QUE LE PUSIMOS
		query="SELECT id_cen_com  FROM \"CentroComercial\" WHERE cen_com_nom='"+nombrePlaza+"';"
		objetoConexion = con.Conexion()
		resultado=objetoConexion.doQuery(str(query))
		if resultado==-1:
			print " ERRO DE QUERY"
			pass
		else:
			print ("\t----EL Id de centro comercial: "+str(resultado[0][0]))
			ID_cen_com_querybase=int(resultado[0][0])
			pass
			query="INSERT INTO \"Expedidora\"(id_exp, id_exp_cc)VALUES ('"+str(numeroTerminal)+"','"+str(ID_cen_com_querybase)+"') ;"
			#print(query)
			objetoConexion = con.Conexion()
			f = objetoConexion.execQuery(query)
			if(f<0):
				print("Error: El dato no se guardo en expendidora")
			else:
				print "\t----Exito al insertar en expedidora"
	print "\t Termina el query..."

	
"""
Cortes de la expedidora
Por día:
	Corte 1
		2017-02-13
Entre fechas:	
	Corte 2
		2017-02-13
		2017-02-13
"""

def elijeCorte1PorDia(fechaDia):
	query="SELECT count( id_bol_exp)  FROM \"boletoexpedidora\" WHERE fec_bol_exp BETWEEN '"+fechaDia+" 00:00:00' AND '"+fechaDia+" 23:59:00' ;"
	objetoConexion = con.Conexion()
	resultado=objetoConexion.doQuery(str(query))
	if resultado==-1:
		print "***********ERRO DE QUERY en CORTE POR FECHA"
		pass
	else:
		print ("\t----Los boletos totales: "+str(resultado[0][0]))
		header()
		Generic.text("\tNumero de Boletos expedidos: "+str(resultado[0][0]))
		footer()
		pass

def elijeCorte2EntreFecha(fechaInicio,fechaFin):
	query="SELECT count( id_bol_exp)  FROM \"boletoexpedidora\" WHERE fec_bol_exp BETWEEN '"+fechaInicio+" 00:00:00' AND '"+fechaFin+" 23:59:00' ;"
	objetoConexion = con.Conexion()
	resultado=objetoConexion.doQuery(str(query))
	if resultado==-1:
		print "***********ERRO DE QUERY en CORTE ENTRE FECHAS"
		pass
	else:
		print ("\t----Los boletos totales: "+str(resultado[0][0]))
		header()
		Generic.text("\tNumero de Boletos expedidos: "+str(resultado[0][0]))
		footer()
		pass
	pass

#elijeCorte1PorDia("2017-01-03")


def insertarBoleto(nombrePlaza,numeroTerminal,folio,fechaIn,placa):
	print "Nombre de la plaza: "+ nombrePlaza 
	print "Numero de terminal: "+ str(numeroTerminal)
	print "Folio "+folio
	print "Fecha in: "+fechaIn
	print "Placa "+placa
	#Insertamos en la tabla Centro Comercial
	query="INSERT INTO \"boletoexpedidora\"( fol_bol_exp, fec_bol_exp, pla_bol_exp) VALUES ( '"+folio+"', '"+fechaIn+"','"+placa+"');"
	print "\t Comienza el query..."
	objetoConexion = con.Conexion()
	f = objetoConexion.execQuery(query)
	if(f<0):
		print("Error: Los datos no se guardaron en Centro comercial")
	else:
		print "\t----Exito al insertar en BOleto expedidora"
		#Insertamos en la expedidora primero necesitamos saber cual es el ID DE CENTRO COMERCIAL QUE LE PUSIMOS
		query="SELECT id_cen_com  FROM \"CentroComercial\"  WHERE cen_com_nom='"+nombrePlaza+"' ;"
		objetoConexion = con.Conexion()
		resultado=objetoConexion.doQuery(query)
		if resultado==-1:
			print " ERRO DE QUERY"
			pass
		else:
			print ("\t----EL Id de centro comercial: "+str(resultado[0][0]))
			ID_cen_com_querybase=int(resultado[0][0])
			q = "SELECT MAX(id_bol_exp) FROM \"boletoexpedidora\";"
			conexion = con.Conexion()
			q = conexion.doQuery(q)
			if q==-1:
				print "ERROR QUERY 3"
			else:
				print (str(q[0][0]))
				id_bol_last=str(q[0][0])
				query="UPDATE \"Expedidora\"   SET id_exp_bol='"+str(id_bol_last)+"'  WHERE id_exp='"+str(numeroTerminal)+"' AND id_exp_cc='"+str(ID_cen_com_querybase)+"';"
				objetoConexion = con.Conexion()
				f = objetoConexion.execQuery(query)
				if(f<0):
					print("Error: El boleto no se guardo en expendidora")
				else:
					print "\t----Exito al insertar en expedidora"
	print "\t Termina el query..."

print terminalEnt
print PATH_NOMBRE_PLAZA
#insertarBoleto(PATH_NOMBRE_PLAZA,terminalEnt,"AG:300",'12/02/2017','JJJO')
#elijeCorte1PorDia("2017-01-03")
