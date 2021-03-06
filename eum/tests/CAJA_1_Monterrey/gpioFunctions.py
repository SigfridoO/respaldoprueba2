import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.IN) #APAGAR



def abrirBarrera(self):
	GPIO.setup(13, GPIO.OUT) #Configura el GPIO como salida 
	GPIO.output(13, True) # Transforma el GPIO en un bajo logico
	time.sleep(0.5)
	GPIO.output(13, False) # Turns the GPIO logical Low

def cerrarBarrera(self): 
	GPIO.setup(6, GPIO.OUT) #Set GPIO Pin as Output 
	GPIO.output(6, True) # Turns the GPIO logical Low
	time.sleep(0.5)
	GPIO.output(6, False) # Turns the GPIO logical Low

def gpiocleanup(self):
	GPIO.cleanup() # GPIO cleanup upon Close Button Press


