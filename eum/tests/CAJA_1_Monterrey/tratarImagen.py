# -*- coding: utf-8 -*-
"""
Estacionamientos unicos de México
Este archivo es para remplaar a acceso4.py
Funcion: 		Funcion de reducir tamaño de imagen
Descripcion:	
				Reduce la imagen que ingresa
Funciones que se pueden usar:
	1) cambTam()	


"""
import Image

def cambiarTamLog(imageFile):
	# open an image file (.bmp,.jpg,.png,.gif) you have in the working folder
	#imageFile = str(imagen)+".png"
	print imageFile
	
	im1 = Image.open(imageFile)
	# adjust width and height to your needs
	width = 200
	height = 100
	im5 = im1.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter
	ImagenSalida = "outLogo.jpg"
	im5.save(ImagenSalida)
	return ImagenSalida
	pass
def cambiarTamTODO(imageFile):
	# open an image file (.bmp,.jpg,.png,.gif) you have in the working folder
	#imageFile = str(imagen)+".png"
	print imageFile
	
	im1 = Image.open(imageFile)
	# adjust width and height to your needs
	width = 512
	height = 255
	im5 = im1.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter
	ImagenSalida = "outLogo.jpg"
	im5.save(ImagenSalida)
	return ImagenSalida
	pass	

def cambiarTamQR(imageFile):
	# open an image file (.bmp,.jpg,.png,.gif) you have in the working folder
	#imageFile = str(imagen)+".png"
	print imageFile
	im1 = Image.open(imageFile)
	# adjust width and height to your needs
	width = 200
	height = 200
	im5 = im1.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter
	ImagenSalida = "outQR.jpg"
	im5.save(ImagenSalida)
	return ImagenSalida
	pass

def cambiarTamTex(imageFile):
	print imageFile
	im1 = Image.open(imageFile)
	# adjust width and height to your needs
	width = 512 # ancho
	height = 255 # alto
	im5 = im1.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter
	ImagenSalida = "outT.png"
	im5.save(ImagenSalida)
	return ImagenSalida
	pass

#cambiarTam("logoPTIP")
