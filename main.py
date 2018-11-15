import sys
import os
import time
import subprocess
sys.path.append('./Encrypt_And_Decrypt')
sys.path.append('./locker')
import identify
import Encrypt
import trylock
import cv2
from config import config



if __name__ == '__main__':
	while True:
		time.sleep(5)
		x = subprocess.check_output(['gnome-screensaver-command','-q'])
		if("The screensaver is inactive" in str(x)):#unlock
			Takephoto("unknow.jpg")
			x = COMPARE("owner,jpg""unknow")
			if x == 0:
				continue
			else:
				os.system("gnome-screensaver-command -l")
		else:#lock
			


