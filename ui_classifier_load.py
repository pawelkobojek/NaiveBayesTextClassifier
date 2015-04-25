# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classifier_load.ui'
#
# Created: Sat Apr 25 18:15:49 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoadDatabaseWindow(object):
    def setupUi(self, LoadDatabaseWindow):
        LoadDatabaseWindow.setObjectName("LoadDatabaseWindow")
        LoadDatabaseWindow.resize(460, 130)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoadDatabaseWindow.sizePolicy().hasHeightForWidth())
        LoadDatabaseWindow.setSizePolicy(sizePolicy)
        LoadDatabaseWindow.setMinimumSize(QtCore.QSize(460, 130))
        LoadDatabaseWindow.setMaximumSize(QtCore.QSize(460, 130))
        self.pushButton_browseDatabase = QtWidgets.QPushButton(LoadDatabaseWindow)
        self.pushButton_browseDatabase.setGeometry(QtCore.QRect(340, 40, 101, 27))
        self.pushButton_browseDatabase.setObjectName("pushButton_browseDatabase")
        self.pushButton_loadDatabase = QtWidgets.QPushButton(LoadDatabaseWindow)
        self.pushButton_loadDatabase.setEnabled(False)
        self.pushButton_loadDatabase.setGeometry(QtCore.QRect(20, 80, 421, 31))
        self.pushButton_loadDatabase.setObjectName("pushButton_loadDatabase")
        self.label_loadDatabase = QtWidgets.QLabel(LoadDatabaseWindow)
        self.label_loadDatabase.setGeometry(QtCore.QRect(20, 20, 111, 17))
        self.label_loadDatabase.setObjectName("label_loadDatabase")
        self.lineEdit_databaseFilename = QtWidgets.QLineEdit(LoadDatabaseWindow)
        self.lineEdit_databaseFilename.setGeometry(QtCore.QRect(20, 40, 311, 27))
        self.lineEdit_databaseFilename.setReadOnly(True)
        self.lineEdit_databaseFilename.setObjectName("lineEdit_databaseFilename")

        self.retranslateUi(LoadDatabaseWindow)
        QtCore.QMetaObject.connectSlotsByName(LoadDatabaseWindow)

    def retranslateUi(self, LoadDatabaseWindow):
        _translate = QtCore.QCoreApplication.translate
        LoadDatabaseWindow.setWindowTitle(_translate("LoadDatabaseWindow", "Naive Bayes Classifier"))
        self.pushButton_browseDatabase.setText(_translate("LoadDatabaseWindow", "Browse..."))
        self.pushButton_loadDatabase.setText(_translate("LoadDatabaseWindow", "Load"))
        self.label_loadDatabase.setText(_translate("LoadDatabaseWindow", "Load Database"))

