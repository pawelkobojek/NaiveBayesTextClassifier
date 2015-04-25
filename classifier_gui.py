#!/usr/bin/env python3

from sys import argv, exit
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem
from ui_classifier_load import Ui_LoadDatabaseWindow
from ui_classifier_main import Ui_MainWindow
from bayes import read_from_file, nb_classify_all, get_data_from_db


def center(window):
    frameGm = window.frameGeometry()
    screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
    centerPoint = QApplication.desktop().screenGeometry(screen).center()
    frameGm.moveCenter(centerPoint)
    window.move(frameGm.topLeft())


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.database = None

        self.setupUi(self)
        center(self)

        self.pushButton_classifySingle.clicked.connect(self.classify_single_clicked)
        self.plainTextEdit_classifySingle.textChanged.connect(self.classify_single_text_changed)

    def show(self):
        w = LoadDatabaseWindow()
        w.exec_()
        self.database, filename = w.get_database()

        if not self.database:
            self.close()
            return

        super(MainWindow, self).show()

        self.statusbar.showMessage('Database: %s' % filename)
        self.label_created_from.setText(self.database['created_from'])
        self.label_timeCreated.setText(self.database['time_created'])
        self.label_avg.setText('%.02f' % (self.database['total_words'] / self.database['total_examples']))
        self.label_totalArticles.setText(str(self.database['total_examples']))
        self.label_totalClasses.setText(str(len(self.database['classes'])))
        self.label_totalUnique.setText(str(self.database['unique_words']))
        self.label_totalWords.setText(str(self.database['total_words']))

        self.tableWidget_info.setRowCount(len(self.database['classes']))

        for i, c in enumerate(self.database['classes']):
            self.tableWidget_info.setItem(i, 0, QTableWidgetItem(c))
            self.tableWidget_info.setItem(i, 1, QTableWidgetItem(str(self.database['docs_per_class'][c])))
            self.tableWidget_info.setItem(i, 2, QTableWidgetItem('%.2f%%' % (self.database['prob_of_classes'][c] * 100)))

    def classify_single_clicked(self):
        text = self.plainTextEdit_classifySingle.toPlainText()
        pc, pw, vc = get_data_from_db(self.database)
        d = nb_classify_all(text, pc, pw, vc)
        d = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]

        self.tableWidget_classifySingle.setRowCount(len(d))

        for i, c in enumerate(d):
            self.tableWidget_classifySingle.setItem(i, 0, QTableWidgetItem(c[0]))
            self.tableWidget_classifySingle.setItem(i, 1, QTableWidgetItem('%.02f%%' % c[1]))

    def classify_single_text_changed(self):
        self.pushButton_classifySingle.setEnabled(len(self.plainTextEdit_classifySingle.toPlainText()) != 0)


class LoadDatabaseWindow(QDialog, Ui_LoadDatabaseWindow):
    def __init__(self):
        super(LoadDatabaseWindow, self).__init__()

        self.db_file_name = None
        self.database = None

        self.setupUi(self)
        center(self)

        self.pushButton_browseDatabase.clicked.connect(self.browse_database_clicked)
        self.pushButton_loadDatabase.clicked.connect(self.load_database_clicked)

    def browse_database_clicked(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open Database', '', 'Database File (*.dat)')
        self.db_file_name = fileName[0]
        if self.db_file_name:
            self.pushButton_loadDatabase.setEnabled(True)
            self.lineEdit_databaseFilename.setText(self.db_file_name)

    def load_database_clicked(self):
        try:
            self.database = read_from_file(self.db_file_name)
        except IOError:
            QMessageBox.critical(self, 'Error', 'Cannot load \'%s\'!' % self.db_file_name)
            self.pushButton_loadDatabase.setEnabled(False)
            return

        self.close()

    def get_database(self):
        return self.database, self.db_file_name.split('/')[-1]


if __name__ == '__main__':
    app = QApplication(argv)

    w = MainWindow()
    QTimer.singleShot(0, w.show)

    exit(app.exec_())