import os
import sys
from . import configGenerator

def gesturesGo():
# here the path may need to be changed according to the path where this file is called
    os.chdir('LockHub/Gestures')
    configGenerator.init()
    os.system('libinput-gestures-setup start')

def gesturesStop():
# here the path may need to be changed according to the path where this file is called
    os.system('libinput-gestures-setup stop')
    os.chdir('..')