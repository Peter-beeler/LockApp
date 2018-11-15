
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5 import QtCore
import cv2

class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Device Guard'
        # self.left = 10
        # self.top = 10
        # self.width = 640
        # self.height = 480

        # self.setTimer()
        self.setLabel()
        self.setLinedit()
        self.setTextedit()
        self.setButton()
        self.SetLayout()
        self.cap = cv2.VideoCapture(0)

        self.initUI()

    def setButton(self):
        self.submit = QPushButton("save config")
        self.submit.clicked.connect(self.save_config)

    def setTextedit(self):
        self.textedit = QTextEdit()

    def setLinedit(self):
        self.hotkey = QLineEdit()
        self.passwd = QLineEdit()
        self.passwd.setEchoMode(QLineEdit.Password)

    def setTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.start)
        self.timer.start(100)

    def setLabel(self):
        self.l = QLabel(self)
        self.l.setFixedSize(100, 100)

    def SetLayout(self):
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.hotkey)
        hbox.addWidget(self.passwd)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addWidget(self.textedit)
        vbox.addWidget(self.submit)
        self.setLayout(vbox)
        self.setGeometry(300,300, 640, 480)

    def start(self):
        ret, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        showImage = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        self.l.setPixmap(QPixmap.fromImage(showImage))
        

    def initUI(self):
        self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        # self.l.show()
        # self.hotkey.show()
        self.show()

    def save_config(self):
        hotkey_s = self.hotkey.text()
        hotkey_s = hotkey_s.split(',')
        passwd_s = self.passwd.text()
        dirs = self.textedit.toPlainText()
        dirs = dirs.split('\n')
        print(hotkey_s)
        print(passwd_s)
        print(dirs)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())