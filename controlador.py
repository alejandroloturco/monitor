class PacienteController:
    def __init__(self, root):
        self.model = PacienteModel("pacientes.json")
        self.view = PacienteView(root, self)
        self.usuario = "admin123"
        self.password = "contrasena123"
        self.view.mostrar_login()

    def login(self):
        usuario = self.view.entry_usuario.get()
        password = self.view.entry_password.get()
        if usuario == self.usuario and password == self.password:
            self.view.mostrar_main()
        else:
            self.view.mostrar_mensaje("Error", "Usuario o contraseña incorrectos")

    def agregar_paciente(self):
        nombre = self.view.entry_nombre.get()
        apellido = self.view.entry_apellido.get()
        edad = self.view.entry_edad.get()
        identificacion = self.view.entry_identificacion.get()
        try:
            self.model.agregar_paciente(nombre, apellido, edad, identificacion)
            self.view.mostrar_mensaje("Éxito", "Paciente agregado exitosamente")
        except ValueError as e:
            self.view.mostrar_mensaje("Error", str(e))

    def buscar_pacientes(self):
        query = self.view.entry_busqueda.get()
        resultados = self.model.buscar_pacientes(query)
        self.view.lista_pacientes.delete(0, tk.END)
        for paciente in resultados:
            self.view.lista_pacientes.insert(tk.END, f"{paciente['nombre']} {paciente['apellido']} ({paciente['identificacion']})")

    def eliminar_paciente(self):
        seleccion = self.view.lista_pacientes.curselection()
        if seleccion:
            paciente_str = self.view.lista_pacientes.get(seleccion[0])
            identificacion = paciente_str.split("(")[-1].strip(")")
            self.model.eliminar_paciente(identificacion)
            self.view.mostrar_mensaje("Éxito", "Paciente eliminado exitosamente")
            self.buscar_pacientes()
        else:
            self.view.mostrar_mensaje("Error", "Seleccione un paciente para eliminar")

if __name__ == "__main__":
    root = tk.Tk()
    controller = PacienteController(root)
    root.mainloop()
