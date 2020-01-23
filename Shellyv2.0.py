# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Shelly_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import tempfile
import subprocess
import shlex
import codecs
import sys
import time
import os.path
#from os import path
from pathlib import Path
from finestra import Ui_Dialog




class BottoneF(QtWidgets.QPushButton):

    def __init__(self, parent = None, comando = None,labeli = None):
        super().__init__(parent)
        self.labelo = labeli
        self.tipo = comando
        self.clicked.connect(lambda: self.Runna())

    def Runna(self):
        Array = []
        Array = self.tipo.split(';')
        i=0
        for x in Array:

            try:
                process = subprocess.Popen(shlex.split(x), stdout=subprocess.PIPE,shell = True)
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Status")
                msg.setText("Comando Fallito")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()


            while True:
                output = process.stdout.readline()
                if not output and process.poll() is not None:
                    break
                if output:
                    output = str(output, errors='ignore')
                    self.labelo.setText(self.labelo.text()+"\n "+output)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 141, 581))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 119, 579))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")





        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(140, 10, 641, 411))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 639, 409))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n""font-size:8pt; \n""font-weight:600; \n""color:#FFFFFF;\n""font: 8pt \"Consolas\";\n")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.i=-1
        self.Buttons = []
        self.comandi = []
        while(Path("Buttons/Documenti"+str(self.i+1)+".txt").exists()):
            f = open(Path("Buttons/Documenti"+str(self.i+1)+".txt"),"r")
            f1 = f.read()
            f1 = f1.rstrip('\n')
            x,y = f1.split('####')
            f.close()
            self.i+=1
            self.CreateButton(y,x)
        MainWindow.setCentralWidget(self.centralwidget)

        self.Aggiungi= QtWidgets.QPushButton(self.centralwidget)
        self.Aggiungi.setGeometry(QtCore.QRect(410, 500, 75, 23))
        self.Aggiungi.setObjectName("Aggiungi")
        self.Comando = QtWidgets.QTextEdit(self.centralwidget)
        self.Comando.setGeometry(QtCore.QRect(243, 440, 411, 36))
        self.Comando.setObjectName("Comando")
        self.Eseguito = QtWidgets.QProgressBar(self.centralwidget)
        self.Eseguito.setGeometry(QtCore.QRect(280, 540, 441, 23))
        self.Eseguito.setProperty("value", 0)
        self.Eseguito.setObjectName("Eseguito")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuPrincipale = QtWidgets.QMenu(self.menubar)
        self.menuPrincipale.setObjectName("menuPrincipale")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuPrincipale.addAction(self.actionNew)
        self.menuPrincipale.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuPrincipale.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.Aggiungi.clicked.connect(self.Display)#lambda: self.CreateButton(self.Comando.toPlainText().strip(),"nuovo_bottone"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Aggiungi.setText(_translate("MainWindow","Aggiungi"))
        self.menuPrincipale.setTitle(_translate("MainWindow", "Principale"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy a file"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste a file"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save a file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.Eseguito.setFormat(_translate("MainWindow", "Comandi eseguiti %p"))

    def Display(self):
        if(self.Comando.toPlainText().strip()):
            self.ui = QtWidgets.QDialog()
            self.window = Ui_Dialog(self.Comando.toPlainText().strip(),self.i)
            self.window.setupUi(self.ui)
            self.ui.exec_()
            if(Path("Buttons/Documenti"+str(self.i+1)+".txt").exists()):
                f = open(Path("Buttons/Documenti"+str(self.i+1)+".txt"),"r")
                f1 = f.read()
                f1 = f1.rstrip('\n')
                x,y = f1.split('####')
                f.close()
                self.i +=1
                self.CreateButton(y,x)

    def CreateButton(self,y,x):
        if(len(x)>15):
            t = x[0:len(x)//2]
            z = x[len(x)//2 if len(x)%2 == 0 else ((len(x)//2)+1):]

        #h = t +"\n" + z
        self.comandi.append(y)
        self.Buttons.append(BottoneF(self.scrollAreaWidgetContents,y,self.label))
        self.Buttons[self.i].setMaximumSize(QtCore.QSize(120,1000000))
        self.Buttons[self.i].setText(x)
        self.verticalLayout.addWidget(self.Buttons[self.i])
        self.Buttons[self.i].show()
        self.Buttons[self.i].setObjectName(x)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
