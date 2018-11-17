import os
import sys
import time
sys.path.append("../locker")
from config import config

passwd = config['unlockPasswd']
os.system("hciconfig hci0 up")
number = config['number']
Command = 'hcitool cc ' + number

while True:
	time.sleep(4)
	x = os.system(Command)
	print(x)