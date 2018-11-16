
gesCode = int(sys.argv[1])

# gesCode = 
# 0: other gesture
# 1: 1st gesture
# 2: 2nd gesture
# 3: 3rd gesture

with open("state.txt", 'r+') as f:
	curState = int(f.read())
	newState = mapping[curState][gesCode]
	if(newState == successState):
		# replace here with what you want to
		with open("congras.txt", 'w+'):
			pass
		# but do not delete the following line!
		newState = 0
	f.seek(0)
	f.write(str(newState))