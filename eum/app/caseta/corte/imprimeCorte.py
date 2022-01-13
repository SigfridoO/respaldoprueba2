# -*- coding: utf-8 -*-
"""
Estacionamientos unicos de México
Este archivo es para remplaar a acceso4.py
Funcion: 		Funcion de imprimir boleto
Descripcion:	

Funciones que se pueden usar:
	1) imprimirBoletoT tiempo corto formato largo
	2) imprimirBoleto  tiempo largo formato pequeño

"""
from escposprinter import *#original funcional
import tratarImagen as imagen
import configuracionEXP as archivoConfiguracion
#import time
#import psycopg2, psycopg2.extras
import fechaUTC as hora
#import datetime

import psycopg2
#from datetime import datetime
#from datetime import timedelta
from datetime import datetime, date, timedelta
import time,os	
import requests

ruta =  os.path.join(os.path.dirname(os.path.abspath(__file__)))
ruta = ruta + "/"
def obtenerUsuario(ruta):
	lista = ruta.split("/")
	return "/"+lista[1]+"/"+lista[2]+"/"	
rutaUsuario = obtenerUsuario(ruta)
print(rutaUsuario)


print("Obteniendo corte...")
PATH_NOMBRE_PLAZA=str(archivoConfiguracion.getName()).replace('\n','')
PATH_NUMERO_TERMINAL=str(archivoConfiguracion.getNumTer()).replace('\n','')
PATH_CODIGOS_QR="/home/pi/Documents/eum/app/caseta/EUM_EXPE/CodigosQR/outputQR.png"

conn = psycopg2.connect(database='caseta',user='postgres',password='Postgres3UMd6', host='localhost')
cur = conn.cursor()

#Generic = printer.Usb(0x0519,0x0001)
print("ImprimeCorte.py")


def imprimirHeader():
	Generic = printer.Usb(0x0519,0x0001)
	Generic.set(size='2x', align='center')
	Generic.text('Bienvenido \n'+str(PATH_NOMBRE_PLAZA)+'\n')
	Generic.set(size='normal',align='center')
	Generic.text("La empresa no se hace responsable por objetos\npersonales,fallas mecanicas  y/o  electricas,\nsiestros ocasionados por derrumedbes,temblores,\nterremotos o fenomenos naturales,asi como ro-\nbo de accesorios o vandalismo en su vehiculo.\n")
	Generic.text("Por robo total de acuerdo a los terminos  del\nseguro contratado.Boleto Perdido.Se entregara\nel  vehiculo  a quien acredite la  propiedad.\nCosto del boleto perdido es de $100.00\n")
	Generic.text("Al recibir este boleto acepta las condiciones\ndel seguro contra robo total. PARKING TIP S.A\nDE  C.V.  -R.F.C PTI120210571. Escobillera 13\nCol.Paseos de Churubusco Iztapalapa CDMX C.P.\n09030 Horario de Lunes-Domingo de 7 a 22 hrs \n")

def imprimirQR(noBol,terminalEnt,fechaIn,horaEnt):
	Generic = printer.Usb(0x0519,0x0001)
	Generic.text('Expedidora #'+PATH_NUMERO_TERMINAL+'\n')
	Generic.text('Folio: GM'+str(noBol)+' '+fechaIn+' '+horaEnt +'\n')
	Generic.qr(noBol+"\n"+terminalEnt+"\n"+fechaIn+"\n"+horaEnt)
	Generic.cut()

#imprimirHeader()
#imprimirQR("GM:12","3","21/03/2017","8:00:00")

def imprimirBoletoT(folio,terminal,fecha):
	Generic = printer.Usb(0x0519,0x0001)
	codQR=imagen.cambiarTamQR(PATH_CODIGOS_QR)
	
	Generic = printer.Usb(0x0519,0x0001)
	Generic.set(size='2x', align='center')
	Generic.text('Bienvenido \n'+str(PATH_NOMBRE_PLAZA)+'\n')
	Generic.set(size='normal',align='center')
	Generic.text("La empresa no se hace responsable por objetos\npersonales,fallas mecanicas  y/o  electricas,\nsiestros ocasionados por derrumbes,temblores,\nterremotos o fenomenos naturales,asi como ro-\nbo de accesorios o vandalismo en su vehiculo.\n")
	Generic.text("Por robo total de acuerdo a los terminos  del\nseguro contratado.Boleto Perdido.Se entregara\nel  vehiculo  a quien acredite la  propiedad.\nCosto del boleto perdido es de $100.00\n")
	Generic.text("Al recibir este boleto acepta las condiciones\ndel seguro contra robo total. PARKING TIP S.A\nDE  C.V.  -R.F.C PTI120210571. Escobillera 13\nCol.Paseos de Churubusco Iztapalapa CDMX C.P.\n09030 Horario de Lunes-Domingo de 7 a 22 hrs \n")
	horaActual= time.strftime("%H:%M:%S")
	Generic.text('Folio: '+str(folio)+'\n')
	Generic.text('Expedirora #'+PATH_NUMERO_TERMINAL+' '+fecha+' '+horaActual +'\n')
	Generic.image(codQR)
	Generic.cut()
	
	
def imprimirBoletoC2(fecha,horaEntrada,costillo,folio,expedidora):
	global Generic
	#Generic = printer.Usb(0x0519,0x0001)
	print ("Bienvenido \n "+PATH_NOMBRE_PLAZA+"\n")
	print ("Expedirora: "+PATH_NUMERO_TERMINAL+"\n")
	print (fecha +"\n")
	#Generic = printer.Usb(0x0519,0x0001)
	Generic.set(size='2x', align='center')
	Generic.text(str(PATH_NOMBRE_PLAZA)+'\n\n')
	Generic.set(size='normal',align='center')
	
	#Generic.text('--------------------------------\n')
	#Generic.text("La empresa no se hace responsable por objetos\npersonales,fallas mecanicas  y/o  electricas,\nsiestros ocasionados por derrumbes,temblores,\nterremotos o fenomenos naturales,asi como ro-\nbo de accesorios o vandalismo en su vehiculo.\n")
	#Generic.text("Por robo total de acuerdo a los terminos  del\nseguro contratado.Boleto Perdido.Se entregara\nel  vehiculo  a quien acredite la  propiedad.\nCosto del boleto perdido es de $100.00\n")
	#Generic.text("Al recibir este boleto acepta las condiciones\ndel seguro contra robo total. PARKING TIP S.A\nDE  C.V.  -R.F.C PTI120210571. Escobillera 13\nCol.Paseos de Churubusco Iztapalapa CDMX C.P.\n09030 Horario de Lunes-Domingo de 7 a 22 hrs \n")
	horaActual= time.strftime("%H:%M:%S")
	Generic.text('Hora de entrada:'+horaEntrada +'    '+'Fecha: '+fecha+'\n'+'Hora de Pago:'+horaActual+'      '+'Pagado: $'+str(costillo)+'.00\n')	#Generic.image(codQR)
	Generic.qr(folio+"\n"+expedidora+"\n"+fecha+"\n"+horaEntrada+"\n"+horaActual+"\n"+str(costillo)+"\n")
	Generic.set(size='normal',align='center')
	Generic.text('\nPresentar al salir. Valido por 15 minutos\n')
	Generic.set(size='2x', align='center')
	Generic.text('Gracias por su visita!')
	Generic.cut()
	
	
def imprimirBoletoC(folio,terminal,fecha):
	Generic = printer.Usb(0x0519,0x0001)
	codQR=imagen.cambiarTamQR(PATH_CODIGOS_QR)
	print ("Bienvenido \n "+PATH_NOMBRE_PLAZA+"\n")
	print ("Terminos y condiciones")
	print ("Folio: "+str(folio)+"\n")
	print ("Expedirora: "+PATH_NUMERO_TERMINAL+"\n")
	print (fecha +"\n")
	print ("CODIGO QR: "+str(codQR))
	Generic = printer.Usb(0x0519,0x0001)
	Generic.set(size='2x', align='center')
	Generic.text(str(PATH_NOMBRE_PLAZA)+'\n\n')
	Generic.set(size='normal',align='center')
	
	#Generic.text('--------------------------------\n')
	#Generic.text("La empresa no se hace responsable por objetos\npersonales,fallas mecanicas  y/o  electricas,\nsiestros ocasionados por derrumbes,temblores,\nterremotos o fenomenos naturales,asi como ro-\nbo de accesorios o vandalismo en su vehiculo.\n")
	#Generic.text("Por robo total de acuerdo a los terminos  del\nseguro contratado.Boleto Perdido.Se entregara\nel  vehiculo  a quien acredite la  propiedad.\nCosto del boleto perdido es de $100.00\n")
	#Generic.text("Al recibir este boleto acepta las condiciones\ndel seguro contra robo total. PARKING TIP S.A\nDE  C.V.  -R.F.C PTI120210571. Escobillera 13\nCol.Paseos de Churubusco Iztapalapa CDMX C.P.\n09030 Horario de Lunes-Domingo de 7 a 22 hrs \n")
	horaActual= time.strftime("%H:%M:%S")
	Generic.text('Entrada:'+horaActual +'    '+'Fecha: '+fecha+'\n'+'Salida:'+horaActual+'    '+'Pagado: $100.00\n')
	Generic.image(codQR)
	
	Generic.set(size='normal',align='center')
	Generic.text('\nPresentar al salir. Valido por 15 minutos\n')
	Generic.set(size='2x', align='center')
	Generic.text('Gracias por su visita!')
	
	Generic.cut()


def imprimirBoleto(folio,terminal,fecha):
	Generic.set(size='2x', align='center')
	codQR=imagen.cambiarTamQR("output.png")
	Generic.set(size='2x',align='center')
	Generic.text("Macro Plaza"+"\n")
	Generic.text(" TECAMAC"+"\n")
	Generic.image("3.jpg")	
	Generic.set(size='normal')	
	Generic.text("Folio: "+str(folio)+"\n")
	Generic.text("Entrada: "+str(terminal)+"\n")
	Generic.text(fecha +"\n")
	Generic.set(size='2x', align='center')
	Generic.image(codQR)
	Generic.cut()
	pass


def header():
	Generic = printer.Usb(0x0519,0x0001)
	Generic.set(size='2x', align='center')
	Generic.text('Bienvenido \n'+str(PATH_NOMBRE_PLAZA))
	Generic.set(size='normal',align='center')

def footer():
	Generic.cut()

def informacionEXT():
	Generic.set(size='normal', align='center')
	Generic.text("Bienvenido\n\n")
	
def checale(fecha1,fecha2,folio):
	global cur,generic
	
	desglose_pagos = 0
	ingreso = 0
	detallesBoletos = ""
	turno = "Vespertino"
	cobrados = 0
	expedidos=0
	recuperados = 0
	tolerancias = 0
	locatarios = 0
	encargado = "1"
	sucursal = 16
	corteCaja=0
	detallesCorte=""
	
	Generic = printer.Usb(0x04b8,0x0202)
	#Generic = printer.Usb(0x0519,0x0001)
	fecha=hora.mostrarFechayHora()
	archivo = open("/home/pi/Documents/eum/app/caseta/NoCajero.txt", "r")
	idCajero=str(archivo.readline().rstrip("\n"))
	archivo.close()
	Generic.set(size='2x', align='center')
	Generic.text("INGRESO\n")
	Generic.text("TOTAL.\n\n")
	Generic.set(size='normal', align='center')
	Generic.text("Folio #"+str(folio)+"  "+fecha1+" - "+fecha2+"\n")
	Generic.text("Caja: "+str(idCajero)+"\n\n")
	cur.execute("select costo,COUNT(\"idBoleto\") from \"BOLETO\" where \"fechaExpedicion\" BETWEEN '"+fecha1+"' and '"+fecha2+"' group by costo ")
	for reg in cur: 
		print(reg[0],reg[1])
		Generic.text('Tarifa:'+str(reg[0])+'     '+' boletos cobrados:'+str(reg[1])+'\n\n')
		detallesCorte += str(reg[1])+" x "+str(reg[0])+" "
		
		
	cur.execute("select SUM(\"costo\") from \"BOLETO\" where \"fechaExpedicion\" BETWEEN '"+fecha1+"' and '"+fecha2+"'")
	for reg in cur: 
		#print("AAAS"reg[0])
		Generic.text('Dinero total:'+str(reg[0])+'\n\n')
		ingreso = reg[0]
	conn = psycopg2.connect(database='caseta',user='postgres',password='Postgres3UMd6', host='localhost')
	cur = conn.cursor()
	cur2 = conn.cursor()
	cur.execute("select tipo,COUNT(\"idBoleto\") from \"BOLETO\" where \"fechaExpedicion\" BETWEEN '"+fecha1+"' and '"+fecha2+"' group by tipo ")
	for rega in cur: 
		print("tipazos",rega[0],rega[1])
		cur2.execute("select nombre from \"TIPO\" where \"idTipo\"="+str(rega[0])+"")
		for reg in cur2: 
			print(reg[0])
		Generic.text('Tipo:'+str(reg[0])+'     '+' boletos cobrados:'+str(rega[1])+'\n\n')
		detallesCorte += str(rega[1])+" X "+str(reg[0])+" "
	
	cur.execute("select SUM(\"costo\") from \"BOLETO\" where \"fechaExpedicion\" BETWEEN '"+fecha1+"' and '"+fecha2+"'")
	for reg in cur: 
		print(reg[0])
		#Generic.text('Dinero total:'+str(reg[0])+'\n\n')

	Generic.cut()
	
	
	if(not expedidos):
		expedidos=0
	if(not recuperados):
		recuperados=0
	if(not tolerancias):
		tolerancias=0
	if(not locatarios):
		locatarios=0
	if(not ingreso):
		ingreso=0
	if(not detallesCorte):
		detallesCorte=0
	if(not detallesBoletos):
		detallesBoletos=0


	fechaHoy=time.strftime("%Y-%m-%d")
	horaHoy=time.strftime("%H:%M:%S")
	payload = {
		"turno": turno,
		"boletaje": expedidos,
		"recuperados": cobrados,
		"tolerancias": tolerancias,
		"locatarios": locatarios,
		"caja": 1,
		"created": fechaHoy+"T"+horaHoy,
		"ingreso": ingreso,
		"detalles": detallesCorte,
		"encargado": encargado,
		"sucursal_id": sucursal
	}
	#print(fechaInicio)
	time.sleep(1)





	r = requests.post("https://parkingtip.pythonanywhere.com/api/cortes/create/", json=payload)
	#r = requests.post("http://127.0.0.1:8000/api/cortes/create/", json=payload)
	print(r.text)




#hoy=datetime.datetime.today()
#ayer=hoy+datetime.timedelta(days=-1)
#m=str(ayer).split(" ")
#n=m[0].split("-")
#fechaayer=n[2]+"/"+n[1]+"/"+n[0]

#hoy=datetime.datetime.today()
#a=str(hoy).split(" ")
#b=a[0].split("-")
#fec=b[2]+"/"+b[1]+"/"+b[0]



#fecha1=fechaayer+" "+ time.strftime("%H:%M:%S")
#fecha2=fec+" 22:00:00"


infile = open(ruta+"fechaDeCorte.txt", 'r')
fecha_tmp=infile.readline().rstrip("\n")
fecha_tmp=fecha_tmp.split(",")
folio=fecha_tmp[1]

fecha_tmp=fecha_tmp[0]
#fecha_tmp=infile.readline()
infile.close()
fecha_hoy = str(date.today())
fecha_actual = time.strftime("%Y-%m-%d")
hora_actual = time.strftime("%H:%M:%S")
fecha_hora_actual = fecha_hoy + " " + hora_actual




#print("fechas:: ",fecha_tmp,fecha_hoy,fecha_hora_actual)
#shutil.copy(ruta+"fechaDeCorte.txt", ruta+"fechaDeCorte_intervalo_de_inicio.txt")


print(fecha_tmp,fecha_hora_actual)
#checale(fecha1,fecha_tmp)
checale(fecha_tmp,fecha_hora_actual,folio)

infile = open(ruta+"fechaDeCorte.txt", 'w')
infile.write(str(fecha_hora_actual)+","+str(int(folio)+1))
infile.close()
try:
	pass
	#checale(fecha1,fecha2)
except:
	pass
#imprimirBoletoC2(fe,he,str(costo),str(folio),str(expedidora))









"""




import psycopg2
from datetime import datetime
from datetime import timedelta
import time
import requests

turno="Vespertino"
encargado="1"
sucursal=9

fechaHoy=time.strftime("%Y-%m-%d")
horaHoy=time.strftime("%H:%M:%S")
fechaInicio='2021-03-03'#un dia antes
fechaFin='2021-03-05'
fechaQuery='2019-01-09'
#fechaQuery=fechaHoy
fechaInicio = datetime.strptime(fechaInicio, '%Y-%m-%d').date()
fechaFin = datetime.strptime(fechaFin, '%Y-%m-%d')

while (fechaInicio != fechaFin):
    fechaInicio = fechaInicio + timedelta(days=1)
    fechaQuery = str(fechaInicio)
	
    queryExpedidos="select count(idboleto) from boleto where fechaexpedicion::date='{}'".format(fechaQuery)
    queryCobrados="select count(pagos) from pagos where fechaexpedicion::date='{}'".format(fechaQuery)
    queryRecuperados="select count(idboleto) from boleto where fechaexpedicion::date='{}' and idestado=4".format(fechaQuery)
    queryTolerancias="select count(idboleto) from boleto where fechaexpedicion::date='{}' and idestado=7".format(fechaQuery)
    queryLocatarios="select count(idboleto) from boleto where fechaexpedicion::date='{}' and idestado=6".format(fechaQuery)
    queryCorteCaja="select sum(monto) from pagos where fechapago::date='{}' and fechaexpedicion::date='{}'".format(fechaQuery,fechaQuery)
    queryDetallesCorte="SELECT monto,count(monto) from pagos where fechapago::date='{}' and fechaexpedicion::date='{}' group by monto".format(fechaQuery,fechaQuery)
    connection = psycopg2.connect(user='eumdb', password='Ingenieria3UMd6', database='dbeum_tecamac', host='localhost')
    cursor = connection.cursor()
    cursor.execute(queryExpedidos)
    expedidos = cursor.fetchone()[0]
    cursor.execute(queryRecuperados)
    recuperados = cursor.fetchone()[0]
    cursor.execute(queryCobrados)
    cobrados = cursor.fetchone()[0]
    cursor.execute(queryTolerancias)
    tolerancias = cursor.fetchone()[0]
    cursor.execute(queryLocatarios)
    locatarios = cursor.fetchone()[0]
    cursor.execute(queryCorteCaja)
    corteCaja = cursor.fetchone()[0]
    cursor.execute(queryDetallesCorte)
    detallesCorte=""
    for reg in cursor:
        detallesCorte += str(reg[1])+" x "+str(reg[0])+" "
    connection.close()
    print(fechaQuery)
    print(expedidos)
    print(recuperados)
    print(tolerancias)
    print(locatarios)
    print(corteCaja)
    print(detallesCorte)

    if(not expedidos):
        expedidos=0
    if(not recuperados):
        recuperados=0
    if(not tolerancias):
        tolerancias=0
    if(not locatarios):
        locatarios=0
    if(not corteCaja):
        corteCaja=0
    if(not detallesCorte):
        detallesCorte=0


    payload = {
        "turno": turno,
        "boletaje": expedidos,
        "recuperados": cobrados,
        "tolerancias": tolerancias,
        "locatarios": locatarios,
        "caja": 1,
        "created": fechaQuery+"T"+horaHoy,
        "ingreso": corteCaja,
        "detalles": detallesCorte,
        "encargado": encargado,
        "sucursal_id": sucursal
    }
    #print(fechaInicio)
    time.sleep(1)





    r = requests.post("https://parkingtip.pythonanywhere.com/api/cortes/create/", json=payload)
    #r = requests.post("http://127.0.0.1:8000/api/cortes/create/", json=payload)
    print(r.text)


"""

