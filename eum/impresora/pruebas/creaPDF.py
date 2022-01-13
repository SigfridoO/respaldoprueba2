from reportlab.pdfgen import canvas
 
c = canvas.Canvas("hola_mundo.pdf")
c.drawString(100,750,"Hola mundo pdf!")
c.drawImage("logoPTIP.jpg", 0, 0, width=400, height=400)

#drawImage(archivo, x, y, width=None, height=None)
#c.drawImage("Tux2.png", 0, A4[1]/2, width=400, height=400)
c.drawImage("output.png", 100, 150, width=400, height=400)
c.save()



