# -*- coding: utf-8 -*-

import math

import escribirTipoBoleto as boleto
import os

COSTO_POR_HORA_EXTRA=10
COSTO_POR_HORA_EXTRA_CON_SELLO=5
COSTO_POR_HORA_EXTRA_SIN_SELLO=10
HORAS_DE_COOPERACION_VOLUNTARIA=120 #MINUTOS
COSTO_BOLETO_PERDIDO=100
TIEMPO_TOLERANCIA_TAXI=5
PATH_INTERFAZ_TIPO_BOLETO="/home/pi/Documents/CAJA_1_Monterrey/tipoBoleto.py"



def preguntarPorVoluntario():
	#LLAMO A A¿LA INTERFAZ
	os.system("python " + PATH_INTERFAZ_TIPO_BOLETO)
	return boleto.getDato()

def preguntarCantidadVoluntario():
	#LLAMO A A¿LA INTERFAZ
	os.system("python /home/pi/Documents/CAJA_1_Monterrey/cobroVoluntario.py")
	return boleto.getVoluntario()

def calcularMonto(purosMinutos,tar,entrada):
	total = 0
	tarifa = int(tar)
	tiempo = int(purosMinutos)
	horaEntrada = int(entrada)
	print tiempo 
	#tarifa1  reglas: 2 primeras horas cooperacion voluntaria, restante 10 cada hora o fraccion adicional
	if tarifa == 1:
		#Tarifas dentro del horario de city Club SIN coperacion voluntaria
		if tiempo > HORAS_DE_COOPERACION_VOLUNTARIA and horaEntrada < 23 and horaEntrada >= 7:
			tarifaSELLO = preguntarPorVoluntario()#Preguntamos por el sello
			if tarifaSELLO == 'conSuburbia':
				tiempoResiduo = tiempo - HORAS_DE_COOPERACION_VOLUNTARIA
				horasPasadas = float(float(tiempoResiduo)/60.0)
				horasPasadas = math.ceil(horasPasadas) #subimos al entero proximo
				total = (horasPasadas) * COSTO_POR_HORA_EXTRA
				return float(total),5
			else:
				horasPasadas = float(float(tiempo)/60.0)
				horasPasadas = math.ceil(horasPasadas) #subimos al entero proximo
				total = (horasPasadas)*COSTO_POR_HORA_EXTRA
				return float(total),1
		#Tarifas dentro del horario de city Club CON coperacion voluntaria
		elif tiempo < HORAS_DE_COOPERACION_VOLUNTARIA and horaEntrada < 23 and horaEntrada >= 7:
			total = preguntarCantidadVoluntario()#Preguntamos por el sello
			return float(total),1
		#Turno nocturno
		else:
			horasPasadas = float(float(tiempo)/60.0)
			horasPasadas = math.ceil(horasPasadas)
			horaSalida = horaEntrada + horasPasadas
			if horaSalida >= 24:
				horaSalida = horaSalida - 24
			print horaSalida
			if horaSalida < 7:
				total = 50
				return float(total),1
			else:
				total = 50 + (horaSalida-7)*COSTO_POR_HORA_EXTRA
				return float(total),1
	#tarifa2 reglas: Locatario 0 Pesos
	if tarifa==2:
		total=0
		print(total)
		return float(total),2
	#tarifa3 reglas:Boleto perdido 
	if tarifa==3:
		total = COSTO_BOLETO_PERDIDO
		print(total)
		return float(total),3



