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
        self.principal = MainWindow2(self)
        self.principal.show()

    def ventana3(self):
        self.tercera = MainWindow3(self)
        self.tercera.show()
    
    def agregar(self,nombre,apellido,edad,id):
        self.modelo.agregar(nombre,apellido,edad,id)

    def ventana4(self):
        self.tercera = MainWindow4(self)
        self.tercera.show()
    
    def buscar(self,pal):
        return self.modelo.buscar(pal)
    
    def eliminar(self,cedula):
        self.modelo.eliminar(cedula)
        



