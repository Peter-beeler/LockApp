import os

class gestureSettings:
	def __init__(self):
		self.num = 0
		self.list = []
	
	def setNumberOfsteps(self, num):
		self.num = num
	
	def readSettings(self, filePath):
		try:
			file = open(filePath, 'r')
		except IOError:
			print("filed to open! (settings.txt)")
			return -1
		else:
			fileContent = file.read().split('\n')
			self.num = int(fileContent.pop(0))
			if self.num > 3 or self.num < 1:
				print("gesture number error!")
				return -1
			if len(fileContent) != self.num:
				print("file format error!")
				return -1
			for item in fileContent:
				self.list.append(item)
			file.close()
		return 0
	
	def writeMachine(self):
		mappingList = ['', '[[0, 1]]', '[[0, 1, 0], [0, 0, 2]]', '[[0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3]]']
		if os.path.exists("machine.py"):
			os.remove("machine.py")
		machine = open("machine.py", 'w+')
		machine.write('import sys\n')
		machine.write('mapping = ' + mappingList[self.num] + '\n')
		machine.write('successState = ' + str(self.num) + '\n')
		try:
			tail = open('machineTail.py', 'r')
		except IOError:
			print("filed to open! (machineTail.py)")
			return -1
		else:
			tailContent = tail.read()
			machine.write(tailContent)
			tail.close()
		machine.close()
		return 0

	def writeConfig(self):
		if os.path.exists("libinput-gestures.conf"):
			os.remove("libinput-gestures.conf")
		config = open("libinput-gestures.conf", 'w+')
		head = open('libinput-gesturesHead.conf', 'r')
		headContent = head.read()
		config.write(headContent)
		head.close()
		for i in range(self.num):
			config.write('gesture ' + self.list[i] + '\tpython3 ~/LockApp/Gestures/machine.py ' + str(i + 1) + '\n')
		config.close()

def stateInit():
	""" initialize state to 0 """
	if os.path.exists("state.txt"):
		state = open('state.txt', 'r+')
		state.seek(0)
		state.write('0')
		state.close()
	else:
		state = open('state.txt', 'w+')
		state.write('0')
		state.close()


def moveConfig():
	""" move config file to right directory """
	# change userName before use
	userName = 'fere'
	# change userName before use
	if os.path.exists("libinput-gestures.conf"):
		os.rename('libinput-gestures.conf', '/home/' + userName + '/.config/libinput-gestures.conf')

# a example of config and machine generation
stateInit()
test = gestureSettings()
test.readSettings('settings.txt')
test.writeMachine()
test.writeConfig()
moveConfig()

# be sure to run 'lininput-gestures-setup start' in this directory,
# or errors will rise.