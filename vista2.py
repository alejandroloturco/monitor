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

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
                                 "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(105, 203, 227, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_regresar = QPushButton(self.centralwidget)
        self.pushButton_regresar.setObjectName("pushButton_regresar")
        self.pushButton_regresar.setGeometry(QRect(270, 450, 93, 28))
        font = QFont()
        font.setFamily("Montserrat")
        self.pushButton_regresar.setFont(font)
        self.pushButton_regresar.setStyleSheet("QPushButton{\n"
                                               "    border-radius: 10px;\n"
                                               "    background-color: rgb(0, 180, 216);\n"
                                               "}")
        self.pushButton_salir = QPushButton(self.centralwidget)
        self.pushButton_salir.setObjectName("pushButton_salir")
        self.pushButton_salir.setGeometry(QRect(390, 450, 93, 28))
        self.pushButton_salir.setFont(font)
        self.pushButton_salir.setStyleSheet("QPushButton{\n"
                                            "    border-radius: 10px;\n"
                                            "    background-color: rgb(0, 180, 216);\n"
                                            "}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(190, 30, 431, 61))
        font1 = QFont()
        font1.setFamily("Montserrat")
        font1.setPointSize(25)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet("QLabel{\n"
                                 "    color: rgb(0, 180, 216);\n"
                                 "}")
        self.pushButton_ingresar = QPushButton(self.centralwidget)
        self.pushButton_ingresar.setObjectName("pushButton_ingresar")
        self.pushButton_ingresar.setGeometry(QRect(270, 220, 211, 41))
        self.pushButton_ingresar.setFont(font)
        self.pushButton_ingresar.setStyleSheet("QPushButton{\n"
                                               "    border-radius: 10px;\n"
                                               "    background-color: rgb(0, 180, 216);\n"
                                               "}")
        self.pushButton_buscar = QPushButton(self.centralwidget)
        self.pushButton_buscar.setObjectName("pushButton_buscar")
        self.pushButton_buscar.setGeometry(QRect(270, 300, 211, 41))
        self.pushButton_buscar.setFont(font)
        self.pushButton_buscar.setStyleSheet("QPushButton{\n"
                                             "    border-radius: 10px;\n"
                                             "    background-color: rgb(0, 180, 216);\n"
                                             "}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_regresar.setText(_translate("MainWindow", "Regresar"))
        self.pushButton_salir.setText(_translate("MainWindow", "Salir"))
        self.label.setText(_translate("MainWindow", "Patient Manager"))
        self.pushButton_ingresar.setText(_translate("MainWindow", "Ingresar paciente "))
        self.pushButton_buscar.setText(_translate("MainWindow", "Buscar paciente"))


class MainWindow2(QMainWindow, Ui_MainWindow2):
    def __init__(self,controlador):
        super(MainWindow2, self).__init__()
        self.New_controlador = controlador
        self.setupUi(self)
        self.pushButton_regresar.clicked.connect(self.on_regresar_clicked)
        self.pushButton_salir.clicked.connect(self.on_salir_clicked)
        self.pushButton_ingresar.clicked.connect(self.on_ingresar_clicked)
        self.pushButton_buscar.clicked.connect(self.on_buscar_clicked)

    def on_regresar_clicked(self):
        self.close()
        self.New_controlador.ventana1()

    def on_salir_clicked(self):
        self.close()
        self.New_controlador.ventana1()

    def on_ingresar_clicked(self):
        self.close()
        self.New_controlador.ventana3()

    def on_buscar_clicked(self):
        self.close()
        self.New_controlador.ventana4()

class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
                                 "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(105, 203, 227, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(270, 430, 93, 28))
        font = QFont()
        font.setFamily("Montserrat")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    border-radius: 10px;\n"
                                      "    background-color: rgb(0, 180, 216);\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QRect(440, 430, 93, 28))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    border-radius: 10px;\n"
                                        "    background-color: rgb(0, 180, 216);\n"
                                        "}\n"
                                        "\n"
                                        "")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(200, 50, 431, 61))
        font1 = QFont()
        font1.setFamily("Montserrat")
        font1.setPointSize(25)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet("QLabel{\n"
                                 "    color: rgb(0, 180, 216);\n"
                                 "}")
        self.lineEdit_nombre = QLineEdit(self.centralwidget)
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.lineEdit_nombre.setGeometry(QRect(280, 160, 281, 22))
        self.lineEdit_apellido = QLineEdit(self.centralwidget)
        self.lineEdit_apellido.setObjectName("lineEdit_apellido")
        self.lineEdit_apellido.setGeometry(QRect(280, 200, 281, 22))
        self.lineEdit_edad = QLineEdit(self.centralwidget)
        self.lineEdit_edad.setObjectName("lineEdit_edad")
        self.lineEdit_edad.setGeometry(QRect(280, 240, 281, 22))
        self.lineEdit_identificacion = QLineEdit(self.centralwidget)
        self.lineEdit_identificacion.setObjectName("lineEdit_identificacion")
        self.lineEdit_identificacion.setGeometry(QRect(280, 280, 281, 22))
        self.pushButton_guardar = QPushButton(self.centralwidget)
        self.pushButton_guardar.setObjectName("pushButton_guardar")
        self.pushButton_guardar.setGeometry(QRect(370, 370, 93, 28))
        self.pushButton_guardar.setStyleSheet("QPushButton{\n"
                                              "    border-radius: 10px;\n"
                                              "    background-color: rgb(0, 180, 216);\n"
                                              "}\n"
                                              "\n"
                                              "")
        self.label_nombre = QLabel(self.centralwidget)
        self.label_nombre.setObjectName("label_nombre")
        self.label_nombre.setGeometry(QRect(200, 160, 55, 16))
        self.label_apellido = QLabel(self.centralwidget)
        self.label_apellido.setObjectName("label_apellido")
        self.label_apellido.setGeometry(QRect(210, 200, 55, 16))
        self.label_edad = QLabel(self.centralwidget)
        self.label_edad.setObjectName("label_edad")
        self.label_edad.setGeometry(QRect(210, 240, 55, 16))
        self.label_identificacion = QLabel(self.centralwidget)
        self.label_identificacion.setObjectName("label_identificacion")
        self.label_identificacion.setGeometry(QRect(190, 280, 81, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Regresar"))
        self.pushButton_2.setText(_translate("MainWindow", "Salir"))
        self.label.setText(_translate("MainWindow", "Patient Manager"))
        self.pushButton_guardar.setText(_translate("MainWindow", "Guardar"))
        self.label_nombre.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Nombre:</p></body></html>"))
        self.label_apellido.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Apellido:</p></body></html>"))
        self.label_edad.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Edad:</p></body></html>"))
        self.label_identificacion.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Identificacion:</p></body></html>"))

class MainWindow3(QMainWindow, Ui_MainWindow3):
    def __init__(self,controlador):
        super(MainWindow3, self).__init__()
        self.New_controlador = controlador
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_regresar_clicked)
        self.pushButton_2.clicked.connect(self.on_salir_clicked)
        self.pushButton_guardar.clicked.connect(self.on_guardar_clicked)

    def on_regresar_clicked(self):
        self.close()
        self.New_controlador.ventana2()

    def on_salir_clicked(self):
        self.close()
        self.New_controlador.ventana1()        

    def on_guardar_clicked(self):
        # Define the action for the "Guardar" button
        nombre = self.lineEdit_nombre.text()
        apellido = self.lineEdit_apellido.text()
        edad = self.lineEdit_edad.text()
        id = self.lineEdit_identificacion.text()
        self.New_controlador.agregar(nombre,apellido,edad,id)
        self.lineEdit_nombre.clear()
        self.lineEdit_apellido.clear()
        self.lineEdit_edad.clear()
        self.lineEdit_identificacion.clear()
        QMessageBox.information(self, "Operacion exitosa", "Se agrego al paciente correctamente")

class Ui_MainWindow4(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
                                 "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(105, 203, 227, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(250, 500, 93, 28))
        font = QFont()
        font.setFamily("Montserrat")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    border-radius: 10px;\n"
                                      "    background-color: rgb(0, 180, 216);\n"
                                      "}")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QRect(410, 500, 93, 28))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    border-radius: 10px;\n"
                                        "    background-color: rgb(0, 180, 216);\n"
                                        "}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(190, 50, 431, 61))
        font1 = QFont()
        font1.setFamily("Montserrat")
        font1.setPointSize(25)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet("QLabel{\n"
                                 "    color: rgb(0, 180, 216);\n"
                                 "}")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setGeometry(QRect(100, 220, 650, 160))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Nombre", "Apellido", "Edad", "Cedula","Eliminar"])
        self.lineEdit_search = QLineEdit(self.centralwidget)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.lineEdit_search.setGeometry(QRect(240, 170, 301, 22))
        self.pushButton_buscar = QPushButton(self.centralwidget)
        self.pushButton_buscar.setObjectName("pushButton_buscar")
        self.pushButton_buscar.setGeometry(QRect(240, 400, 93, 28))
        self.pushButton_buscar.setFont(font)
        self.pushButton_buscar.setStyleSheet("QPushButton{\n"
                                             "    border-radius: 10px;\n"
                                             "    background-color: rgb(0, 180, 216);\n"
                                             "}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(100, 170, 131, 20))
        self.label_2.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Regresar"))
        self.pushButton_2.setText(_translate("MainWindow", "Salir"))
        self.label.setText(_translate("MainWindow", "Patient Manager"))
        self.pushButton_buscar.setText(_translate("MainWindow", "Buscar"))
        self.label_2.setText(_translate("MainWindow", "Ingrese el nombre:"))


class MainWindow4(QMainWindow, Ui_MainWindow4):
    def __init__(self,controlador):
        super(MainWindow4, self).__init__()        
        self.New_controlador = controlador
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_regresar_clicked)
        self.pushButton_2.clicked.connect(self.on_salir_clicked)
        self.pushButton_buscar.clicked.connect(self.on_buscar_clicked)

    def on_regresar_clicked(self):
        self.close()
        self.New_controlador.ventana2() 

    def on_salir_clicked(self):
        self.close()
        self.New_controlador.ventana1() 

    def on_buscar_clicked(self):
        pal = self.lineEdit_search.text()
        lista = self.New_controlador.buscar(pal)
        self.tableWidget.setRowCount(0)
        for i in lista:
            self.tabla_pacientes(i)
    
    def tabla_pacientes(self, paciente):
        posicion = self.tableWidget.rowCount()
        self.tableWidget.insertRow(posicion)
        self.tableWidget.setItem(posicion, 0, QTableWidgetItem(paciente[0]))
        self.tableWidget.setItem(posicion, 1, QTableWidgetItem(paciente[1]))
        self.tableWidget.setItem(posicion, 2, QTableWidgetItem(paciente[2]))
        self.tableWidget.setItem(posicion, 3, QTableWidgetItem(paciente[3]))
        self.tableWidget.setCellWidget(posicion, 4, self.boton_eliminar(paciente[3]))
    
    def boton_eliminar(self, cedula):
        boton = QPushButton("Eliminar")
        boton.clicked.connect(lambda: self.eliminar(cedula))
        return boton

    def eliminar(self, cedula):
        self.New_controlador.eliminar(cedula)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
    
