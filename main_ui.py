# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineInputFileName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineInputFileName.setGeometry(QtCore.QRect(10, 30, 491, 21))
        self.lineInputFileName.setReadOnly(True)
        self.lineInputFileName.setObjectName("lineInputFileName")
        self.pushOpenInputFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushOpenInputFile.setGeometry(QtCore.QRect(510, 30, 75, 23))
        self.pushOpenInputFile.setFlat(False)
        self.pushOpenInputFile.setObjectName("pushOpenInputFile")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupInflectOpts = QtWidgets.QGroupBox(self.centralwidget)
        self.groupInflectOpts.setGeometry(QtCore.QRect(280, 60, 221, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupInflectOpts.setFont(font)
        self.groupInflectOpts.setObjectName("groupInflectOpts")
        self.checkIng = QtWidgets.QCheckBox(self.groupInflectOpts)
        self.checkIng.setGeometry(QtCore.QRect(10, 20, 41, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkIng.setFont(font)
        self.checkIng.setObjectName("checkIng")
        self.checkPlural = QtWidgets.QCheckBox(self.groupInflectOpts)
        self.checkPlural.setGeometry(QtCore.QRect(60, 20, 51, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkPlural.setFont(font)
        self.checkPlural.setObjectName("checkPlural")
        self.checkPast = QtWidgets.QCheckBox(self.groupInflectOpts)
        self.checkPast.setGeometry(QtCore.QRect(120, 20, 51, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkPast.setFont(font)
        self.checkPast.setObjectName("checkPast")
        self.checkEr = QtWidgets.QCheckBox(self.groupInflectOpts)
        self.checkEr.setGeometry(QtCore.QRect(180, 20, 41, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkEr.setFont(font)
        self.checkEr.setObjectName("checkEr")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineOutputFileName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineOutputFileName.setGeometry(QtCore.QRect(10, 140, 491, 21))
        self.lineOutputFileName.setReadOnly(True)
        self.lineOutputFileName.setObjectName("lineOutputFileName")
        self.pushOpenOutputFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushOpenOutputFile.setGeometry(QtCore.QRect(510, 140, 75, 23))
        self.pushOpenOutputFile.setFlat(False)
        self.pushOpenOutputFile.setObjectName("pushOpenOutputFile")
        self.pushRun = QtWidgets.QPushButton(self.centralwidget)
        self.pushRun.setGeometry(QtCore.QRect(510, 80, 75, 23))
        self.pushRun.setObjectName("pushRun")
        self.lineWordToFind = QtWidgets.QLineEdit(self.centralwidget)
        self.lineWordToFind.setGeometry(QtCore.QRect(10, 80, 261, 21))
        self.lineWordToFind.setObjectName("lineWordToFind")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Word Frequency Analyzer"))
        self.pushOpenInputFile.setText(_translate("MainWindow", "Open..."))
        self.label.setText(_translate("MainWindow", "File to analyze:"))
        self.groupInflectOpts.setTitle(_translate("MainWindow", "Inflect Options"))
        self.checkIng.setText(_translate("MainWindow", "-ing"))
        self.checkPlural.setText(_translate("MainWindow", "-s -es"))
        self.checkPast.setText(_translate("MainWindow", "-ed -d"))
        self.checkEr.setText(_translate("MainWindow", "-er"))
        self.label_2.setText(_translate("MainWindow", "File to save results:"))
        self.pushOpenOutputFile.setText(_translate("MainWindow", "Open..."))
        self.pushRun.setText(_translate("MainWindow", "Run"))
        self.label_3.setText(_translate("MainWindow", "Word:"))
