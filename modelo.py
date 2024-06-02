import json
import os


class Usuario:
    def __init__(self):
        self._ruta = os.path.join(os.getcwd(),'paciente.json')
    
    def getRuta(self):
        return self._ruta

    def validacion(self,usuario,contraseña):
        if usuario == 'admin123' and contraseña == 'contrasena123':
            return True
        else:
            return False
        
    def cargar_pacientes(self):        
        with open(self._ruta, 'r') as file:
            self._pacientes = json.load(file)
            return self._pacientes
        
    def validar_paciente(self,id,nombre,apellido):
        x = self.cargar_pacientes()
        if str(id) in x:
            #print("Documento ya registrado")
            return True
        ids = list(self._pacientes.keys())
        for i in ids:
            if nombre in x[i][0] and apellido in x[i][1]:
                #print("Nombre y apellido ya registrado")
                return True
    
    def agregar(self,id,nombre,apellido,edad):
        if self.validar_paciente(id,nombre,apellido):
            print("Paciente ya registrado")
        else:
            x = self.cargar_pacientes()
            x[str(id)]=[nombre,apellido,edad]
            with open(self._ruta, 'w') as file:
                json.dump(x, file)

    def buscar(self,palabra):
        nuevos = []
        x=self.cargar_pacientes()
        ids = list(self._pacientes.keys())
        for i in ids:
            if x[i][0].upper().startswith(palabra.upper()):
                x[i].append(i)
                nuevos.append(x[i])
        return nuevos
    
    def eliminar(self, id):
        x = self.cargar_pacientes()
        for i in x:
            if i == id:
                del x[id]
                with open(self._ruta, 'w') as file:
                    json.dump(x, file)
                    break


                

        

        
