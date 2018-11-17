from time import sleep
import os,shutil

usbpath = "/Volumes"
content = ['Macintosh HD', 'Untitled']
def fun(x):
	try:
		x = usbpath + "/" + x + "/code/code.txt"
		f = open(x)
		code = f.readline()
		print(code)	
	except:
		print("NO file")
while(1):
	new_content = os.listdir(usbpath)
	print(new_content)
	for x in new_content:
		if(not(x in content)):
			fun(x)
			break
	sleep(3)