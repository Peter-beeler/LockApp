import os
import time
import pyautogui
import subprocess
import sys
sys.path.append("../locker")
from config import config
from trylock import locker

while True:
	number = config['number']
	os.system("sudo hciconfig hci0 up")
	x = subprocess.check_output(['sudo','hcitool', 'cc', number], stderr=subprocess.STDOUT)
	lzy = subprocess.check_output(['gnome-screensaver-command', '-q'])
	if("Can" in str(x)):
		os.system("gnome-screensaver-command -l")
	elif ("The screensaver is inactive" in str(lzy)):
		time.sleep(3)
		continue
	else:
		l = locker()
		l.unlock_workstation()
		time.sleep(3)
