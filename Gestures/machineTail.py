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