import json
import os

class PacienteModel:
    def __init__(self, filepath):
        self.filepath = filepath
        self.pacientes = self.cargar_datos()

    def cargar_datos(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                return json.load(file)
        return []

    def guardar_datos(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.pacientes, file)

    def agregar_paciente(self, nombre, apellido, edad, identificacion):
        if any(p['identificacion'] == identificacion for p in self.pacientes):
            raise ValueError("La identificación ya existe")
        nuevo_paciente = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "identificacion": identificacion
        }
        self.pacientes.append(nuevo_paciente)
        self.guardar_datos()

    def eliminar_paciente(self, identificacion):
        self.pacientes = [p for p in self.pacientes if p['identificacion'] != identificacion]
        self.guardar_datos()

    def buscar_pacientes(self, query):
        query = query.lower()
        return [p for p in self.pacientes if p['nombre'].lower().startswith(query)]
