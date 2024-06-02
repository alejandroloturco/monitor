import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
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

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_regresar_clicked)
        self.pushButton_2.clicked.connect(self.on_salir_clicked)
        self.pushButton_guardar.clicked.connect(self.on_guardar_clicked)

    def on_regresar_clicked(self):
        # Define the action for the "Regresar" button
        print("Regresar button clicked")

    def on_salir_clicked(self):
        # Define the action for the "Salir" button
        print("Salir button clicked")
        QApplication.quit()

    def on_guardar_clicked(self):
        # Define the action for the "Guardar" button
        nombre = self.lineEdit_nombre.text()
        apellido = self.lineEdit_apellido.text()
        edad = self.lineEdit_edad.text()
        identificacion = self.lineEdit_identificacion.text()
        print(f"Datos guardados:\nNombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nIdentificacion: {identificacion}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
