import sys
import os
import time
import subprocess
import cv2
sys.path.append("../BlueTooth")
sys.path.append("../locker")
import usblock
from trylock import locker
from dbus_1 import *

if __name__ == '__main__':
	while True:
		lzy = Query()
		if(lzy == 0):#unlock
			continue
		else:#lock
			time.sleep(1)
			print("************")
			tmp = 0
			tmp = subprocess.check_output(['sudo', 'python3', 'usblock.py'])
			l = str(tmp)
			if(l[2] == 'T'):
				rel = l[2:6]
				path = l[7:-3]
			else:
				rel = l[2:7]
				path = l[8:-3]
			print("l = %s" % l)
			if ("True" in l):
				l = locker()
				l.unlock_workstation()
				os.system('sudo python3 usbDe.py')
				os.system("sudo umount -f /media/foenix/tmp")
				time.sleep(1)
			else:
				time.sleep(1)
				continue

