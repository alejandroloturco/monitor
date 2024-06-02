from modelo import *
from vista2 import *

class New_controlador:
    def __init__(self):
        self.modelo = Usuario()
        self.aplicacion = QApplication([])

    def inicio(self):
        self.ventana1()

    def ventana1(self):
        self.log_in = QTprincipal(self)
        self.log_in.show()
        self.aplicacion.exec_()
    
    def validacion(self,usuario,contraseña):
        if self.modelo.validacion(usuario,contraseña) == True:
            return True

    def ventana2(self):
        self.principal = QTsegundo(self)
        self.principal.show()
