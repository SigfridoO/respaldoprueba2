#!/usr/bin/python3
import os
from time import sleep
def pedirNumeroEntero(label):
 
	correcto=False
	num=0
	while(not correcto):
		try:
			num = int(input(label))
			correcto=True
		except ValueError:
			print('Opcion invalida')
	 
	return num
 
salir = False
opcion = 0
 
def menu():

	os.system('clear') # NOTA para windows tienes que cambiar clear por cls

	print ("\t\t----- Menu de configuracion Sistemas EUM------\n")

	print ("\t1 - Numero de Sucursal")

	print ("\t2 - Tipo de sistema")
	
	print ("\t3 - Ver Parametros")

	print ("\t4 - Salir")
	
def tecla():	
	input("Enter para continuar...")
 
 
def sustituye(archivo,buscar,reemplazar):
		"""

		Esta simple función cambia una linea entera de un archivo

		Tiene que recibir el nombre del archivo, la cadena de la linea entera a

		buscar, y la cadena a reemplazar si la linea coincide con buscar

		"""
		with open(archivo, "r") as f:

			# obtenemos las lineas del archivo en una lista

			lines = (line.rstrip() for line in f)
			print(lines)

	 

			# busca en cada linea si existe la cadena a buscar, y si la encuentra

			# la reemplaza

			

			altered_lines = [reemplazar if line==buscar else line for line in lines]
			f= open(archivo, "w+")
			print(altered_lines[0],len(altered_lines))
			for i in range(len(altered_lines)):
				if(buscar in altered_lines[i]):
					print (altered_lines[i])
					cambia=altered_lines[i]
					f.write(reemplazar+"\n")
				else:
					f.write(altered_lines[i]+"\n")
			f.close()


while not salir:

	menu()
	opcion = pedirNumeroEntero("\nIngresa una opcion: ")
 
	if opcion == 1:
		num = pedirNumeroEntero("Ingresa el No. de Sucursal:")
		print ("Sucursal: ",num)
		escribeArch = open("/home/pi/Documents/eum/sys/sucursal.txt","w")
		escribeArch.write(str(num))
		escribeArch.close()	
		tecla()
	elif opcion == 2:
		os.system('clear')
		print ("\t1 - Boletera")
		print ("\t2 - Cajero")
		print ("\t3 - Validador")
		print ("\t4 - Publicidad")
		num = pedirNumeroEntero("Ingresa el No. de Sistema ")
		print ("Sistema: ",num)
		if(num == 1):
			sustituye("/home/pi/.config/lxsession/LXDE-pi/autostart","python3","@lxterminal")
			sustituye("/home/pi/.bashrc","","sudo python3 /home/pi/Documents/eum/app/expedidora/first.py")
		elif(num == 2):
			
			sustituye("/home/pi/.config/lxsession/LXDE-pi/autostart","python3","@/usr/bin/python3 /home/pi/Documents/eum/app/cajeroF/cajero/cajeroRed.py")
			sustituye("/home/pi/.config/lxsession/LXDE-pi/autostart","lxterminal","@/usr/bin/python3 /home/pi/Documents/eum/app/cajeroF/cajero/cajeroRed.py")
			sustituye("/home/pi/.bashrc","python3","")
		elif(num == 3):
			
			sustituye("/home/pi/.config/lxsession/LXDE-pi/autostart","python3","@/usr/bin/python3 /home/pi/Documents/eum/app/salida/salida.py")
			sustituye("/home/pi/.config/lxsession/LXDE-pi/autostart","lxterminal","@/usr/bin/python3 /home/pi/Documents/eum/app/salida/salida.py")
			sustituye("/home/pi/.bashrc","python3","")
		elif(num == 4):
			
			sustituye("/home/pi/.config/lxsession/LXDE-pi/autostart","python3","@/usr/bin/python3 /home/pi/Documents/eum/app/cajeroF/publicidad/publicidad.py")
			sustituye("/home/pi/.config/lxsession/LXDE-pi/autostart","lxterminal","@/usr/bin/python3 /home/pi/Documents/eum/app/cajeroF/publicidad/publicidad.py")
			sustituye("/home/pi/.bashrc","python3","")
			num = pedirNumeroEntero("Ingresa un numero de Rotacion (0 al 3) ")
			sustituye("/boot/config.txt","display","display_rotate="+str(num)+"")
			print ("Rotate: ",num)
			tecla()
		else:
			print ("Opcion Invalida: ")
		tecla()

	elif opcion == 3:
		tecla()
	elif opcion == 4:
		salir = True
	else:
		print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
