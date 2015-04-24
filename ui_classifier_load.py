# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classifier_load.ui'
#
# Created: Sat Apr 25 00:20:54 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoadDatabaseWindow(object):
    def setupUi(self, LoadDatabaseWindow):
        LoadDatabaseWindow.setObjectName("LoadDatabaseWindow")
        LoadDatabaseWindow.resize(459, 130)
        self.centralwidget = QtWidgets.QWidget(LoadDatabaseWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_databaseFilename = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_databaseFilename.setGeometry(QtCore.QRect(20, 40, 311, 27))
        self.lineEdit_databaseFilename.setReadOnly(True)
        self.lineEdit_databaseFilename.setObjectName("lineEdit_databaseFilename")
        self.label_loadDatabase = QtWidgets.QLabel(self.centralwidget)
        self.label_loadDatabase.setGeometry(QtCore.QRect(20, 20, 111, 17))
        self.label_loadDatabase.setObjectName("label_loadDatabase")
        self.pushButton_browseDatabase = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browseDatabase.setGeometry(QtCore.QRect(340, 40, 101, 27))
        self.pushButton_browseDatabase.setObjectName("pushButton_browseDatabase")
        self.pushButton_loadDatabase = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_loadDatabase.setEnabled(False)
        self.pushButton_loadDatabase.setGeometry(QtCore.QRect(20, 80, 421, 31))
        self.pushButton_loadDatabase.setObjectName("pushButton_loadDatabase")
        LoadDatabaseWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoadDatabaseWindow)
        QtCore.QMetaObject.connectSlotsByName(LoadDatabaseWindow)
        LoadDatabaseWindow.setTabOrder(self.pushButton_browseDatabase, self.pushButton_loadDatabase)
        LoadDatabaseWindow.setTabOrder(self.pushButton_loadDatabase, self.lineEdit_databaseFilename)

    def retranslateUi(self, LoadDatabaseWindow):
        _translate = QtCore.QCoreApplication.translate
        LoadDatabaseWindow.setWindowTitle(_translate("LoadDatabaseWindow", "Naive Bayes Text Classifier"))
        self.label_loadDatabase.setText(_translate("LoadDatabaseWindow", "Load Database"))
        self.pushButton_browseDatabase.setText(_translate("LoadDatabaseWindow", "Browse..."))
        self.pushButton_loadDatabase.setText(_translate("LoadDatabaseWindow", "Load"))

