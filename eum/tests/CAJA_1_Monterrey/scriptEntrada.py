#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import easygui as eg
import os
import  first as ventana

def elegirVideo():
	mes=opciones()
	respuesta = eg.buttonbox(msg=str(mes),title='Control: buttonbox',choices=(mes))
	print respuesta
	reproducir(respuesta)
def reproducir(archivo):
	os.system("omxplayer --loop --win \"500 0 1400 800\" /home/pi/Videos/admi/"+archivo+"")
def opciones():
	path ="/home/pi/Videos/admi"
	dirs = os.listdir( path )
	return dirs
	
def main():
	
	os.system(" lxterminal -e sudo python /home/pi/Desktop/Ticket/first.py   ")
	archivo= "1.mp4"
	os.system("omxplayer   --win \"500 0 1400 800\" /home/pi/Videos/admi/"+archivo+"")

#main()
