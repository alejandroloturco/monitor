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
        self.tableWidget.setGeometry(QRect(240, 230, 301, 151))
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


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_regresar_clicked)
        self.pushButton_2.clicked.connect(self.on_salir_clicked)
        self.pushButton_buscar.clicked.connect(self.on_buscar_clicked)

    def on_regresar_clicked(self):
        print("Regresar button clicked")

    def on_salir_clicked(self):
        print("Salir button clicked")
        QApplication.quit()

    def on_buscar_clicked(self):
        print("Buscar button clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
