# environment: Python 3.7.0
# add the account info in account.txt under the same folder

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class email:
    def __init__(self):
        self.sender = ''
        self.password = ''
        self.receiver = ''
        self.server = ''
        self.serverPort = ''
        self.subject = ''
        self.text = ''
        self.picture = ''

    def __init__(self, filePath):
        with open(filePath, 'r') as account:
            accountInfo = account.read().split('\n')
            self.server = accountInfo[0]
            self.serverPort = accountInfo[1]
            self.sender = accountInfo[2]
            self.password = accountInfo[3]
            self.receiver = accountInfo[4]
            self.subject = accountInfo[5]
            self.text = accountInfo[6]
            self.picture = accountInfo[7]
            # print(self.picture)

    def sendMail(self):
        msg = MIMEMultipart()
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.text))
        pic_data = open(self.picture, 'rb').read()
        pic = MIMEImage(pic_data, name = os.path.basename(self.picture))
        msg.attach(pic)
        server = smtplib.SMTP_SSL(self.server, self.serverPort)
        server.login(self.sender, self.password)
        server.sendmail(self.sender, self.receiver, msg.as_string())

# newMail = email("account.txt")
# newMail.sendMail()


