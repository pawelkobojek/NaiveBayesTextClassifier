# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classifier_main.ui'
#
# Created: Tue May 26 20:22:06 2015
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
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_totalClasses = QtWidgets.QLabel(self.groupBox_2)
        self.label_totalClasses.setObjectName("label_totalClasses")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_totalClasses)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_totalArticles = QtWidgets.QLabel(self.groupBox_2)
        self.label_totalArticles.setObjectName("label_totalArticles")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_totalArticles)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_created_from = QtWidgets.QLabel(self.groupBox_2)
        self.label_created_from.setObjectName("label_created_from")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_created_from)
        self.label_timeCreated = QtWidgets.QLabel(self.groupBox_2)
        self.label_timeCreated.setObjectName("label_timeCreated")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_timeCreated)
        self.label_totalWords = QtWidgets.QLabel(self.groupBox_2)
        self.label_totalWords.setObjectName("label_totalWords")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_totalWords)
        self.label_totalUnique = QtWidgets.QLabel(self.groupBox_2)
        self.label_totalUnique.setObjectName("label_totalUnique")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_totalUnique)
        self.label_avg = QtWidgets.QLabel(self.groupBox_2)
        self.label_avg.setObjectName("label_avg")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_avg)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tableWidget_info = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_info.setObjectName("tableWidget_info")
        self.tableWidget_info.setColumnCount(3)
        self.tableWidget_info.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_info.setHorizontalHeaderItem(2, item)
        self.tableWidget_info.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_info.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_info.verticalHeader().setVisible(False)
        self.gridLayout_6.addWidget(self.tableWidget_info, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_loadDataset = QtWidgets.QPushButton(self.tab)
        self.pushButton_loadDataset.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_loadDataset.setObjectName("pushButton_loadDataset")
        self.gridLayout_5.addWidget(self.pushButton_loadDataset, 0, 1, 1, 1)
        self.tableWidget_calculateSet = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_calculateSet.setObjectName("tableWidget_calculateSet")
        self.tableWidget_calculateSet.setColumnCount(5)
        self.tableWidget_calculateSet.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calculateSet.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calculateSet.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calculateSet.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calculateSet.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calculateSet.setHorizontalHeaderItem(4, item)
        self.tableWidget_calculateSet.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_calculateSet.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_calculateSet.horizontalHeader().setMinimumSectionSize(80)
        self.tableWidget_calculateSet.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_calculateSet.verticalHeader().setVisible(False)
        self.gridLayout_5.addWidget(self.tableWidget_calculateSet, 1, 1, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_totalAccuracy = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_totalAccuracy.sizePolicy().hasHeightForWidth())
        self.label_totalAccuracy.setSizePolicy(sizePolicy)
        self.label_totalAccuracy.setMinimumSize(QtCore.QSize(160, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_totalAccuracy.setFont(font)
        self.label_totalAccuracy.setObjectName("label_totalAccuracy")
        self.horizontalLayout_3.addWidget(self.label_totalAccuracy)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.progressBar_classifier = QtWidgets.QProgressBar(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_classifier.sizePolicy().hasHeightForWidth())
        self.progressBar_classifier.setSizePolicy(sizePolicy)
        self.progressBar_classifier.setProperty("value", 0)
        self.progressBar_classifier.setTextVisible(False)
        self.progressBar_classifier.setObjectName("progressBar_classifier")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.progressBar_classifier)
        self.gridLayout_5.addLayout(self.formLayout_2, 2, 1, 1, 1)
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
        self.tableWidget_classifySingle.horizontalHeader().setDefaultSectionSize(150)
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Naive Bayes Text Classifier :: Main Module"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Information about database"))
        self.label.setText(_translate("MainWindow", "Total classes:"))
        self.label_totalClasses.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Total articles:"))
        self.label_totalArticles.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Total words:"))
        self.label_6.setText(_translate("MainWindow", "Total unique words:"))
        self.label_7.setText(_translate("MainWindow", "Avg words per class:"))
        self.label_8.setText(_translate("MainWindow", "Time created:"))
        self.label_9.setText(_translate("MainWindow", "Created from:"))
        self.label_created_from.setText(_translate("MainWindow", "0"))
        self.label_timeCreated.setText(_translate("MainWindow", "0"))
        self.label_totalWords.setText(_translate("MainWindow", "0"))
        self.label_totalUnique.setText(_translate("MainWindow", "0"))
        self.label_avg.setText(_translate("MainWindow", "0"))
        self.groupBox.setTitle(_translate("MainWindow", "Information about Classes"))
        item = self.tableWidget_info.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Class name"))
        item = self.tableWidget_info.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Items count"))
        item = self.tableWidget_info.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "% items"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Database info"))
        self.pushButton_loadDataset.setText(_translate("MainWindow", "Load dataset..."))
        item = self.tableWidget_calculateSet.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Class"))
        item = self.tableWidget_calculateSet.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Items count"))
        item = self.tableWidget_calculateSet.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Accuracy"))
        item = self.tableWidget_calculateSet.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Number of errors"))
        item = self.tableWidget_calculateSet.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "% of errors"))
        self.label_4.setText(_translate("MainWindow", "Total Accuracy:"))
        self.label_totalAccuracy.setText(_translate("MainWindow", "Unknown"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Text set"))
        self.pushButton_classifySingle.setText(_translate("MainWindow", "Classify Text"))
        item = self.tableWidget_classifySingle.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Class"))
        item = self.tableWidget_classifySingle.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Probability"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Single text"))

