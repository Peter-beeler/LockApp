#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QLabel, QTextEdit, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5 import QtCore
from identify import TakePhoto, cutface
from Make_Rsa_Key import CreateRSAKeys
import cv2
import json
import time

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
        self.initUI()

    def setButton(self):
        self.takePhoto = QPushButton('take photo')
        self.submit = QPushButton("save config")
        self.createkeys = QPushButton('create keys')
        self.submit.clicked.connect(self.save_config)
        self.takePhoto.clicked.connect(self.getPhoto)
        self.createkeys.clicked.connect(self.createKey)

    def setTextedit(self):
        self.textedit = QTextEdit()

    def setLinedit(self):
        self.hotkey = QLineEdit()
        self.passwd = QLineEdit()
        self.passwd.setEchoMode(QLineEdit.Password)
        self.emailedit = QLineEdit()

    def setLabel(self):
        self.l = QLabel(self)
        self.l.setFixedSize(100, 100)
        self.hotkey_label = QLabel('hotkey')
        self.passwd_label = QLabel('passwd')
        self.dirs = QLabel('directories')
        self.emaillabel = QLabel('email')

    def SetLayout(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.hotkey_label,1,0)
        grid.addWidget(self.hotkey, 1, 1)
        grid.addWidget(self.passwd_label, 2, 0)
        grid.addWidget(self.passwd, 2, 1)
        grid.addWidget(self.emaillabel, 3, 0)
        grid.addWidget(self.emailedit, 3, 1)
        grid.addWidget(self.dirs, 4, 0)
        grid.addWidget(self.textedit, 4, 1)
        grid.addWidget(self.submit, 5, 0)
        grid.addWidget(self.takePhoto, 5, 1)
        grid.addWidget(self.createkeys)
        self.setLayout(grid)

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
        QMessageBox.information(self, '成功保存配置', '已成功保存您的配置特征')

    def getPhoto(self):
        self.camera = photoWidget()

    def createKey(self):
        CreateRSAKeys()
        info = '密钥生成成功，目录下的 my_private_rsa_key.bin为私钥，my_public_rsa_key.pem为公钥'
        QMessageBox.information(self, '密钥构建成功', info, QMessageBox.Ok)


class photoWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Camera'
        self.takeButton = QPushButton('take photo')
        self.takeButton.clicked.connect(self.takePhoto)
        self.cameraLabel = QLabel(self)
        layout = QVBoxLayout()
        layout.addWidget(self.cameraLabel)
        layout.addWidget(self.takeButton)
        self.setLayout(layout)
        # self.initCamera()
        # self.setTimer
        self.initUI()

    def setTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.start)
        self.timer.start(100)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.show()
        # self.takeButton.show()
        self.initCamera()

    def start(self):
        # self.initCamera()
        # self.setTimer()
        # time.sleep(1)
        ret, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        showImage = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        self.cameraLabel.setPixmap(QPixmap.fromImage(showImage))

    def initCamera(self):
        self.cap = cv2.VideoCapture(0)
        self.setTimer()
        # self.start()

    def takePhoto(self):
        TakePhoto(self.cap, 'rawface.jpg')
        cutface('rawface.jpg')
        QMessageBox.information(self, "图片采集成功", "已成功记录您的面部特征")

    def __del__(self):
        try:
            self.cap.release()
        except NameError:
            pass

def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()