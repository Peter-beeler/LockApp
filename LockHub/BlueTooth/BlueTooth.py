import os
import time
import pyautogui
import subprocess
import sys
from dbus_1 import Query
from ..global_api.loadconfig import load_config
from ..locker.trylock import locker


# def Start_BlueTooth():
def Start_BlueTooth():
	config = load_config()
	while True:
		time.sleep(3)
		number = config['bluetooth_num']
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
