
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QLabel, QTextEdit
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5 import QtCore
from LockApp.identify import TakePhoto, cutface
import cv2
import json

# TakePhoto = identify.TakePhoto
# cutface = identify.cutface

class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Device Guard'
        self.setLabel()
        self.setLinedit()
        self.setTextedit()
        self.setButton()
        self.SetLayout()
        # self.cap = cv2.VideoCapture(0)
        self.initUI()

    def setButton(self):
        self.takePhoto = QPushButton('take photo')
        self.submit = QPushButton("save config")
        self.submit.clicked.connect(self.save_config)
        self.takePhoto.clicked.connect(self.getPhoto)

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
        self.hotkey_label = QLabel('hotkey')
        self.passwd_label = QLabel('passwd')
        self.dirs = QLabel('directories:')

    def SetLayout(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.hotkey_label,1,0)
        grid.addWidget(self.hotkey, 1, 1)
        grid.addWidget(self.passwd_label, 2, 0)
        grid.addWidget(self.passwd, 2, 1)
        grid.addWidget(self.dirs, 3, 0)
        grid.addWidget(self.textedit, 3, 1)
        grid.addWidget(self.submit, 4, 0)
        grid.addWidget(self.takePhoto, 4, 1)
        self.setLayout(grid)

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
        # print(hotkey_s)
        # print(passwd_s)
        # print(dirs)
        config = {
            'lock': hotkey_s,
            'unlockPasswd': passwd_s,
            'protectDir': dirs,
        }
        m = json.dumps(config)

        f = open('config.json', 'w')
        f.write(m)
        f.close()

    def getPhoto(self):
        TakePhoto('rawface.jpg')
        cutface('rawface.jpg')

def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())