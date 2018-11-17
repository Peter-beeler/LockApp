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

flag = 0
tmp_flag = 0

unlock_interval = 5
lock_threshold = 3

def press(key):
	global flag, tmp_flag
	tmp_flag = tmp_flag + 1
	if("Key.esc" in str(key)):
		tmp_flag = 0
		return False
	if(("Key.enter" in str(key)) and tmp_flag > 10):
		flag = flag + 1
		time.sleep(0.5)
		os.system("gnome-screensaver-command -l")
		return False

def lock_on_face():
    rec_fail_time = 0
    while True:
    	check_status = subprocess.check_output(['gnome-screensaver-command','-q'])
    	# print(str(lzy))
    	if("The screensaver is inactive" in str(check_status)):#unlock
            identify.TakePhoto("unknow.jpg")
            x = identify.COMPARE("owner.jpg", "unknow.jpg")
            if x == 0:
                rec_fail_time = 0
                time.sleep(unlock_interval)
                continue
            else:
                rec_fail_time += 1
            if rec_fail_time == lock_threshold:
                os.system("gnome-screensaver-command -l")
                rec_fail_time = 0
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
    			os.system("gnome-screensaver-command -l")
    			time.sleep(1)
    			flag = flag + 1
    			if flag > 4:
    				Work_Encrypt("/home/foenix/test")
    				Email = email("./mailViaPython/account.txt")
    				Email.sendMail()
    				break
    			continue    