# -*- coding: utf-8 -*-
"""
Funciones de validacion de datos de formularios
Return False si no hubo insidencias
Return True si existio alguna insidencia
"""
import re
import easygui as eg
import time 

letras="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\n"
letrasMIN="abcdefghijklmnopqrstuvwxyz\n"
numeros="0123456789\n"
caracteresEspaciales="ñ|@·~½¬{[]}},.+´/*"


def registroSalida(noBol,terminalEntrada,fechaIn,horaIn,tarifa):
	noBol=str(noBol).replace('\n','')
	terminalEntrada=str(terminalEntrada).replace('\n','')
	fechaIn=str(fechaIn).replace('\n','')
	horaIn=str(horaIn).replace('\n','')
	tarifa=str(tarifa).replace('\n','')
	noBol=str(noBol)
	#Primero validar que las fechas sean buenas
	if validarNumeros(noBol)!= True:
		ventana(" ----- ERROR DE DATOS -----","\t\tEl Boleto  "+str(noBol)+ " es invalido \n\t\t Porfavor ingreselo con números")
		return True
		pass
	if validarNumeros(terminalEntrada)!= True:
		ventana(" ----- ERROR DE DATOS -----","\t\tLa terminal de entrada no corresponde >> "+str(terminalEntrada)+ "  es invalida")
		return True
		pass
	if validarFormatoFecha(fechaIn)!= True:
		ventana(" ----- ERROR DE DATOS -----","\t\tEl  formato de la fecha es incorrecta >> "+str(fechaIn)+ " \n\t\t utiliza formato dd/mm/aaaa \n\t\t no te olvides de rellenar con ceros \n\t\t Ejemplo: 07/12/2017")
		return True
		pass
	if validarFormatoHora(horaIn)!= True:
		ventana(" ----- ERROR DE DATOS -----","\t\tLa hora  "+str(horaIn)+ " es incorrecta\n\t\tutiliza formato hh:mm:ss \n\t\t no te olvides de rellenar con ceros \n\t\t Ejemplo: 07:25:05")
		return True
		pass
	if validarTarifa(tarifa)!= True:
		ventana(" ----- ERROR DE DATOS -----","\t\tLa tarfia >>  "+str(tarifa)+ "es invalida")
		return True
		pass
	if validarNumeros(noBol) and validarNumeros(terminalEntrada) and validarFormatoFecha(fechaIn) and validarFormatoHora(horaIn) and validarTarifa(tarifa)  and validarFechaInFechaOut(fechaIn) and validarHoraIn(horaIn):
		#ventana("DATOS CORRECTOS"," Ningun error \n\t\t\t\t SE REGISTRO EL BOLETO EXITOSAMENTE")
		return False
		pass



def validarBolPer(marca,placas,modelo,licencia,nombre,telefono):
	placas=str(placas).replace('\n','')
	modelo=str(modelo).replace('\n','')
	licencia=str(licencia).replace('\n','')
	nombre=str(nombre).replace('\n','')
	telefono=str(telefono).replace('\n','')
	if validarMarca(marca)!= True:
		ventana(" ----- ERROR DE DATOS -----","La marca del carro "+str(marca)+ " es invalida")
		return True
		pass	
	if validarPlacas(placas)!= True:
		ventana(" ----- ERROR DE DATOS -----","Las placas del carro "+str(placas)+ " son invalidas escriba en Mayúsculas")
		return True
		pass
	if validarMarca(modelo)!= True:
		ventana(" ----- ERROR DE DATOS -----","El modelo del carro "+str(modelo)+ " es invalido")
		return True
		pass
	if validarNombre(nombre)!= True:
		ventana(" ----- ERROR DE DATOS -----","La nombre  "+str(nombre)+ " es invalido")
		return True
		pass
	if validarTelefono(telefono)!= True:
		ventana(" ----- ERROR DE DATOS -----","La telefono  "+str(telefono)+ " es invalido")
		return True
		pass					
	
	if  validarMarca(marca) and validarPlacas(placas) and validarNumeros(modelo) and validarNombre(nombre) and validarTelefono(telefono):
		ventana("DATOS CORRECTOS","  Ningun error \n\t\tSe valido Correctamente el Boleto perdido")
		return False
		pass
	
	pass


def validarFechaInFechaOut(fin):
	fechaActual=time.strftime("%d/%m/%Y")   #OBETENEMOS LA FECHA ACTUAL
	fin=str(fin)	#OBETENEMOS LA FECHA 
	#Verificamos que la fecha no sea mayor que la actual
	if fin>fechaActual:
		return False
	else:
		return True

#print validarFechaInFechaOut("17/03/2017")

def validarHoraIn(hin):
	horaActual= time.strftime("%H:%M:%S")
	hin=str(hin)
	print hin
	print horaActual
	if hin>horaActual:
		return False
	else:
		return True
	
#print validarHoraIn("18:10:00")

def validarNumeros(cadena):
	cadena=str(cadena)
	for x in range(len(cadena)):
		if cadena[x] not in numeros:
			print "	Error -*Un argumento enetero tiene letras*-"
			return False
			pass
	return True			
	pass


def validarLetras(cadena):
	cadena=str(cadena)
	for x in range(len(cadena)):
		if cadena[x] not in letras:
			print "	Error -*Un argumento enetero tiene *-"
			return False
			pass
	return True			
	pass	

def validarUser(cadena):
	cadena=str(cadena)
	for x in range(len(cadena)):
		if cadena[x] in caracteresEspaciales:
			print "	Error -*Un argumento enetero caracteresEspaciales xD *-"
			return False
			pass
	return True			
	pass
	pass

def validarFormatoFecha(date):
    """    Funcion para validar una fecha en formato:   dd/mm/yyyy   """
    for format in ['%d/%m/%Y']:
        try:
            result = time.strptime(date, format)
            cadena=str(date)
            fecha = re.compile(r'^([0][1-9]|[12][0-9]|3[01])/([0][1-9]|1[012])/(([2][0][0-9]\d))$')
            # validando dd/mm/aaaa
            if fecha.search(cadena) != None:
            	print "correctofecha formato!"
            	return True
            else:
            	print "mal fecha formato!"
            	return False
        except:
            pass
    return False
#print validarFormatoFecha("17/01/2017")

def validarFormatoHora(cadena):
	cadena=str(cadena)
	cadena=cadena.strip('\n')
	"""
	Funcion para validar una fecha en formato:
	hh:mm:ss
	"""
	for format in ['%H:%M:%S']:
		try:
			result = time.strptime(cadena, format)
			return True
		except:
			pass
	return False

def validarTarifa(cadena):
	cadena=str(cadena)
	if cadena !=0: 
		return True 
	else:
		return False
	pass


def validarMarca(cadena):
	cadena=str(cadena)
	if re.match('^[(A-Za-z0-9\ \-)]', cadena) :
		return True
	else:
		return False
	pass
	pass
def validarPlacas(cadena):
	cadena=str(cadena)
	for x in range(len(cadena)):
		if cadena[x] in letrasMIN:
			print "	Error -*No se pueden tener minusculas en placas o Licencia xD *-"
			return False
			pass
	return True	
	pass
def validarNombre(cadena):
	cadena=str(cadena)
	for x in range(len(cadena)):
		if (cadena[x] in caracteresEspaciales ) or (cadena[x] in numeros):
			print "	Error -*Los nobres no pueden tener caracteres especiales o números xD *-"
			return False
			pass
	return True	
	pass
def validarTelefono(cadena):
	cadena=str(cadena)
	for x in range(len(cadena)):
		if (cadena[x] in letras):
			print "	Error -*El telefono tiene letras xD *-"
			return False
			pass
	return True	
	pass


def ventana(cadena1,cadena2):
	cadena1=str(cadena1)
	cadena2=str(cadena2)
	eg.msgbox(msg="------------->"+cadena2, 
		title=cadena1, 
		ok_button='Continuar' #,image="imagen.jpg"
		)
	pass

def validarRegistarUsuario(nombre,aP,aM,user,pas,puesto):
	if validarLetras(nombre)!= True:
		ventana(" ----- ERROR DE DATOS -----","El nombre tiene letras  "+str(nombre)+ " es invalido")
		return True
		pass
	if validarLetras(aP)!= True:
		ventana(" ----- ERROR DE DATOS -----","El apellido tiene numeros "+str(aP)+ "es invalida")
		return True
		pass
	if validarLetras(aM)!= True:
		ventana(" ----- ERROR DE DATOS -----","El apellido tiene numeros  "+str(aM)+ "es invalida")
		return True
		pass
	if validarUser(user)!= True:
		ventana(" ----- ERROR DE DATOS -----","El usuario   "+str(user)+ "es invalida")
		return True
		pass
	if validarLetras(puesto)!= True:
		ventana(" ----- ERROR DE DATOS -----","EL puesto es incorrecto "+str(puesto)+ " es invalida")
		return True
		pass		
	if validarLetras(nombre) and validarLetras(aP) and validarLetras(aM) and validarUser(user) and  validarLetras(puesto):
		ventana("DATOS CORRECTOS","  Ningun error \n\t\tSe valido Correctamente el Usuario")
		return False
		pass

	pass





#Ejemplos de como se debe llamar las funciones *fecha entrada tiene que ser ingresada afuerzas con "" (str)
#registroSalida("5a15158",15,"31/12/00","00:59:58","11")
#correo='nombre@dominiao.eaxt'
#validarCorreo(correo)
#validarRegistarUsuario("gab","me","rdz","dw13d","67u","bjhgj")
#validarBolPer("Taurus 2014","25A-00","2014","S1AS5","Gabriel Mendoza",214153132)

def compararUsuarios(cadena):
	cadena1 = 'casa'
	cadena2 = 'casas'
	cadena3 = 'pasa'
	 
	if re.match(cadena1, cadena2):
	    print('cadena1 y cadena2 son coincidentes')
	else:
	    print('cadena1 y cadena2 no son coincidentes')
	  
	if re.match(cadena1, cadena3):
	    print('cadena1 y cadena3 son coincidentes')
	else:
	    print('cadena1 y cadena3 no son coincidentes')
	pass

def validarCorreo(clave):
	lista=str(clave)
	if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',lista.lower()):
		print "Correo correcto"
	else:
		print "Correo incorrecto"
	pass


################ Ventanas ###############
#eg.msgbox(msg='   	         ERROR, PARECE SER QUE ALGUN CAMPO ES INCORRECTO', title=' ** ERROR DE DATOS **', ok_button='Continuar')
