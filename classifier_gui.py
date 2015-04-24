#!/usr/bin/env python3

from sys import argv, exit
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_classifier_load import Ui_LoadDatabaseWindow
from ui_classifier_main import Ui_MainWindow


def center(window):
    frameGm = window.frameGeometry()
    screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
    centerPoint = QApplication.desktop().screenGeometry(screen).center()
    frameGm.moveCenter(centerPoint)
    window.move(frameGm.topLeft())


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)
        center(self)


class LoadDatabaseWindow(QMainWindow, Ui_LoadDatabaseWindow):
    def __init__(self, main_window):
        super(LoadDatabaseWindow, self).__init__()

        self.mainWindow = main_window
        self.setupUi(self)
        center(self)

        self.pushButton_browseDatabase.clicked.connect(self.browse_database_clicked)
        self.pushButton_loadDatabase.clicked.connect(self.load_database_clicked)

    def browse_database_clicked(self):
        self.pushButton_loadDatabase.setEnabled(True)

    def load_database_clicked(self):
        self.hide()
        self.mainWindow.show()


if __name__ == '__main__':
    app = QApplication(argv)

    w = MainWindow()
    lw = LoadDatabaseWindow(w)
    lw.show()

    exit(app.exec_())