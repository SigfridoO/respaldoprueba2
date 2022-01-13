# -*- coding: utf-8 -*-
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os


from PyQt4 import QtGui, QtCore
#Vista
from accesoTerminal import dAccesoConfigurarTerminal
from configurarTer import dConfigurarTerminal
from cortesExp import dcorteCaja
from configurarFechaHora import dConfigurarFechaHora

import validacionesExp as validaciones
import escribirArchivos as esc
import cortesExpFun as conectionBD


SUPER_PASSWORD_CONFIGURAR   ="1"
SUPER_PASSWORD_CORTE        ="2"
SUPER_PASSWORD_FECHAHORA    ="3"
SUPER_PASSWORD_APAGAR		="4"


class Vista(QtGui.QWidget):
    def __init__(self):
        super(Vista, self).__init__()
        self.Form = QtGui.QWidget()
        self.initUI()

    def initUI(self):
        #Funcionalidades
        self.accesoT = QtGui.QDialog(self.Form)
        self.aT = dAccesoConfigurarTerminal(self.accesoT)
        self.aT.pushButton_Acceder.clicked.connect(self.secretAccess)
        self.accesoT.show()
        #Lo siguiente tenemnos preparadas las siguientes interfaces
        #Interfaz de configuracion
        self.configT = QtGui.QDialog(self.Form)
        self.conT = dConfigurarTerminal(self.configT)
        #Interfaz de cortes
        self.corteT = QtGui.QDialog(self.Form)
        self.corT = dcorteCaja(self.corteT)
        #Interfaz de Fecha y Hora
        self.configFH = QtGui.QDialog(self.Form)
        self.conFH = dConfigurarFechaHora(self.configFH)

    def vAccess(self):
        if(self.access1.lineEdit.text()==SUPER_PASSWORD):
            print("acceso concedido")
            exit()
    pass

    def secretAccess(self):
        print("Entrada a acceso Secreto")
        palabraMagica=self.aT.palabraMagica.text() #palabra que se escribio
        indexCombo=self.aT.comboBox.currentIndex() #index del combox
        #palabraMagica="2"
        #indexCombo=1
        if palabraMagica==SUPER_PASSWORD_CONFIGURAR and indexCombo==0 :
            self.accesoT.setHidden(True)    #Hacemos la ventana de acceso invisible
            print "Configuracion" #Combox de configuracion
            self.configT.show()
            self.conT.pushButton_Cancelar.clicked.connect(self.botonCancelarConfiguracion) #Vamos al boton de cancelar y nos devuelve a la pagina acceso
            self.conT.pushButton_Aceptar.clicked.connect(self.logicaConfiguracion)

        elif palabraMagica==SUPER_PASSWORD_CORTE and indexCombo==1:
            self.accesoT.setHidden(True)    #Hacemos la ventana de acceso invisible
            print "Cortes"        #Combox de Corte
            self.corteT.show()
            self.corT.pushButton_Cancelar.clicked.connect(self.botonCancelarCorte)
            self.corT.pushButton.clicked.connect(self.logicaCorte)
        elif palabraMagica==SUPER_PASSWORD_FECHAHORA and indexCombo==2:
            self.accesoT.setHidden(True)    #Hacemos la ventana de acceso invisible
            self.configFH.show()
            fechaActual=time.strftime("%d/%m/%Y")
            self.conFH.dateEditFecha.setText(fechaActual)
            self.conFH.pushButton_Aceptar.clicked.connect(self.logicaConfiguracionFechaHora)
            self.conFH.pushButton_Cancelar.clicked.connect(self.botonCancelarConfiguracionFechaHora)
        elif palabraMagica==SUPER_PASSWORD_APAGAR and indexCombo==3:
            self.accesoT.setHidden(True)    #Hacemos la ventana de acceso invisible
            reiniciarSistema(self)
        else:
            print "Mensaje de Error de contraseña"
            self.aT.palabraMagica.setText("") #Limpiamos 
    pass

    def botonCancelarConfiguracion(self):
        self.accesoT.show()
        self.aT.palabraMagica.setText("") #Limpiamos
        self.configT.setHidden(True)
        pass

    def botonCancelarCorte(self):
        self.accesoT.show()
        self.aT.palabraMagica.setText("") #Limpiamos
        self.corteT.setHidden(True)
        pass        

    def botonCancelarConfiguracionFechaHora(self):
        self.accesoT.show()
        self.aT.palabraMagica.setText("") #Limpiamos
        self.configFH.setHidden(True)
        
        pass

    def logicaConfiguracion(self):
        nombrePlaza=str(self.conT.txtNombrePlaza.text())
        localidad_Estado=str(self.conT.txtLocalidadEstado.text())
        localidad_Muni=str(self.conT.txtLocalidadMunicipio.text())
        numeroTerminal=str(self.conT.spinBox.value())
        if len(nombrePlaza)==0 or len(localidad_Estado)==0  or len(localidad_Muni)==0    :
            #Falta algún argumento
            validaciones.ventana(" -------------- ERROR ---------------","\t\tPorfavor ingrese Datos \n\t\t Todos los datos son \n\t\t ** Obligatorios **")
        else:
            #print "Nombre de la plaza: "+ nombrePlaza 
            #print "Nombre de la localidad: "+ localidad_Estado
            #print "Nombre de la estado: "+ localidad_Muni
            #print "Numero de terminal: "+ numeroTerminal
            conectionBD.agregarCentroComercial(nombrePlaza,localidad_Estado,localidad_Muni,numeroTerminal)
            esc.escribirArchivoDatosDeTerminal(nombrePlaza,localidad_Estado,localidad_Muni,numeroTerminal)
            
            limpiarCamposConfigTer(self)

    def logicaCorte(self):
        fechaActual=time.strftime("%Y-%m-%d")   #OBETENEMOS LA FECHA ACTUAL
        #Se eligue el tipo de corte
        tipoDeCorte=self.corT.comboBox.currentIndex()
        if tipoDeCorte==0:
            print "Corte 1"
            fechaCorte1=self.corT.dateEdit.date()   #OBETENEMOS LA FECHA 
            fechaCorte1=fechaCorte1.toPyDate()      #OCUPAMOS ESTA FUNCION PARA PONER EL FORMATO CORRECTO  DD/MM/aaaa 
            fechaCorte1=str(fechaCorte1)
            
            #Verificamos que la fecha no sea mayor que la actual
            if fechaCorte1>fechaActual:
                print "ERROR FECHA MAYOR A HOY"
                pass
            else:
                print fechaCorte1
                conectionBD.elijeCorte1PorDia(fechaCorte1)
                pass
            pass
        if tipoDeCorte==1:
            print "Corte 2"
            fechaCorte1=self.corT.dateEdit.date()   #OBETENEMOS LA FECHA 
            fechaCorte1=fechaCorte1.toPyDate()      #OCUPAMOS ESTA FUNCION PARA PONER EL FORMATO CORRECTO  DD/MM/aaaa 
            fechaCorte2=self.corT.dateEdit_2.date()   #OBETENEMOS LA FECHA 
            fechaCorte2=fechaCorte2.toPyDate()      #OCUPAMOS ESTA FUNCION PARA PONER EL FORMATO CORRECTO  DD/MM/aaaa 
            fechaCorte1=str(fechaCorte1)
            fechaCorte2=str(fechaCorte2)
            
            #Verificamos que la fecha no sea mayor que la actual
            if fechaCorte1>fechaActual or fechaCorte2>fechaActual:
                print "ERROR FECHA MAYOR A HOY"
                pass
            else:
                print fechaCorte1
                print fechaCorte2
                conectionBD.elijeCorte2EntreFecha(fechaCorte1,fechaCorte2)
                pass

            pass

        pass


    def logicaConfiguracionFechaHora(self):
        fechaEditada=self.conFH.dateEditFecha.text()
        horaEditada=self.conFH.timeEditHora.text()
        fechaEditada=str(fechaEditada)
        horaEditada=str(horaEditada)
        #print "La fecha es "+fechaEditada        print "La hora será "+horaEditada
        #FALTA VALIDAR QUE SEAN EN EL FORMATO CORRECTO
        #Validar Fecha y Hora
        if len(horaEditada)==0: #VALIDAR QUE NO SEAN VACIOS
            validaciones.ventana(" -------------- ERROR ---------------","\t\tPorfavor ingrese Datos  con formato:\n\t\t Fecha: dd/mm/aaaa \n\t\t Hora: hh:mm:ss")
            pass
        else:
            # validando dd/mm/aaaa
            if validaciones.validateDateEs(fechaEditada)== False: #Devuelve true si es correcto false si hay error
                validaciones.ventana(" -------------- ERROR EN FORMATO DE FECHA ---------------","\t\tLa fecha  "+fechaEditada+ " es invalida \n\t\t Porfavor ingreselo con formato :\n dd/mm/aaaa")
            else:
                #SE PREGUNTA POR LA HORA
                if validaciones.validarHora(horaEditada)==False: # Devuelve true si es correcto y false si hay error
                    validaciones.ventana(" -------------- ERROR EN FORMATO DE HORA ---------------","\t\tLa hora  "+horaEditada+ " es invalida \n\t\t Porfavor ingreselo con formato :\n\t\t hh/mm/ss por ejemplo: 08:20:00")
                else:
                    ##Se llena el archivo donde se tomaran la hora y Fecha
                    respuestaUsu=validaciones.ventadaTF("Los cambios se realizaran una vez que se reinicie el Sistema\n Quieres reiniciar ahora?")
                    esc.escibirArchivoFechaHora(fechaEditada,horaEditada)   
                    if respuestaUsu==False: #logica inversa por la ventana
                        reiniciarSistema(self) 
                        limpiarCamposFechaHora(self)
                    

        pass

def limpiarCamposConfigTer(self):
    self.conT.txtNombrePlaza.setText("")
    self.conT.txtLocalidadEstado.setText("")
    self.conT.txtLocalidadMunicipio.setText("")
    pass

def limpiarCamposFechaHora(self):
    self.conFH.dateEditFecha.setText("")
    self.conFH.timeEditHora.setText("")
    pass

def reiniciarSistema(self):
	os.system("sudo shutdown 0")


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Vista()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
