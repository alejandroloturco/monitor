import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QTprincipal(QWidget):
    def __init__(self, controlador):
        super().__init__()
        self.New_controlador = controlador
        self.QTprimero()

    def QTprimero(self):
        self.setWindowTitle("Login")
        self.setFixedSize(800, 600)
        self.setStyleSheet("QWidget {"
                           "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(105, 203, 227, 255), stop:1 rgba(255, 255, 255, 255));"
                           "}"
                           "QLabel {"
                           "color: rgb(0, 180, 216);"
                           "font-family: Montserrat;"
                           "font-size: 20px;"
                           "}"
                           "QLineEdit {"
                           "border: 2px solid rgb(0, 180, 216);"
                           "border-radius: 10px;"
                           "padding: 5px;"
                           "font-family: Montserrat;"
                           "font-size: 18px;"
                           "}"
                           "QPushButton {"
                           "border-radius: 10px;"
                           "background-color: rgb(0, 180, 216);"
                           "font-family: Montserrat;"
                           "font-size: 18px;"
                           "padding: 5px;"
                           "}")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("Patient Manager")
        title.setAlignment(Qt.AlignCenter)
        title_font = QFont("Montserrat", 25, QFont.Bold)
        title.setFont(title_font)

        self.usuario_t = QLabel("Usuario:")
        self.usuario_r = QLineEdit()
        self.contraseña_t = QLabel("Contraseña:")
        self.contraseña_r = QLineEdit()
        self.contraseña_r.setEchoMode(QLineEdit.Password)

        button_layout = QHBoxLayout()
        self.boton_login = QPushButton("Ingresar")
        self.boton_salir = QPushButton("Salir")
        self.boton_salir.clicked.connect(QApplication.instance().quit)

        button_layout.addWidget(self.boton_login)
        button_layout.addWidget(self.boton_salir)

        layout.addWidget(title)
        layout.addSpacing(40)
        layout.addWidget(self.usuario_t)
        layout.addWidget(self.usuario_r)
        layout.addWidget(self.contraseña_t)
        layout.addWidget(self.contraseña_r)
        layout.addSpacing(20)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.boton_login.clicked.connect(self.login)

    def login(self):
        usuario = self.usuario_r.text()
        contraseña = self.contraseña_r.text()
        if self.New_controlador.validacion(usuario, contraseña):
            self.close()
            self.New_controlador.ventana2()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")

class QTsegundo:
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow1()
    window.show()
    sys.exit(app.exec_())
