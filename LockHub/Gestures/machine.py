import sys
import os
mapping = [[0, 1, 0, 3], [0, 1, 2, 3]]
successState = 2
sys.path.append('../locker')
sys.path.append('../BlueTooth')
from trylock import locker
from dbus_1 import Query
gesCode = int(sys.argv[1])

with open("state.txt", 'r+') as f:
	curState = int(f.read())
	if curState >= successState:
		curState = 0
	newState = mapping[curState][gesCode]
	if(newState == successState):
		if Query() != 0:
			l = locker()
			l.unlock_workstation()
	elif(newState == successState + 1):
		l = locker()
		l.lock_workstation()
	f.seek(0)
	f.write(str(newState))