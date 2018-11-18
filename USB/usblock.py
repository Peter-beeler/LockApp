from time import sleep
import os,shutil,time
import subprocess
import pyotp
import sys
sys.path.append('../Encrypt_And_Decrypt')
from Encrypt import	Encrypt
from Decrypt import	Decrypt
from Decrypt import Work_Decrypt
import random
usbpath = "/media/foenix"
content = ['Ubuntu 18.0']

def readcode(x):
	codepath = usbpath + "/" + x + "/code/code.txt"
	keypath = usbpath + "/" + x + "/code/my_private_rsa_key.bin"
	data = open(keypath).read()
	Decrypt(codepath,data)
	f = open(codepath)
	code = f.readline()
	f.close()
	return code,data

def verification(code):
	file = open("key.txt")
	key = file.readline()
	key = key[:len(key)-1]
	#print(key)
	counter = file.readline()
	counter = int(counter)
	hotp = pyotp.HOTP(key)
	#print(type(code))
	rel = hotp.verify(code,counter)
	file.close()
	return rel,key

def newpasswd(key,usbfile,localfile,keydata):
	rad = random.random()
	rad = int(1000*rad)
	rad = rad % 10
	hopt = pyotp.HOTP(key)
	f = open(usbfile,"w")
	f.truncate()
	f.seek(0)
	f.write(str(hopt.at(rad)))
	f.close()

	f = open(localfile,"w")
	f.truncate()
	f.seek(0)
	key = key + '\n'
	f.write(key)
	f.write(str(rad))
	f.close()
	Encrypt(usbfile)
	return 0

# def usb_main():
if __name__ == "__main__":
	# print("-----------")
	os.chdir('/proc/scsi')
	while True:
		time.sleep(1)
		tmp = subprocess.check_output(['ls'])
		lzy = str(tmp)
		if('usb-storage' in lzy):
			break
		else:
			continue
	time.sleep(1)
	os.chdir('usb-storage')
	# os.system('ls')
	time.sleep(1)
	tmp = subprocess.check_output(['ls'])
	# print(tmp)
	l = str(tmp)[2:3]
	# print('l = %s' % l)
	time.sleep(1)
	if l=='1':
		os.system("mount -t vfat /dev/sda4 /media/foenix/tmp")
	elif l=='2':
		os.system("mount -t vfat /dev/sdb4 /media/foenix/tmp")
	else:
		os.system("mount -t vfat /dev/sdc4 /media/foenix/tmp")

	time.sleep(3)
	# print(x)
	x = 'tmp'
	# os.chdir(x)
	# os.system("ls")
	code,data = readcode(x)
	os.chdir("/home/foenix/LockApp/USB")
	rel,key = verification(code)
	print(rel, end = ' ')
	newpasswd(key,usbpath + "/" + x + "/code/code.txt","key.txt",data)
	# return rel,usbpath + '/' + x
	# print(rel)
	print(usbpath + '/' + x)

def unlock(filepath,codepath):
	x = codepath + "/code/my_private_rsa_key.bin"
	datakey =open(x).read()
	Work_Decrypt(filepath,datakey)
	
