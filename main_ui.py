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
        MainWindow.resize(580, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(580, 600))
        MainWindow.setMaximumSize(QtCore.QSize(580, 600))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineInputFileName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineInputFileName.setGeometry(QtCore.QRect(10, 30, 491, 21))
        self.lineInputFileName.setReadOnly(True)
        self.lineInputFileName.setObjectName("lineInputFileName")
        self.pushOpenInputFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushOpenInputFile.setGeometry(QtCore.QRect(510, 12, 51, 41))
        self.pushOpenInputFile.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(255, 240, 219);\n"
"}")
        self.pushOpenInputFile.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/open-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushOpenInputFile.setIcon(icon)
        self.pushOpenInputFile.setIconSize(QtCore.QSize(32, 32))
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
        self.groupInflectOpts.setGeometry(QtCore.QRect(280, 60, 281, 51))
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
        self.pushRun = QtWidgets.QPushButton(self.centralwidget)
        self.pushRun.setGeometry(QtCore.QRect(210, 510, 51, 41))
        self.pushRun.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(255, 240, 219);\n"
"}")
        self.pushRun.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushRun.setIcon(icon1)
        self.pushRun.setIconSize(QtCore.QSize(32, 32))
        self.pushRun.setObjectName("pushRun")
        self.lineWordToFind = QtWidgets.QLineEdit(self.centralwidget)
        self.lineWordToFind.setGeometry(QtCore.QRect(10, 80, 221, 21))
        self.lineWordToFind.setObjectName("lineWordToFind")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textResults = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textResults.setGeometry(QtCore.QRect(280, 150, 281, 401))
        self.textResults.setReadOnly(True)
        self.textResults.setObjectName("textResults")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 120, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushAddWord = QtWidgets.QPushButton(self.centralwidget)
        self.pushAddWord.setGeometry(QtCore.QRect(240, 80, 21, 23))
        self.pushAddWord.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(255, 240, 219);\n"
"}")
        self.pushAddWord.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons8-plus-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushAddWord.setIcon(icon2)
        self.pushAddWord.setFlat(False)
        self.pushAddWord.setObjectName("pushAddWord")
        self.listWords = QtWidgets.QListWidget(self.centralwidget)
        self.listWords.setGeometry(QtCore.QRect(10, 150, 251, 351))
        self.listWords.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWords.setObjectName("listWords")
        self.pushSaveAs = QtWidgets.QPushButton(self.centralwidget)
        self.pushSaveAs.setGeometry(QtCore.QRect(540, 120, 21, 23))
        self.pushSaveAs.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(255, 240, 219);\n"
"}")
        self.pushSaveAs.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushSaveAs.setIcon(icon3)
        self.pushSaveAs.setObjectName("pushSaveAs")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushRemoveWord = QtWidgets.QPushButton(self.centralwidget)
        self.pushRemoveWord.setGeometry(QtCore.QRect(240, 120, 21, 23))
        self.pushRemoveWord.setStyleSheet("QPushButton:hover {\n"
"    background-color: rgb(255, 240, 219);\n"
"}")
        self.pushRemoveWord.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons8-minus-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushRemoveWord.setIcon(icon4)
        self.pushRemoveWord.setFlat(False)
        self.pushRemoveWord.setObjectName("pushRemoveWord")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 520, 201, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 21))
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
        self.label.setText(_translate("MainWindow", "File to analyze:"))
        self.groupInflectOpts.setTitle(_translate("MainWindow", "Inflect Options"))
        self.checkIng.setText(_translate("MainWindow", "-ing"))
        self.checkPlural.setText(_translate("MainWindow", "-s -es"))
        self.checkPast.setText(_translate("MainWindow", "-ed -d"))
        self.checkEr.setText(_translate("MainWindow", "-er"))
        self.pushRun.setToolTip(_translate("MainWindow", "Run Analysis"))
        self.label_3.setText(_translate("MainWindow", "Word:"))
        self.label_4.setText(_translate("MainWindow", "Results:"))
        self.pushAddWord.setToolTip(_translate("MainWindow", "Add Word"))
        self.label_5.setText(_translate("MainWindow", "List of Words to Find:"))
        self.pushRemoveWord.setToolTip(_translate("MainWindow", "Remove Word"))

import icons_rc
