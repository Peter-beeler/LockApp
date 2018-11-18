# 要改的东西：
# 1. 加密目录的获取方式
# 2. 加密的逻辑规则
import sys
import os
import time
import subprocess
import cv2
sys.path.append('./Encrypt_And_Decrypt')
sys.path.append('./locker')
sys.path.append('./identify')
sys.path.append("./mailViaPython")
sys.path.append('./BlueTooth')
from .identify import identify
from .Encrypt_And_Decrypt.Encrypt import Work_Encrypt
from .locker.trylock import locker
from.mailViaPython.mail import email
from .locker.config import config
from .BlueTooth.dbus_1 import Query
from pynput.keyboard import Listener
from .global_api.loadconfig import load_config

flag = 0
tmp_flag = 0


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

def Face():
	fail_time = 0
	flag = 0
	while True:
		# lzy = subprocess.check_output(['gnome-screensaver-command','-q'])
		# print(str(lzy))
		status = Query()
		if(status == 0):#unlock
			identify.TakePhoto("unknow.jpg")
			x = identify.COMPARE("owner.jpg", "unknow.jpg")
			if x == 0:
				time.sleep(2)
				fail_time = 0
				continue
			else:
				fail_time += 1
				print(fail_time)
				if(fail_time == 5):
					l = locker()
					l.lock_workstation()
					fail_time = 0
		else:#lock
			with Listener(on_press = press) as listener:					
				listener.join()
			identify.TakePhoto("unknow.jpg")
			x = identify.COMPARE("owner.jpg", "unknow.jpg")
			if x == 0:
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
					Email = email("./LockHub/mailViaPython/account.txt")
					Email.sendMail()
					flag = 0
					break
				continue
