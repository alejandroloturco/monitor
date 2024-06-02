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
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(170, 210, 81, 21))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "}")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(140, 270, 111, 21))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "}")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(QRect(260, 210, 251, 22))
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "    border-radius: 10px;\n"
                                    "    background-color:rgb(237, 254, 255);\n"
                                    "}")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(260, 270, 251, 22))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 10px;\n"
                                      "    background-color:rgb(237, 254, 255);\n"
                                      "}")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(250, 380, 93, 28))
        font1 = QFont()
        font1.setFamily("Montserrat")
        font1.setPointSize(8)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    border-radius: 10px;\n"
                                      "    background-color: rgb(0, 180, 216);\n"
                                      "}")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QRect(410, 380, 93, 28))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    border-radius: 10px;\n"
                                        "    background-color: rgb(0, 180, 216);\n"
                                        "}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(190, 50, 431, 61))
        font2 = QFont()
        font2.setFamily("Montserrat")
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setStyleSheet("QLabel{\n"
                                 "    color: rgb(0, 180, 216);\n"
                                 "}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(300, 320, 181, 21))
        font3 = QFont()
        font3.setPointSize(10)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet("QLabel{\n"
                                   "    color: rgb(0, 119, 182);\n"
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Usuario:</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Contraseña:</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Ingresar"))
        self.pushButton_2.setText(_translate("MainWindow", "Salir"))
        self.label.setText(_translate("MainWindow", "Patient Manager"))
        self.label_2.setText("")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_ingresar_clicked)
        self.pushButton_2.clicked.connect(self.on_salir_clicked)

    def on_ingresar_clicked(self):
        # Define the action for the "Ingresar" button
        usuario = self.lineEdit.text()
        contrasena = self.lineEdit_2.text()
        print(f"Usuario: {usuario}\nContraseña: {contrasena}")

    def on_salir_clicked(self):
        # Define the action for the "Salir" button
        print("Salir button clicked")
        QApplication.quit()

