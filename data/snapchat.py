import importlib

# List of required modules
required_modules = ['ctypes', 'pyautogui', 'keyboard', 'os', 'time', 'platform', 'datetime', 'colorama']

# Iterate over the required modules
for module in required_modules:
    try:
        # Try to import the module
        importlib.import_module(module)
    except ImportError:
        # If the module is not installed, install it
        print(f"Module '{module}' not found. Installing...")
        os.system(f"pip install {module}")

# Now you can safely import the modules
import ctypes
import pyautogui
import keyboard
import os
import time
import platform
from datetime import datetime
from colorama import Fore


class SnapchatBot:
    CAMERA_BUTTON = "camera button"
    TAKE_PICTURE_BUTTON = "take picture button"
    ARROW_DOWN_BUTTON = "arrow down button"
    MULTI_SNAP_BUTTON = "Multi Snap button"
    EDIT_SEND_BUTTON = "Edit & Send button"
    SEND_TO_BUTTON = "Send To button"
    SHORTCUT_BUTTON = "shortcut"
    SELECT_ALL_IN_SHORTCUT_BUTTON = "select all in shortcut"
    SEND_SNAP_BUTTON = "send snap button"

    def __init__(self):
        self.sent_snaps = 0
        self.delay = 1.3
        self.started_time = None

    def on_linux(self):
        return platform.system() == "Linux"

    def get_positions(self):
        positions = [
            self.CAMERA_BUTTON,
            self.TAKE_PICTURE_BUTTON,
            self.ARROW_DOWN_BUTTON,
            self.MULTI_SNAP_BUTTON,
            self.EDIT_SEND_BUTTON,
            self.SEND_TO_BUTTON,
            self.SHORTCUT_BUTTON,
            self.SELECT_ALL_IN_SHORTCUT_BUTTON,
            self.SEND_SNAP_BUTTON
        ]

        for pos in positions:
            self.print_console(f"Move your mouse to the {pos}, then press F")
            while True:
                if keyboard.is_pressed("f"):
                    setattr(self, pos.lower().replace(" ", "_"), pyautogui.position())
                    break
            time.sleep(0.5)

    def send_snap(self, shortcut_users):
        self.update_title(shortcut_users)

        # Switch to camera and take 7 pictures
        pyautogui.moveTo(getattr(self, self.CAMERA_BUTTON))
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(getattr(self, self.TAKE_PICTURE_BUTTON))
        for _ in range(7):
            pyautogui.click()
            time.sleep(self.delay)

        # Edit and send the snaps
        pyautogui.moveTo(getattr(self, self.EDIT_SEND_BUTTON))
        time.sleep(self.delay)
        pyautogui.click()
        pyautogui.moveTo(getattr(self, self.SEND_TO_BUTTON))
        pyautogui.click()
        time.sleep(self.delay)

        # Select recipients and send snaps
        pyautogui.moveTo(getattr(self, self.SHORTCUT_BUTTON))
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(getattr(self, self.SELECT_ALL_IN_SHORTCUT_BUTTON))
        pyautogui.click()
        pyautogui.moveTo(getattr(self, self.SEND_SNAP_BUTTON))
        pyautogui.click()

        self.sent_snaps += 7
        self.update_title(shortcut_users)

    def update_title(self, shortcut_users):
        now = time.time()
        elapsed = str(now - self.started_time).split(".")[0]
        sent_snaps = self.sent_snaps * shortcut_users
        if not self.on_linux():
            ctypes.windll.kernel32.SetConsoleTitleW(
                f"Snapchat Score Botter | Sent Snaps: {sent_snaps} | Elapsed: {elapsed}s | Developed by @Titzn on Github"
            )

    def print_console(self, arg, status="Console"):
        print(f"\n       {Fore.WHITE}[{Fore.RED}{status}{Fore.WHITE}] {arg}")

    def main(self):
        if not self.on_linux():
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("Snapchat Score Botter | Developed by @Titzn on Github")
        else:
            os.system("clear")

        ascii_text = """
   _____                        _           _      __                    __    _                _       
  / ____|                      | |         | |    / /                    \ \  | |              | |      
 | (___  _ __   __ _ _ __   ___| |__   __ _| |_  | |___  ___ ___  _ __ ___| | | |__  _ __ _   _| |_ ___ 
  \___ \| '_ \ / _` | '_ \ / __| '_ \ / _` | __| | / __|/ __/ _ \| '__/ _ \ | | '_ \| '__| | | | __/ _ /
  ____) | | | | (_| | |_) | (__| | | | (_| | |_  | \__ \ (_| (_) | | |  __/ | | |_) | |  | |_| | ||  __/
 |_____/|_| |_|\__,_| .__/ \___|_| |_|\__,_|\__| | |___/\___\___/|_|  \___| | |_.__/|_|   \__,_|\__\___|
                    | |                           \_\                    /_/                            
                    |_|                                                                                 
"""

        print(Fore.RED + ascii_text)

        self.get_positions()

        while True:
            try:
                shortcut_users = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] How many people are in this shortcut: "))
                break
            except ValueError:
                print(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] There was an error with that input, please try again :) ")

        self.print_console("Slow PC", "1")
        self.print_console("Fast PC", "2")
        options = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Option: "))
        if options == 1:
            self.delay = 2

        self.print_console("Go to your chats, then press F when you're ready.")

        while True:
            try:
                if keyboard.is_pressed("f"):
                    break
            except KeyboardInterrupt:
                self.print_console("Script terminated by user.")
                return

        if not self.on_linux():
            os.system("cls")
        else:
            os.system("clear")

        print(Fore.RED + ascii_text)
        self.print_console("Sending snaps...")

        self.started_time = time.time()
        while True:
            try:
                if keyboard.is_pressed("F4"):
                    break
                self.send_snap(shortcut_users)
                time.sleep(4)
            except KeyboardInterrupt:
                self.print_console("Script terminated by user.")
                break

        self.print_console(f"Finished sending {self.sent_snaps} snaps.")

# Instantiate and run the SnapchatBot
obj = SnapchatBot()
obj.main()
