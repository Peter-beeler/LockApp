#!/usr/bin/python3
import os
import pyautogui
import time
from config import config

class locker:
    
    def lock_workstation(self):
        hotkey = config['lock']
        for key in hotkey:
            pyautogui.keyDown(key)
        for key in hotkey:
            pyautogui.keyUp(key)

    def unlock_workstation(self):
        passwd = config['unlockPasswd']
        # pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite(passwd)
        pyautogui.press('enter')

def main():
    m = locker()
    m.lock_workstation()
    m.unlock_workstation()

if __name__ == "__main__":
    main()