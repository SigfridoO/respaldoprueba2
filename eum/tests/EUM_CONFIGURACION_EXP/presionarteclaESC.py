import sys
from PyQt4 import QtGui, QtCore
#Vista
from dLogin import dLogin
from dAccess import dAccess

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.Form = QtGui.QWidget()
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Event handler')
        #Funcionalidades
        self.login = QtGui.QDialog(self.Form)
        self.l = dLogin(self.login)
        self.l.pushButton.clicked.connect(self.vLogin)
        self.l.pushButton2.clicked.connect(self.secretAccess)
        self.login.show()
        #Final
        self.daccess= QtGui.QDialog(self.Form)
        self.access1 = dAccess(self.daccess)
        self.access1.pushButton.clicked.connect(self.vAccess)
        self.access1.pushButton2.clicked.connect(self.Logout)
        self.show()

    def vLogin(self):
        f = -1
        user = self.l.lineEdit.text()
        password = self.l.lineEdit_2.text()
        f=1
        print(f)
        self.login.setHidden(True)
        self.Form.show()
        return f
    pass

    def Logout(self):
        self.groupBox.setEnabled(False)
        self.Form.setHidden(True)
        self.daccess.setHidden(True)
        self.clearScreen()
        self.l.lineEdit.setText("")
        self.l.lineEdit_2.setText("")
        self.l.elabel.setText("")
        self.login.setHidden(False)
    pass

    
    def vAccess(self):
        if(self.access1.lineEdit.text()==SUPER_PASSWORD):
            print("acceso concedido")
            exit()
    pass

    def secretAccess(self):
        print("Hola")
        self.login.setHidden(True)
        self.daccess.show()
    pass

    def keyPressEvent(self, event):
        #Did the user press the Escape key?
        if event.key() == QtCore.Qt.Key_Escape: #QtCore.Qt.Key_Escape is a value that equates to what the operating system passes to python from the keyboard when the escape key is pressed.
            #Yes: Close the window
            self.show()
            print "ESC"
        #No:  Do nothing.

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()