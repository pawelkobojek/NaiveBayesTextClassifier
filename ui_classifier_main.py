# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classifier_main.ui'
#
# Created: Sat Apr 25 21:03:39 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit_classifySingle = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_classifySingle.setObjectName("plainTextEdit_classifySingle")
        self.gridLayout_2.addWidget(self.plainTextEdit_classifySingle, 0, 0, 1, 1)
        self.pushButton_classifySingle = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_classifySingle.sizePolicy().hasHeightForWidth())
        self.pushButton_classifySingle.setSizePolicy(sizePolicy)
        self.pushButton_classifySingle.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_classifySingle.setObjectName("pushButton_classifySingle")
        self.gridLayout_2.addWidget(self.pushButton_classifySingle, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tableWidget_classifySingle = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_classifySingle.setMaximumSize(QtCore.QSize(300, 16777215))
        self.tableWidget_classifySingle.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_classifySingle.setRowCount(0)
        self.tableWidget_classifySingle.setObjectName("tableWidget_classifySingle")
        self.tableWidget_classifySingle.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_classifySingle.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_classifySingle.setHorizontalHeaderItem(1, item)
        self.tableWidget_classifySingle.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_classifySingle.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_classifySingle.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.tableWidget_classifySingle, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Naive Bayes Text Classifier :: Main Module"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Database info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Text set"))
        self.pushButton_classifySingle.setText(_translate("MainWindow", "Classify Text"))
        item = self.tableWidget_classifySingle.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Class"))
        item = self.tableWidget_classifySingle.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Probability"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Single text"))

