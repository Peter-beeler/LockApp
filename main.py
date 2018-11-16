import sys
import os
import time
import subprocess
sys.path.append('./Encrypt_And_Decrypt')
sys.path.append('./locker')
sys.path.append('./identify')
import identify
from Encrypt import Work_Encrypt
from trylock import locker
import cv2
from config import config
from pynput.keyboard import Listener

def press(key):
	# x = subprocess.check_output(['gnome-screensaver-command','-q'])
	# if("The screensaver is inactive" in str(x)):
	# 	os.system("gnome-screensaver-command -l")
	print("-----------")
	if("Key.esc" in str(key)):
		return False

if __name__ == '__main__':
	flag = 0
	lll_flag = 0
	while True:
		# time.sleep(5)
		# lzy = subprocess.check_output(['gnome-screensaver-command','-q'])
		# print(str(lzy))
		# if("The screensaver is inactive" in str(lzy)):#unlock
		if lll_flag == 0:
			print("+++++++++")
			identify.TakePhoto("unknow.jpg")
			if(identify.numberof("unknow.jpg") <= 0):
				os.system("gnome-screensaver-command -l")
				print(1)
				lll_flag = 1
				continue
			x = identify.COMPARE("owner.jpg", "unknow.jpg")
			if x == 0:
				flag = 0
				time.sleep(1)
				continue
			else:
				# time.sleep(5)
				lll_flag = 1
				os.system("gnome-screensaver-command -l")
				print(2)
		else:#lock
			print("***********")
			# lzy = subprocess.check_output(['gnome-screensaver-command','-q'])
			# print(str(lzy))
			with Listener(on_press = press) as listener:					
				listener.join()
			identify.TakePhoto("unknow.jpg")
			if(identify.numberof("unknow.jpg") <= 0):
				continue
			x = identify.COMPARE("owner.jpg", "unknow.jpg")
			if x == 0:
				lll_flag = 0
				l = locker()
				l.unlock_workstation()
			else:
				flag = flag + 1
				if flag > 5:
					Work_Encrypt("/home/foenix/test")
				continue


