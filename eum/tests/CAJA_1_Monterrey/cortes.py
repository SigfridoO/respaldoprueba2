from datetime import datetime
import time, os
import commands
import sys
import psycopg2	
import getpass
from escposprinter import *
import configuracionEXP as archivoConfiguracion

import conexion as con

#fein="14/02/2017"
#feou="14/02/2017"
#miterminalcorte=7
#user=43

HORA_INICIO_TURNO_MATUTINO="06:30:00"
HORA_FIN_TURNO_MATUTINO="15:00:00"
HORA_INICIO_TURNO_VESPERTINO="14:30:00"
HORA_FIN_TURNO_VESPERTINO="23:00:00"

FECHA_ACTUAL=time.strftime("%d/%m/%Y")
HORA_ACTUAL= time.strftime("%H:%M:%S")

TerminalGlobal="0"	#Se modifica en la funcion puesto que recibe el numero de terminal
PATH_NOMBRE_PLAZA=str(archivoConfiguracion.getName())
TerminalGlobal=str(archivoConfiguracion.getNumTer())

Generic = printer.Usb(0x0519,0x0001)
#Generic = printer.Usb(0x04b8,0x0202) #DESCOMENTAR ESTO 04b8:0202


def header():
	FECHA_ACTUAL=time.strftime("%d/%m/%Y")
	HORA_ACTUAL= time.strftime("%H:%M:%S")
	Generic.set(size='2x', align='center')
	Generic.text(PATH_NOMBRE_PLAZA)
	Generic.text('Corte de Caja \n')
	Generic.set(size='normal')
	Generic.text('Fecha:'+FECHA_ACTUAL+'\n')
	Generic.text('Hora: '+HORA_ACTUAL+'\n')
	Generic.text('Caja: '+TerminalGlobal+'\n')


def footer():
	Generic.set(align='left')
	Generic.text("    					  \n")
	Generic.text("     Firma Supervisor        Firma Cajero\n")
	Generic.text("    					  \n")
	Generic.text("    					  \n")
	Generic.text("   ===================	  ======================\n")
	Generic.cut()



def elijeCorte(tipoCorte, mifechacorte1, mifechacorte2, miterminalcorte, user):
	imprimirTarifas()
	for x in range(0,2):	#para que se imprima dos veces
		if tipoCorte==1:
			corteDeCaja(mifechacorte1,miterminalcorte,user)		
		if tipoCorte==2:

			cortePorTarifa(mifechacorte1,mifechacorte2,miterminalcorte,user)		
		if tipoCorte==3:
			corteEntreFechas(mifechacorte1,mifechacorte2,miterminalcorte,user)
			
		if tipoCorte==4:
			print "CORTE MAT"
			corteMatutino(mifechacorte1,miterminalcorte,user,HORA_INICIO_TURNO_MATUTINO,HORA_FIN_TURNO_MATUTINO)
		if tipoCorte==5:
			print "CORTE VES"
			corteVespertino(mifechacorte1,miterminalcorte,user,HORA_INICIO_TURNO_VESPERTINO,HORA_FIN_TURNO_VESPERTINO)



def corteDeCaja(fin,miterminalcorte,user):
	var1=str(fin)
	var2=str(miterminalcorte)
	global TerminalGlobal
	TerminalGlobal=str(var2)
	query="SELECT US.nom_usu,US.app_usu,US.apm_usu,	bol.id_tar_bol ,count(bol.id_bol),	Sum(bol.tot_bol)  FROM \"Boleto\" bol   join \"Usuario\"US on (bol.id_usu_bol=US.id_usu) where bol.out_fec_bol='"+var1+"' AND  bol.out_hor_bol between '00:00:00' and '23:59:00'   group by US.nom_usu,US.app_usu,US.apm_usu, bol.id_tar_bol   ;"
	objetoConexion = con.Conexion()
	resultado=objetoConexion.doQuery(str(query))
	registros=resultado
	if resultado==-1:
		print " ERRO DE QUERY"
		pass
	else:
		aux=0			#Para moverse entre los registros
		usuAux=""		#Para hacer el formato correcto entre usuario y comparar para que no se imprima de nuevo
		ntotalBol=0
		totalFinal=0
		header()
		for x in registros:
			print registros[aux]
			usu=registros[aux][0]#nombre
			app=registros[aux][1]#app
			apm=registros[aux][2]#apm
			tar=registros[aux][3]#idtar
			nbv=registros[aux][4]#numbol
			tot=registros[aux][5]#subtotal
			if usuAux==str(usu) :
				print str(tar)+"  "+str(nbv)+"  "+str(tot)
				Generic.text("Tarifa:"+str(tar)+"  T. Cobrados:"+str(nbv)+" SubTotal:$"+str(tot)+'\n')
			else:
				print str(usu)+"\n"+str(tar)+"  "+str(nbv)+"  "+str(tot)
				Generic.text("Cajero:"+str(usu)+" "+str(app)+" "+str(apm)+"\nTarifa:"+str(tar)+"  T. Cobrados:"+str(nbv)+" SubTotal:$"+str(tot)+'\n')
			aux=aux+1
			usuAux=str(usu)
			ntotalBol=ntotalBol+nbv
			totalFinal=totalFinal+tot
		print "-----Bol total:"+str(ntotalBol)+" total $"+str(totalFinal)
		Generic.text("----Num.Tot.Boletos cobrados:"+str(ntotalBol)+" Total $"+str(totalFinal))
		footer()
	pass

#corteDeCaja("20/02/2017",8,43)

def cortePorTarifa(fin,fout,t,user):
	var1=str(fin)
	#falta gregar bol.id_tar_bol='1' AND por cada tarifa
	query="SELECT US.nom_usu,US.app_usu,US.apm_usu,	bol.id_tar_bol ,count(bol.id_bol),	Sum(bol.tot_bol)  FROM \"Boleto\" bol   join \"Usuario\"US on (bol.id_usu_bol=US.id_usu) where bol.out_fec_bol='"+var1+"' AND  bol.out_hor_bol between '00:00:00' and '23:59:00'   group by US.nom_usu,US.app_usu,US.apm_usu, bol.id_tar_bol   ;"
	objetoConexion = con.Conexion()
	resultado=objetoConexion.doQuery(str(query))
	registros=resultado
	if resultado==-1:
		print " ERRO DE QUERY"
		pass
	else:
		aux=0			#Para moverse entre los registros
		usuAux=""		#Para hacer el formato correcto entre usuario y comparar para que no se imprima de nuevo
		ntotalBol=0
		totalFinal=0
		header()
		for x in registros:
			print registros[aux]
			usu=registros[aux][0]#nombre
			app=registros[aux][1]#app
			apm=registros[aux][2]#apm
			tar=registros[aux][3]#idtar
			nbv=registros[aux][4]#numbol
			tot=registros[aux][5]#subtotal
			if usuAux==str(usu) :
				print str(tar)+"  "+str(nbv)+"  "+str(tot)
				Generic.text("Tarifa:"+str(tar)+"  T. Cobrados:"+str(nbv)+" SubTotal:$"+str(tot)+'\n')
			else:
				print str(usu)+"\n"+str(tar)+"  "+str(nbv)+"  "+str(tot)
				Generic.text("Cajero:"+str(usu)+" "+str(app)+" "+str(apm)+"\nTarifa:"+str(tar)+"  T. Cobrados:"+str(nbv)+" SubTotal:$"+str(tot)+'\n')
			aux=aux+1
			usuAux=str(usu)
			ntotalBol=ntotalBol+nbv
			totalFinal=totalFinal+tot
		print "-----Bol total:"+str(ntotalBol)+" total $"+str(totalFinal)
		Generic.text("----Num.Tot.Boletos cobrados:"+str(ntotalBol)+" Total $"+str(totalFinal))
		footer()
pass


def corteEntreFechas(fin,fout,t,user):
	global TerminalGlobal
	TerminalGlobal=str(t)
	var1=str(fin)
	var2=str(fout)
	var3=str(t)
	
	query="SELECT US.nom_usu,US.app_usu,US.apm_usu,	bol.id_tar_bol ,count(bol.id_bol),	Sum(bol.tot_bol)  FROM \"Boleto\" bol   join \"Usuario\"US on (bol.id_usu_bol=US.id_usu) where  out_fec_bol between '"+var1+"' and '"+var2+"'    group by US.nom_usu,US.app_usu,US.apm_usu, bol.id_tar_bol   ;"
	objetoConexion = con.Conexion()
	resultado=objetoConexion.doQuery(str(query))
	registros=resultado
	if resultado==-1:
		print " ERRO DE QUERY"
		pass
	else:
		aux=0			#Para moverse entre los registros
		usuAux=""		#Para hacer el formato correcto entre usuario y comparar para que no se imprima de nuevo
		ntotalBol=0
		totalFinal=0
		header()
		for x in registros:
			print registros[aux]
			usu=registros[aux][0]#nombre
			app=registros[aux][1]#app
			apm=registros[aux][2]#apm
			tar=registros[aux][3]#idtar
			nbv=registros[aux][4]#numbol
			tot=registros[aux][5]#subtotal
			if usuAux==str(usu) :
				print str(tar)+"  "+str(nbv)+"  "+str(tot)
				Generic.text("Tarifa:"+str(tar)+"  T. Cobrados:"+str(nbv)+" SubTotal:$"+str(tot)+'\n')
			else:
				print str(usu)+"\n"+str(tar)+"  "+str(nbv)+"  "+str(tot)
				Generic.text("Cajero:"+str(usu)+" "+str(app)+" "+str(apm)+"\nTarifa:"+str(tar)+"  T. Cobrados:"+str(nbv)+" SubTotal:$"+str(tot)+'\n')
			aux=aux+1
			usuAux=str(usu)
			ntotalBol=ntotalBol+nbv
			totalFinal=totalFinal+tot
		print "-----Bol total:"+str(ntotalBol)+" total $"+str(totalFinal)
		Generic.text("----Num.Tot.Boletos cobrados:"+str(ntotalBol)+" Total $"+str(totalFinal))
		footer()
	pass

pass

#corteEntreFechas("17/02/2017","20/02/2017",8,43)

def corteMatutino(fein,miterminalcorte,user,HORA_INICIO_TURNO_MATUTINO,HORA_FIN_TURNO_MATUTINO):
	var1=str(fein)
	var2=str(miterminalcorte)
	user=str(user)
	varHI=str(HORA_INICIO_TURNO_MATUTINO)
	varHF=str(HORA_FIN_TURNO_MATUTINO)
	query1="SELECT count( id_bol)  FROM \"Boleto\" WHERE out_fec_bol='"+var1+"'AND   out_ter_bol='"+var2+"' AND out_hor_bol BETWEEN '"+varHI+"' AND '"+varHF+"';"
	objetoConexion = con.Conexion()
	resultado1=objetoConexion.doQuery(str(query1))
	
	query2="SELECT sum( tot_bol)  FROM \"Boleto\" WHERE out_fec_bol='"+var1+"' AND  out_ter_bol='"+var2+"' AND out_hor_bol BETWEEN '"+varHI+"' AND '"+varHF+"';"
	objetoConexion = con.Conexion()
	resultado2=objetoConexion.doQuery(str(query2))
	
	query3="SELECT US.nom_usu,US.app_usu,US.apm_usu,bol.id_tar_bol ,count(bol.id_bol),Sum(bol.tot_bol)  FROM \"Boleto\" bol   join \"Usuario\"US on (bol.id_usu_bol=US.id_usu) where out_fec_bol='"+var1+"' AND  out_ter_bol='"+var2+"' AND bol.out_hor_bol between '"+varHI+"' and  '"+varHF+"'    group by US.nom_usu,US.app_usu,US.apm_usu,  bol.id_tar_bol   ;"
	objetoConexion = con.Conexion()
	resultado3=objetoConexion.doQuery(str(query3))
	
	if resultado1==-1 or resultado2==-1 or resultado3==-1:
		print "***********ERRO DE QUERY POR TURNO MATUTINO"
		pass
	else:
		print "Query 3"+ str(resultado3)
		print ("\t-- Boletos vendidos: "+str(resultado1[0][0])+" Total:$"+str(resultado2[0][0]))
		registros=resultado3
		aux=0			#Para moverse entre los registros
		usuAux=""		#Para hacer el formato correcto entre usuario y comparar para que no se imprima de nuevo
		global TerminalGlobal
		TerminalGlobal=str(var2)
		header()
		for x in registros:
			print registros[aux]
			usu=registros[aux][0]
			usu1=registros[aux][1]
			usu2=registros[aux][2]
			tar=registros[aux][3]
			nbv=registros[aux][4]
			tot=registros[aux][5]
			if usuAux==str(usu) :
				print str(tar)+"  "+str(nbv)+"  "+str(tot)
				Generic.text("Tarifa:"+str(tar)+"  T. Cobrados:"+str(nbv)+" SubTotal:$"+str(tot)+'\n')
			else:
				print str(usu)+"\n"+str(tar)+"  "+str(nbv)+"  "+str(tot)
				Generic.text("Cajero:"+str(usu)+" "+str(usu1)+" "+str(usu2)+"\nTarifa:"+str(tar)+"  T. Cobrados:"+str(nbv)+" SubTotal:$"+str(tot)+'\n')
			aux=aux+1
			usuAux=str(usu)
		Generic.text("\t T. Totales Cobrados: "+str(resultado1[0][0])+" Total:$"+str(resultado2[0][0]))
		footer()
		pass
	pass
	
pass

def corteVespertino(fein,miterminalcorte,user,HORA_INICIO_TURNO_VESPERTINO,HORA_FIN_TURNO_VESPERTINO):
	var1=str(fein)
	var2=str(miterminalcorte)
	user=str(user)
	varHI=str(HORA_INICIO_TURNO_VESPERTINO)
	varHF=str(HORA_FIN_TURNO_VESPERTINO)
	query1="SELECT count( id_bol)  FROM \"Boleto\" WHERE out_fec_bol='"+var1+"'AND   out_ter_bol='"+var2+"' AND out_hor_bol BETWEEN '"+varHI+"' AND '"+varHF+"';"
	objetoConexion = con.Conexion()
	resultado1=objetoConexion.doQuery(str(query1))
	
	query2="SELECT sum( tot_bol)  FROM \"Boleto\" WHERE out_fec_bol='"+var1+"' AND  out_ter_bol='"+var2+"' AND out_hor_bol BETWEEN '"+varHI+"' AND '"+varHF+"';"
	objetoConexion = con.Conexion()
	resultado2=objetoConexion.doQuery(str(query2))
	
	query3="SELECT US.nom_usu,US.app_usu,US.apm_usu,bol.id_tar_bol ,count(bol.id_bol),Sum(bol.tot_bol)  FROM \"Boleto\" bol   join \"Usuario\"US on (bol.id_usu_bol=US.id_usu) where out_fec_bol='"+var1+"' AND  out_ter_bol='"+var2+"' AND bol.out_hor_bol between'"+varHI+"' and  '"+varHF+"'    group by US.nom_usu,US.app_usu,US.apm_usu,  bol.id_tar_bol   ;"
	objetoConexion = con.Conexion()
	resultado3=objetoConexion.doQuery(str(query3))
	
	if resultado1==-1 or resultado2==-1 or resultado3==-1:
		print "***********ERRO DE QUERY POR TURNO MATUTINO"
		pass
	else:
		print "Query 3"+ str(resultado3)
		print ("\t-- Boletos vendidos: "+str(resultado1[0][0])+" Total:$"+str(resultado2[0][0]))
		registros=resultado3
		aux=0			#Para moverse entre los registros
		usuAux=""		#Para hacer el formato correcto entre usuario y comparar para que no se imprima de nuevo
		global TerminalGlobal
		TerminalGlobal=str(var2)
		header()
		for x in registros:
			print registros[aux]
			usu=registros[aux][0]
			usu1=registros[aux][1]
			usu2=registros[aux][2]
			tar=registros[aux][3]
			nbv=registros[aux][4]
			tot=registros[aux][5]
			if usuAux==str(usu) :
				print str(tar)+"  "+str(nbv)+"  "+str(tot)
				Generic.text("Tarifa:"+str(tar)+"  T. Cobrados:"+str(nbv)+" SubTotal:$"+str(tot)+'\n')
			else:
				print str(usu)+"\n"+str(tar)+"  "+str(nbv)+"  "+str(tot)
				Generic.text("Cajero:"+str(usu)+" "+str(usu1)+" "+str(usu2)+"\nTarifa:"+str(tar)+"  T. Cobrados:"+str(nbv)+" SubTotal:$"+str(tot)+'\n')
			aux=aux+1
			usuAux=str(usu)
		Generic.text("\t T. Totales Cobrados: "+str(resultado1[0][0])+" Total:$"+str(resultado2[0][0]))
		footer()
		pass
	pass
	
pass


def  imprimirTarifas():
	query=	"SELECT id_tar, des_tar, pol_tar  FROM  \"CTarifas\" ;";
	objetoConexion = con.Conexion()
	resultado=objetoConexion.doQuery(str(query))
	registros=resultado
	aux=0
	if resultado==-1:
		print " ERRO DE QUERY"
		pass
	else:
		header()
		Generic.text("CATALOGO DE TARIFAS\n")
		print "Tarifas disponibles"
		for x in registros:
			print "------Descripcion Tarifa-----"
			Generic.text("-----------------------\n")
			#print registros[aux]
			idTarifa=registros[aux][0]
			nombreTar=registros[aux][1]
			desc=registros[aux][2]
			print ">"+str(nombreTar)
			print ">Numero de Tarifa: "+str(idTarifa)
			print ">Descripcion "+str(desc)
			Generic.text('>Numero de Tarifa: '+str(idTarifa)+'\n')
			Generic.text('> '+str(nombreTar)+'\n')
			#Generic.text('>Descripcion '+str(desc)+'\n')
			aux=aux+1
		Generic.cut()
	

#corteMatutino(fein,miterminalcorte,user,HORA_INICIO_TURNO_MATUTINO,HORA_FIN_TURNO_MATUTINO)
#corteVespertino(fein,miterminalcorte,user,HORA_INICIO_TURNO_VESPERTINO,HORA_FIN_TURNO_VESPERTINO)
