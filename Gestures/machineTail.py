
gesCode = int(sys.argv[1])

sys.path.append('../locker')
from trylock import locker

# gesCode = 
# 0: other gesture
# 1: 1st gesture
# 2: 2nd gesture
# 3: 3rd gesture

with open("state.txt", 'r+') as f:
	curState = int(f.read())
	if curState >= successState:
		curState = 0
	newState = mapping[curState][gesCode]
	if(newState == successState):
		# replace here with what you want to
		l = locker()
		l.unlock_workstation()
		
		# but do not delete the following line!
	elif(newState == successState + 1):
		l = locker()
		l.lock_workstation()
	f.seek(0)
	f.write(str(newState))