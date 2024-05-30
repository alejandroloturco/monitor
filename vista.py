from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QListWidget, QMessageBox
)

class PacienteView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Gestión de Pacientes")
        self.setGeometry(100, 100, 600, 400)
        
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        
        self.layout = QVBoxLayout()
        
        # Log-in elements
        self.login_layout = QVBoxLayout()
        self.label_usuario = QLabel("Usuario:")
        self.entry_usuario = QLineEdit()
        self.label_password = QLabel("Contraseña:")
        self.entry_password = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.Password)
        self.button_login = QPushButton("Login")
        self.button_login.clicked.connect(self.controller.login)
        
        self.login_layout.addWidget(self.label_usuario)
        self.login_layout.addWidget(self.entry_usuario)
        self.login_layout.addWidget(self.label_password)
        self.login_layout.addWidget(self.entry_password)
        self.login_layout.addWidget(self.button_login)
        
        # Main elements
        self.main_layout = QVBoxLayout()
        self.label_nombre = QLabel("Nombre:")
        self.entry_nombre = QLineEdit()
        self.label_apellido = QLabel("Apellido:")
        self.entry_apellido = QLineEdit()
        self.label_edad = QLabel("Edad:")
        self.entry_edad = QLineEdit()
        self.label_identificacion = QLabel("Identificación:")
        self.entry_identificacion = QLineEdit()
        self.button_agregar = QPushButton("Agregar Paciente")
        self.button_agregar.clicked.connect(self.controller.agregar_paciente)
        
        self.main_layout.addWidget(self.label_nombre)
        self.main_layout.addWidget(self.entry_nombre)
        self.main_layout.addWidget(self.label_apellido)
        self.main_layout.addWidget(self.entry_apellido)
        self.main_layout.addWidget(self.label_edad)
        self.main_layout.addWidget(self.entry_edad)
        self.main_layout.addWidget(self.label_identificacion)
        self.main_layout.addWidget(self.entry_identificacion)
        self.main_layout.addWidget(self.button_agregar)
        
        self.label_busqueda = QLabel("Buscar Paciente por Nombre:")
        self.entry_busqueda = QLineEdit()
        self.button_buscar = QPushButton("Buscar")
        self.button_buscar.clicked.connect(self.controller.buscar_pacientes)
        
        self.main_layout.addWidget(self.label_busqueda)
        self.main_layout.addWidget(self.entry_busqueda)
        self.main_layout.addWidget(self.button_buscar)
        
        self.lista_pacientes = QListWidget()
        self.button_eliminar = QPushButton("Eliminar Paciente")
        self.button_eliminar.clicked.connect(self.controller.eliminar_paciente)
        
        self.main_layout.addWidget(self.lista_pacientes)
        self.main_layout.addWidget(self.button_eliminar)
        
        self.layout.addLayout(self.login_layout)
        self.layout.addLayout(self.main_layout)
        
        self.widget.setLayout(self.layout)
        self.mostrar_login()
    
    def mostrar_login(self):
        self.login_layout.setEnabled(True)
        self.main_layout.setEnabled(False)
        
    def mostrar_main(self):
        self.login_layout.setEnabled(False)
        self.main_layout.setEnabled(True)
    
    def mostrar_mensaje(self, titulo, mensaje):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(titulo)
        msg.setText(mensaje)
        msg.exec_()

