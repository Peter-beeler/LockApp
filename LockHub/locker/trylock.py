#!/usr/bin/python3
import os
import pyautogui
import time
from ..global_api.loadconfig import load_config

class locker:
    def __init__(self):
        self.config = load_config()
    def lock_workstation(self):
        hotkey = self.config['lock']
        for key in hotkey:
            pyautogui.keyDown(key)
        for key in hotkey:
            pyautogui.keyUp(key)

    def unlock_workstation(self):
        passwd = self.config['unlockPasswd']
        # pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.typewrite(passwd)
        pyautogui.press('enter')
