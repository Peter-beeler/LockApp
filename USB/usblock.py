from time import sleep
import os,shutil
import pyotp
import sys
sys.path.append('../Encrypt_And_Decrypt')
from Encrypt import	Encrypt
from Decrypt import	Decrypt
from Decrypt import Work_Decrypt
import random
usbpath = "/Volumes"
content = ['Macintosh HD', 'Untitled']

def readcode(x):
	x = usbpath + "/" + x + "/code/code.txt"
	Decrypt(x)
	f = open(x)
	code = f.readline()
	f.close()
	return code

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

def newpasswd(key,usbfile,localfile):
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

def usb_main():
	while(1):
		new_content = os.listdir(usbpath)
		if(new_content == content):
			continue
		else:
			break
	for x in new_content:
		if(not(x in content)):
			break

	code = readcode(x)
	#print(x)
	#print(code)
	rel,key = verification(code)
	#print(rel)
	newpasswd(key,usbpath + "/" + x + "/code/code.txt","key.txt")
	return rel

def unlock(path):
	while(1):
		new_content = os.listdir(usbpath)
		if(new_content == content):
			continue
		else:
			break
	for x in new_content:
		if(not(x in content)):
			break
	x = usbpath + "/" + x + "/code/my_private_rsa_key.bin"
	datakey =open(x).read()
	Work_Decrypt(path,datakey)