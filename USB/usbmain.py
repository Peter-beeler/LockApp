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
		# test()
		# print("lzy  = %d" % lzy)
		print(Query())
		time.sleep(0.5)
		if lzy == 1: 
			print("____________")
		if(lzy == 0):#unlock
			continue
		else:#lock
			rel,path = usblock.usb_main()
			print("********")
			if rel == True:
				l = locker()
				l.unlock_workstation()
				time.sleep(1)
			else:
				time.sleep(1)
				continue
