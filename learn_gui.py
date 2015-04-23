#!/usr/bin/env python3

from sys import exit, argv

try:
    from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QFileDialog, QLabel
    from PyQt5.QtGui import QIcon, QFont
    from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTime
except ImportError:
    print('PyQt5 not found!')
    print('Try: sudo apt-get install python3-pyqt5')
    exit(1)

from bayes import learn_naive_bayes, serialize_to_file

class BayesTask(QThread):
    new_status = pyqtSignal(str)
    update_calc_stat = pyqtSignal(float, float)
    new_calc_info = pyqtSignal(str)
    calc_finished = pyqtSignal(dict)

    def __init__(self, learner):
        self.filename = learner.trainFileName
        self.last_time = None

        super().__init__()

    def run(self):
        self.last_time = QTime.currentTime()
        data = learn_naive_bayes(self, self.filename)
        self.calc_finished.emit(data)

    def setNewStatus(self, status):
        self.new_status.emit(status)

    def setNewCalculationInfo(self, status):
        self.new_calc_info.emit(status)

    def updateCalculationStatus(self, total, current):
        new_time = QTime.currentTime()
        if self.last_time.msecsTo(new_time) > 100 or total == 10000 or current == 10000:
            self.update_calc_stat.emit(total, current)
            self.last_time = new_time

class Learner(QWidget):

    def __init__(self):
        self.trainFileName = ''
        self.outputFileName = ''
        self.bayes = None
        self.status_text = []

        super().__init__()
        self.initUI()

    def initUI(self):
        # Main Window
        self.resize(800, 330)
        self.setWindowTitle('Naive Bayes Text Classifier :: Learner Module')
        self.setWindowIcon(QIcon())

        # Training Set Label
        train_label = QLabel('Training Set', self)
        train_label.move(20, 20)

        # Training Set Path Field
        self.train_field = QTextEdit(self)
        self.train_field.resize(200, 26)
        self.train_field.move(20, 40)
        self.train_field.setReadOnly(True)
        self.train_field.setAcceptRichText(False)
        self.train_field.setLineWrapMode(QTextEdit.NoWrap)
        self.train_field.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.train_field.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Training Set Load Button
        self.train_browse = QPushButton('Browse...', self)
        self.train_browse.move(220, 40)
        self.train_browse.clicked.connect(self.trainBrowseClicked)

        # Output Data Set Label
        dataset_label = QLabel('Output Database Path', self)
        dataset_label.move(20, 90)

        # Output Data Set Path Field
        self.dataset_field = QTextEdit(self)
        self.dataset_field.resize(200, 26)
        self.dataset_field.move(20, 110)
        self.dataset_field.setReadOnly(True)
        self.dataset_field.setAcceptRichText(False)
        self.dataset_field.setLineWrapMode(QTextEdit.NoWrap)
        self.dataset_field.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.dataset_field.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Output Data Set Load Button
        self.output_browse = QPushButton('Browse...', self)
        self.output_browse.move(220, 110)
        self.output_browse.clicked.connect(self.outputBrowseClicked)

        # Learn Button
        self.learn_button = QPushButton('Learn', self)
        self.learn_button.move(220, 170)
        self.learn_button.setEnabled(False)
        self.learn_button.clicked.connect(self.learn)

        # Status Label
        self.status_label = QLabel('0.00%', self)
        self.status_label.move(50, 240)
        self.status_label.setFont(QFont('SansSerif', 36))
        self.status_label.setAlignment(Qt.AlignRight)
        self.status_label.setMinimumWidth(250)

        # Loading Status Area
        self.loading_status_area = QTextEdit(self)
        self.loading_status_area.setReadOnly(True)
        self.loading_status_area.move(330, 20)
        self.loading_status_area.resize(440, 280)

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
            self.learn_button.setEnabled(True)

    def learn(self):
        self.bayes = BayesTask(self)
        self.bayes.setTerminationEnabled(True)
        self.connect_thread_signals(self.bayes)
        self.bayes.start()

        self.learn_button.setEnabled(False)
        self.train_browse.setEnabled(False)
        self.output_browse.setEnabled(False)

    def setNewStatus(self, status):
        self.status_text.extend([status, '\n'])
        self.update_text_area()

    def setNewCalculationInfo(self, status):
        self.status_text.extend([status, ' [0.00%]', '\n'])
        self.update_text_area()
        pass

    def updateCalculationStatus(self, total, current):
        self.status_label.setText('%.2f%%' % (total / 100.0))
        self.status_text[-2] = ' [%.2f%%]' % (current / 100.0)
        self.update_text_area()

    def calculationFinished(self, data):
        serialize_to_file(data, self.outputFileName)
        self.status_text.extend(['Done.'])
        self.update_text_area()
        pass

    def connect_thread_signals(self, thread_obj):
        thread_obj.new_status.connect(self.setNewStatus)
        thread_obj.update_calc_stat.connect(self.updateCalculationStatus)
        thread_obj.new_calc_info.connect(self.setNewCalculationInfo)
        thread_obj.calc_finished.connect(self.calculationFinished)

    def update_text_area(self):
        txt = ''
        for t in self.status_text:
            txt = txt + t
        self.loading_status_area.setText(txt)

if __name__ == '__main__':

    app = QApplication(argv)

    w = Learner()

    exit(app.exec_())