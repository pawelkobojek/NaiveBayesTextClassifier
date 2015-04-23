#!/usr/bin/env python3

from sys import exit, argv

try:
    from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QFileDialog, QLabel
    from PyQt5.QtGui import QIcon
    from PyQt5.QtCore import Qt
except ImportError:
    print('PyQt5 not found!')
    print('Try: sudo apt-get install python3-pyqt5')
    exit(1)

class Learner(QWidget):

    def __init__(self):
        self.trainFileName = ''
        self.outputFileName = ''

        super().__init__()
        self.initUI()

    def initUI(self):
        # Main Window
        self.resize(800, 600)
        self.setWindowTitle('Naive Bayes Text Classifier :: Learner Module')
        self.setWindowIcon(QIcon())

        # Training Set Label
        train_label = QLabel('Training Set', self)
        train_label.move(10, 10)

        # Training Set Path Field
        self.train_field = QTextEdit(self)
        self.train_field.resize(200, 26)
        self.train_field.move(10, 30)
        self.train_field.setReadOnly(True)
        self.train_field.setAcceptRichText(False)
        self.train_field.setLineWrapMode(QTextEdit.NoWrap)
        self.train_field.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.train_field.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Training Set Load Button
        train_browse = QPushButton('Browse...', self)
        train_browse.move(210, 30)
        train_browse.clicked.connect(self.trainBrowseClicked)

        # Output Data Set Label
        dataset_label = QLabel('Output Database Path', self)
        dataset_label.move(10, 80)

        # Output Data Set Path Field
        self.dataset_field = QTextEdit(self)
        self.dataset_field.resize(200, 26)
        self.dataset_field.move(10, 100)
        self.dataset_field.setReadOnly(True)
        self.dataset_field.setAcceptRichText(False)
        self.dataset_field.setLineWrapMode(QTextEdit.NoWrap)
        self.dataset_field.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.dataset_field.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Output Data Set Load Button
        train_browse = QPushButton('Browse...', self)
        train_browse.move(210, 100)
        train_browse.clicked.connect(self.outputBrowseClicked)

        self.show()

    def trainBrowseClicked(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open Training Set file', '', 'Text files (*.txt)')
        self.trainFileName = fileName[0]
        self.fileLoaded()

    def outputBrowseClicked(self):
        fileName = QFileDialog.getSaveFileName(self, 'Save Output Database', '', 'Database file (*.dat)')
        self.outputFileName = fileName[0]
        self.fileLoaded()

    def fileLoaded(self):
        if len(self.trainFileName) != 0:
            self.train_field.setText(self.trainFileName)

        if len(self.outputFileName) != 0:
            self.dataset_field.setText(self.outputFileName)

        if len(self.outputFileName) != 0 and len(self.trainFileName) != 0:
            pass

if __name__ == '__main__':

    app = QApplication(argv)

    w = Learner()

    exit(app.exec_())