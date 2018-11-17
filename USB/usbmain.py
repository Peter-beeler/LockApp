import sys
import os
import time
import subprocess
import cv2
sys.path.append('../Encrypt_And_Decrypt')
sys.path.append('../locker')
sys.path.append('../identify')
sys.path.append("../mailViaPython")
sys.path.append("../USB")
sys.path.append("../BlueTooth")
import usblock
from Encrypt import Work_Encrypt
#from trylock import locker
from mail import email
from config import config
from pynput.keyboard import Listener
from dbus_1 import Query

flag = 0
tmp_flag = 0

'''
def press(key):
	global flag, tmp_flag
	tmp_flag = tmp_flag + 1
	if("Key.esc" in str(key)):
		tmp_flag = 0
		return False
	if(("Key.enter" in str(key)) and tmp_flag > 10):
		flag = flag + 1
		time.sleep(0.5)
		l = locker()
		l.lock_workstation()
		return False
rel,path = usblock.usb_main()
print(rel)
'''

'''
if __name__ == '__main__':
	while True:
		# lzy = subprocess.check_output(['gnome-screensaver-command','-q'])
		# print(str(lzy))
		lzy = Query()
		if(lzy == 0):#unlock
			continue
		else:#lock
			with Listener(on_press = press) as listener:					
				listener.join()
			rel,path = usblock.usb_main()

			if x == True:
				l = locker()
				l.unlock_workstation()
				flag = 0
				time.sleep(1)
			else:
				os.system("notify-send 'Wrong!'")
				l = locker()
				l.lock_workstation()
				time.sleep(1)
				flag = flag + 1
				if flag > 4:
					Work_Encrypt("/home/foenix/test")
					Email = email("./mailViaPython/account.txt")
					Email.sendMail()
					break
				continue
'''