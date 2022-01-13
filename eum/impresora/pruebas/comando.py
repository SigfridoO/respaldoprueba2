import commands
resultado = commands.getoutput("ls /var")
print resultado

#colocar comando para imprimir archivo
#imprime= commands.getoutput("lp /home/pi/Desktop/pruebas/hola_mundo.pdf")
imprime= commands.getoutput("lp -d SANEI_SK_Series /home/pi/Documents/eum/impresora/pruebas/test.pdf")
