# -*- coding: utf-8 -*-
"""
Funciones de validacion de datos de formularios
1.- registroSalida : Los datos que se leen de la camara
"""
import re
import easygui as eg


letras="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letrasMIN="abcdefghijklmnopqrstuvwxyz"
numeros="0123456789"
caracteresEspaciales="ñ|@·~½¬{[]}},.+´/*"

def validarNumeros(cadena):
	cadena=str(cadena)
	"""
	for x in range(len(cadena)):
		if cadena[x] not in numeros:
			print "	Error -*Un argumento enetero tiene letras*-"
			return False
			pass
	"""
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

def validarFormatoFecha(cadena):
	cadena=str(cadena)
	"""
	fecha = re.compile(r'^([0][1-9]|[12][0-9]|3[01])/([0][1-9]|1[012])/(([0-9]\d))$')
	# validando dd/mm/aa
	if fecha.search(cadena) != None:
		return True
		pass
	else: 
		return False
	"""
	return True

def validarFecha(cadena):
	cadena=str(cadena)
	fecha = re.compile(r'^([0][1-9]|[12][0-9]|3[01])/([0][1-9]|1[012])/(([2][0][0-9]\d))$')
	# validando dd/mm/aaaa
	if fecha.search(cadena) != None:
		return True
		pass
	else: 
		return False
	pass

import time

def validateDateEs(date):
    """
    Funcion para validar una fecha en formato:
    dd/mm/yyyy
    """
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

#print validateDateEs("02/02/2017")




def validarFormatoHora(cadena):
	cadena=str(cadena) 
	"""
	if re.match('(([0-2][0-3])|([1][0-9])):([0-5][0-9]):([0-5][0-9])', cadena) :
		return True
	else:
		return False
	pass
	"""
	return True



def validarHora(cadena):
	cadena=str(cadena)
	"""
	Funcion para validar una fecha en formato:
	hh:mm:ss
	"""
	for format in ['%H:%M:%S']:
		try:
			result = time.strptime(cadena, format)
			if len(cadena)<8:
				print "Error Completa con el formato hh:mm:ss"
				return False
			else:
				return True
		except:
			pass
	return False

#print validarHora("03:50:00")

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

def ventadaTF(cadena):
	msg=str(cadena)
	respuesta = eg.boolbox(msg, title='Control: boolbox',   choices=('CANCELAR', ' CONTINUAR'))
	print respuesta
	pass

#ventadaTF("hola")

def registroSalida(noBol,terminalEntrada,fechaIn,horaIn,tarifa):
	noBol=str(noBol)
	terminalEntrada=str(terminalEntrada)
	fechaIn=str(fechaIn)
	horaIn=str(horaIn)
	tarifa=str(tarifa)
	if validarNumeros(noBol)!= True:
		ventana(" ----- ERROR DE DATOS -----","\t\tEl Boleto  "+str(noBol)+ " es invalido \n\t\t Porfavor ingreselo con números")
		return True
		pass
	if validarNumeros(terminalEntrada)!= True:
		ventana(" ----- ERROR DE DATOS -----","\t\tLa terminal de entrada no corresponde >> "+str(terminalEntrada)+ "  es invalida")
		return True
		pass
	if validarFormatoFecha(fechaIn)!= True:
		ventana(" ----- ERROR DE DATOS -----","\t\tEl  formato de la fecha es incorrecta >> "+str(fechaIn)+ " \n\t\t utiliza formato dd/mm/aa \n\t\t no te olvides de rellenar con ceros \n\t\t Ejemplo: 07/12/17")
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
	if validarNumeros(noBol) and validarNumeros(terminalEntrada) and validarFormatoFecha(fechaIn) and validarFormatoHora(horaIn) and validarTarifa(tarifa):
		ventana("DATOS CORRECTOS"," Ningun error \n\t\t\t\t SE REGISTRO EL BOLETO EXITOSAMENTE")
		return False
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



def validarBolPer(marca,placas,modelo,licencia,nombre,telefono):
	placas=str(placas)
	modelo=str(modelo)
	licencia=str(licencia)
	nombre=str(nombre)
	telefono=str(telefono)
	if validarMarca(marca)!= True:
		ventana(" ----- ERROR DE DATOS -----","La marca del carro "+str(marca)+ " es invalida")
		return True
		pass	
	if validarPlacas(placas)!= True:
		ventana(" ----- ERROR DE DATOS -----","Las placas del carro "+str(placas)+ " son invalidas escriba en Mayúsculas")
		return True
		pass
	if validarNumeros(modelo)!= True:
		ventana(" ----- ERROR DE DATOS -----","El modelo del carro "+str(modelo)+ " es invalido")
		return True
		pass
	if validarPlacas(licencia)!= True:
		ventana(" ----- ERROR DE DATOS -----","La licencia del carro "+str(licencia)+ " es invalida  escriba en Mayúsculas")
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
	
	if  validarMarca(marca) and validarPlacas(placas) and validarNumeros(modelo) and validarPlacas(licencia) and validarNombre(nombre) and validarTelefono(telefono):
		ventana("DATOS CORRECTOS","  Ningun error \n\t\tSe valido Correctamente el Boleto perdido")
		return False
		pass
	
	pass

def validarCorreo(clave):
	lista=str(clave)
	if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',lista.lower()):
		print "Correo correcto"
	else:
		print "Correo incorrecto"
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



################ Ventanas ###############
#eg.msgbox(msg='   	         ERROR, PARECE SER QUE ALGUN CAMPO ES INCORRECTO', title=' ** ERROR DE DATOS **', ok_button='Continuar')
