from pynput.keyboard import Listener

def press(key):
	print(key)

with Listener(on_press = press) as listener:
        listener.join()

