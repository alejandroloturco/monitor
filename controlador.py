class PacienteController:
    def __init__(self, app):
        self.model = PacienteModel("pacientes.json")
        self.view = PacienteView(self)
        self.usuario = "admin123"
        self.password = "contrasena123"
        self.view.show()

    def login(self):
        usuario = self.view.entry_usuario.text()
        password = self.view.entry_password.text()
        if usuario == self.usuario and password == self.password:
            self.view.mostrar_main()
        else:
            self.view.mostrar_mensaje("Error", "Usuario o contraseña incorrectos")

    def agregar_paciente(self):
        nombre = self.view.entry_nombre.text()
        apellido = self.view.entry_apellido.text()
        edad = self.view.entry_edad.text()
        identificacion = self.view.entry_identificacion.text()
        try:
            self.model.agregar_paciente(nombre, apellido, edad, identificacion)
            self.view.mostrar_mensaje("Éxito", "Paciente agregado exitosamente")
        except ValueError as e:
            self.view.mostrar_mensaje("Error", str(e))

    def buscar_pacientes(self):
        query = self.view.entry_busqueda.text()
        resultados = self.model.buscar_pacientes(query)
        self.view.lista_pacientes.clear()
        for paciente in resultados:
            self.view.lista_pacientes.addItem(f"{paciente['nombre']} {paciente['apellido']} ({paciente['identificacion']})")

    def eliminar_paciente(self):
        seleccion = self.view.lista_pacientes.currentItem()
        if seleccion:
            paciente_str = seleccion.text()
            identificacion = paciente_str.split("(")[-1].strip(")")
            self.model.eliminar_paciente(identificacion)
            self.view.mostrar_mensaje("Éxito", "Paciente eliminado exitosamente")
            self.buscar_pacientes()
        else:
            self.view.mostrar_mensaje("Error", "Seleccione un paciente para eliminar")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    controller = PacienteController(app)
    sys.exit(app.exec_())
