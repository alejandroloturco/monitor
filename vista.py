import tkinter as tk
from tkinter import messagebox

class PacienteView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Gestión de Pacientes")
        self.root.geometry("400x300")
        
        self.frame_login = tk.Frame(self.root)
        self.frame_login.pack()

        self.label_usuario = tk.Label(self.frame_login, text="Usuario:")
        self.label_usuario.pack()
        self.entry_usuario = tk.Entry(self.frame_login)
        self.entry_usuario.pack()

        self.label_password = tk.Label(self.frame_login, text="Contraseña:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self.frame_login, show="*")
        self.entry_password.pack()

        self.button_login = tk.Button(self.frame_login, text="Login", command=self.controller.login)
        self.button_login.pack()

        self.frame_main = tk.Frame(self.root)
        self.label_nombre = tk.Label(self.frame_main, text="Nombre:")
        self.entry_nombre = tk.Entry(self.frame_main)
        self.label_apellido = tk.Label(self.frame_main, text="Apellido:")
        self.entry_apellido = tk.Entry(self.frame_main)
        self.label_edad = tk.Label(self.frame_main, text="Edad:")
        self.entry_edad = tk.Entry(self.frame_main)
        self.label_identificacion = tk.Label(self.frame_main, text="Identificación:")
        self.entry_identificacion = tk.Entry(self.frame_main)
        self.button_agregar = tk.Button(self.frame_main, text="Agregar Paciente", command=self.controller.agregar_paciente)
        
        self.label_nombre.pack()
        self.entry_nombre.pack()
        self.label_apellido.pack()
        self.entry_apellido.pack()
        self.label_edad.pack()
        self.entry_edad.pack()
        self.label_identificacion.pack()
        self.entry_identificacion.pack()
        self.button_agregar.pack()

        self.label_busqueda = tk.Label(self.frame_main, text="Buscar Paciente por Nombre:")
        self.entry_busqueda = tk.Entry(self.frame_main)
        self.button_buscar = tk.Button(self.frame_main, text="Buscar", command=self.controller.buscar_pacientes)
        
        self.label_busqueda.pack()
        self.entry_busqueda.pack()
        self.button_buscar.pack()

        self.lista_pacientes = tk.Listbox(self.frame_main)
        self.lista_pacientes.pack()
        self.button_eliminar = tk.Button(self.frame_main, text="Eliminar Paciente", command=self.controller.eliminar_paciente)
        self.button_eliminar.pack()
        
    def mostrar_login(self):
        self.frame_login.pack()
        self.frame_main.pack_forget()

    def mostrar_main(self):
        self.frame_login.pack_forget()
        self.frame_main.pack()

    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)
