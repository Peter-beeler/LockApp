import sys
import os
import time
import subprocess
import cv2
sys.path.append('./Encrypt_And_Decrypt')
sys.path.append('./locker')
sys.path.append('./identify')
sys.path.append("./mailViaPython")
import identify
from Encrypt import Work_Encrypt
from trylock import locker
from mail import email
from config import config
from pynput.keyboard import Listener

def press(key):
	x = subprocess.check_output(['gnome-screensaver-command','-q'])
	if("The screensaver is inactive" in str(x)):
		os.system("gnome-screensaver-command -l")
	# print("-----------")
	if("Key.esc" in str(key)):
		return False

if __name__ == '__main__':
	flag = 0
	lll_flag = 0
	while True:
		lzy = subprocess.check_output(['gnome-screensaver-command','-q'])
		print(str(lzy))
		if("The screensaver is inactive" in str(lzy)):#unlock
			# print("+++++++++")
			identify.TakePhoto("unknow.jpg")
			x = identify.COMPARE("owner.jpg", "unknow.jpg")
			if x == 0:
				flag = 0
				time.sleep(1)
				continue
			else:
				lll_flag = 1
				os.system("gnome-screensaver-command -l")
				# print(2)
		else:#lock
			# print("***********")
			with Listener(on_press = press) as listener:					
				listener.join()
			identify.TakePhoto("unknow.jpg")
			x = identify.COMPARE("owner.jpg", "unknow.jpg")
			if x == 0:
				lll_flag = 0
				l = locker()
				l.unlock_workstation()
				time.sleep(1)
			else:
				os.system("notify-send 'Wrong!'")
				os.system("gnome-screensaver-command -l")
				time.sleep(1)
				flag = flag + 1
				if flag > 5:
					Work_Encrypt("/home/foenix/test")
					Email = email("./mailViaPython/account.txt")
					Email.sendMail()
					break
				continue


