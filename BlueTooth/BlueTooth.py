import os
import time
import pyautogui
import subprocess
import sys
from dbus_1 import Query
sys.path.append("../locker")
from config import config
from trylock import locker


while True:
	time.sleep(3)
	number = config['number']
	os.system("sudo hciconfig hci0 up")
	x = subprocess.check_output(['sudo','hcitool', 'cc', number], stderr=subprocess.STDOUT)
	# lzy = subprocess.check_output(['gnome-screensaver-command', '-q'])
	lzy = Query()
	if("Input/output" in str(x)):
		# os.system("gnome-screensaver-command -l")
		l = locker()
		l.lock_workstation()
	elif (lzy == 0):
		continue
	else:
		l = locker()
		l.unlock_workstation()
