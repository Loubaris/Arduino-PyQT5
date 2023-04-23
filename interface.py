# -*- coding: utf-8 -*-

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

# DETECT PLATFORM
perm = 0

from sys import platform

if platform == "linux" or platform == "linux2":
    perm = 1



#IMPORTER LES PACKAGES

try:
    import serial
    import serial.tools.list_ports
except:
    print("Erreur durant le chargement du package 'Serial'\nLancement du téléchargement")
    install("pyserial")


try:
    import subprocess
except:
    print("Erreur durant le chargement du package 'subprocess'\nLancement du téléchargement")
    install("subprocess")

try:
    import pyfirmata
except:
    print("Erreur durant le chargement du package 'Pyfirmata'\nLancement du téléchargement")
    install("pyfirmata")


#INSTALLER LES PACKAGES INTROUVABLES
def install(package):
    system.os("python3 -m pip install {}".format(package))
    
# PLUG ARDUINO

plugpage = False
plugstart = 0
portlist = serial.tools.list_ports.comports()
erreurport = ""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background: #EAF2EF;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(40, 10, 91, 41))
        self.title.setStyleSheet("background: transparent;\n"
"font: 81 22pt \"Cantarell\";\n"
"color: black;")
        self.title.setObjectName("title")
        self.line1 = QtWidgets.QFrame(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(60, 50, 44, 3))
        self.line1.setMinimumSize(QtCore.QSize(0, 0))
        self.line1.setMaximumSize(QtCore.QSize(16777211, 16777215))
        self.line1.setStyleSheet("background-color: white;\n"
"color: black;")
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.notification = QtWidgets.QPushButton(self.centralwidget)
        self.notification.setGeometry(QtCore.QRect(750, 10, 31, 31))
        self.notification.setAutoFillBackground(False)
        self.notification.setStyleSheet("")
        self.notification.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/notification.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notification.setIcon(icon)
        self.notification.setIconSize(QtCore.QSize(30, 30))
        self.notification.setFlat(True)
        self.notification.setObjectName("notification")
        self.information = QtWidgets.QLabel(self.centralwidget)
        self.information.setGeometry(QtCore.QRect(30, 140, 111, 181))
        self.information.setStyleSheet("background-color: #fcf1eb;\n"
"background: qlineargradient(x1:0, y1:0, x10:1, y2:2, stop: 0 rgb(234, 242, 239), stop:0.7 rgba(151, 197, 230));\n"
"border-radius: 15px;")
        self.information.setText("")
        self.information.setObjectName("information")
        self.arduino = QtWidgets.QLabel(self.centralwidget)
        self.arduino.setGeometry(QtCore.QRect(170, 140, 111, 181))
        self.arduino.setStyleSheet("background-color: #fcf1eb;\n"
"background: qlineargradient(x1:0, y1:0, x10:1, y2:2, stop: 0 rgb(234, 242, 239), stop:0.7 rgb(37, 150, 190));\n"
"border-radius: 15px;")
        self.arduino.setText("")
        self.arduino.setObjectName("arduino")
        self.liaison = QtWidgets.QLabel(self.centralwidget)
        self.liaison.setGeometry(QtCore.QRect(310, 140, 111, 181))
        self.liaison.setStyleSheet("background-color: #fcf1eb;\n"
"background: qlineargradient(x1:0, y1:0, x10:1, y2:2, stop: 0 rgb(234, 242, 239), stop:0.7 rgb(18, 78, 120));\n"
"border-radius: 15px;")
        self.liaison.setText("")
        self.liaison.setObjectName("liaison")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 160, 71, 71))
        self.label.setStyleSheet("background: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/arduino.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.bluetoothbutton = QtWidgets.QPushButton(self.centralwidget)
        self.bluetoothbutton.setGeometry(QtCore.QRect(180, 270, 91, 31))
        self.bluetoothbutton.setStyleSheet("QPushButton#bluetoothbutton {\n"
"color: black;\n"
"font: 75 13pt \"Bitstream Vera Sans\";\n"
"background-color: white;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton#bluetoothbutton:hover {\n"
"color: black;\n"
"font: 75 13pt \"Bitstream Vera Sans\";\n"
"background-color: #F0F0C9;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#bluetoothbutton:pressed{\n"
"color: black;\n"
"font: 75 13pt \"Bitstream Vera Sans\";\n"
"background-color: #F0F0C9;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.bluetoothbutton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/bluetooth.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bluetoothbutton.setIcon(icon1)
        self.bluetoothbutton.setIconSize(QtCore.QSize(25, 22))
        self.bluetoothbutton.setFlat(True)
        self.bluetoothbutton.setObjectName("bluetoothbutton")
        self.arduinopair = QtWidgets.QWidget(self.centralwidget)
        self.arduinopair.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.arduinopair.setObjectName("arduinopair")
        self.title_2 = QtWidgets.QLabel(self.arduinopair)
        self.title_2.setGeometry(QtCore.QRect(40, 10, 91, 41))
        self.title_2.setStyleSheet("background: transparent;\n"
"font: 81 22pt \"Cantarell\";\n"
"color: black;")
        self.title_2.setObjectName("title_2")
        self.line1_2 = QtWidgets.QFrame(self.arduinopair)
        self.line1_2.setGeometry(QtCore.QRect(60, 50, 49, 3))
        self.line1_2.setMinimumSize(QtCore.QSize(0, 0))
        self.line1_2.setMaximumSize(QtCore.QSize(16777211, 16777215))
        self.line1_2.setStyleSheet("background-color: white;\n"
"color: black;")
        self.line1_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1_2.setObjectName("line1_2")
        self.plugbutton = QtWidgets.QPushButton(self.arduinopair)
        self.plugbutton.setGeometry(QtCore.QRect(730, 530, 51, 51))
        self.plugbutton.setStyleSheet("QPushButton#plugbutton {\n"
"color: black;\n"
"font: 75 13pt \"Bitstream Vera Sans\";\n"
"background-color: white;\n"
"border-radius: 10px;\n"
"border: 2px solid black;\n"
"}\n"
"QPushButton#plugbutton:hover {\n"
"color: black;\n"
"font: 75 13pt \"Bitstream Vera Sans\";\n"
"background-color: #F0F0C9;\n"
"border-radius: 10px;\n"
"border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton#plugbutton:pressed{\n"
"color: black;\n"
"font: 75 13pt \"Bitstream Vera Sans\";\n"
"background-color: #F0F0C9;\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.plugbutton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/power.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plugbutton.setIcon(icon2)
        self.plugbutton.setIconSize(QtCore.QSize(40, 40))
        self.plugbutton.setFlat(True)
        self.plugbutton.setObjectName("plugbutton")
        self.arduinowidget = QtWidgets.QWidget(self.arduinopair)
        self.arduinowidget.setGeometry(QtCore.QRect(0, 60, 801, 461))
        self.arduinowidget.setObjectName("arduinowidget")
        self.listWidget = QtWidgets.QListWidget(self.arduinowidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 60, 141, 171))
        self.listWidget.setStyleSheet("border: 2px solid black;\n"
"border-radius: 15px;\n"
"color: #191919;")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.arduinoportlineedit = QtWidgets.QLineEdit(self.arduinowidget)
        self.arduinoportlineedit.setGeometry(QtCore.QRect(31, 240, 113, 33))
        self.arduinoportlineedit.setStyleSheet("border: 3px solid black,;\n"
"border-radius: 10px;\n"
"color: #4287f5;\n"
"font: 11pt \"MathJax_Size4\";")
        self.arduinoportlineedit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.arduinoportlineedit.setDragEnabled(False)
        self.arduinoportlineedit.setClearButtonEnabled(False)
        self.arduinoportlineedit.setObjectName("arduinoportlineedit")
        self.textearduinoblebrowser = QtWidgets.QTextBrowser(self.arduinowidget)
        self.textearduinoblebrowser.setGeometry(QtCore.QRect(250, 60, 301, 111))
        self.textearduinoblebrowser.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;\n"
"color: black;")
        self.textearduinoblebrowser.setObjectName("textearduinoblebrowser")
        self.connectionbutton = QtWidgets.QPushButton(self.arduinowidget)
        self.connectionbutton.setGeometry(QtCore.QRect(30, 280, 113, 31))
        self.connectionbutton.setStyleSheet("border-radius: 10px;\n"
"color: #4287f5;\n"
"border: 3px solid black;")
        self.connectionbutton.setObjectName("connectionbutton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        
        # DEBUT

        self.arduinopair.hide()
        self.arduinowidget.hide()

        # BOUTONS


        self.bluetoothbutton.clicked.connect(self.arduinopair.show)
        self.plugbutton.clicked.connect(self.plugarduino)
        self.connectionbutton.clicked.connect(self.connectarduino)



        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MalSpace"))
        self.title.setText(_translate("MainWindow", "Accueil"))
        self.title_2.setText(_translate("MainWindow", "Clé BLE"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "    Listes des ports"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.arduinoportlineedit.setPlaceholderText(_translate("MainWindow", " Nom du port"))
        self.textearduinoblebrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Recopiez le nom exact du port auquel</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">votre clé BLE est connectée puis</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">connectez vous.</span></p></body></html>"))
        self.connectionbutton.setText(_translate("MainWindow", "CONNEXION"))



    def plugarduino(self):
        global plugstart
        global plugpage
        global portlist
        if plugstart == 0:
            plugstart = 1
            for port in portlist:
                self.listWidget.addItem(str(port))
        if plugpage == False:
            self.arduinowidget.show()
            plugpage = True
        elif plugpage == True:
            self.arduinowidget.hide()
            plugpage = False

    def connectarduino(self):
        global erreurport
        avr_port = self.arduinoportlineedit.text()
        if avr_port == "ERREUR1" or avr_port == "erreur1":
            if perm == 1:
                print("Système détécté 'LINUX'")
                os.system("notify-send 'Permission' 'Vous recevrez une demande d authentification afin de régler le problème de permission.'")
                subprocess.call('sudo chmod 777 {}'.format(erreurport), shell = True)
            else:
                print("Système windows")
        else:
            avr_port_split = avr_port.split(" ")
            avr_port = avr_port_split[0]
            try:
                board = pyfirmata.Arduino(avr_port)
                print("Connexion clé BLE réussite")
            except:
                print("Erreur de connexion avec la clé BLE\n Erreur possibles:")
                self.textearduinoblebrowser.append("<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Il y'a eu une erreur de connexion avec la clé</span></p>\n")
                self.textearduinoblebrowser.append("<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Les causes problables sont:</span></p>\n")
                self.textearduinoblebrowser.append("<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Mauvais port, essayez un autre.</span></p>\n")
                self.textearduinoblebrowser.append("<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Écrivez ERREUR1 pour essayer de</span></p>\n")
                self.textearduinoblebrowser.append("<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">régler la permission de connexion au port.</span></p>")
                erreurport = avr_port


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())