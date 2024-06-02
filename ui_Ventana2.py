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


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_regresar.clicked.connect(self.on_regresar_clicked)
        self.pushButton_salir.clicked.connect(self.on_salir_clicked)
        self.pushButton_ingresar.clicked.connect(self.on_ingresar_clicked)
        self.pushButton_buscar.clicked.connect(self.on_buscar_clicked)

    def on_regresar_clicked(self):
        print("Regresar button clicked")
        self.close()
        self.New_controlador.ventana2()

    def on_salir_clicked(self):
        print("Salir button clicked")
        QApplication.quit()

    def on_ingresar_clicked(self):
        print("Ingresar paciente button clicked")

    def on_buscar_clicked(self):
        print("Buscar paciente button clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
