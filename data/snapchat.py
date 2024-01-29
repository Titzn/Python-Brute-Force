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
try:
    from colorama import Fore
    import ctypes, pyautogui, keyboard, os, time, platform
    from datetime import datetime
except ImportError:
    input("Error while importing modules. Please install the modules in requirements.txt")

class SnapchatBot:
    def __init__(self):
        self.sent_snaps = 0
        self.delay = 1.3

    def on_linux(self):
        return platform.system() == "Linux"

    def get_positions(self):
        positions = [
            "camera button",
            "take picture button",
            "arrow down button",
            "Multi Snap button",
            "Edit & Send button",
            "Send To button",
            "shortcut",
            "select all in shortcut",
            "send snap button"
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
        pyautogui.moveTo(self.camera_button)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.take_picture)
        for _ in range(7):
            pyautogui.click()
            time.sleep(self.delay)

        # Edit and send the snaps
        pyautogui.moveTo(self.edit_send)
        time.sleep(self.delay)
        pyautogui.click()
        pyautogui.moveTo(self.send_to)
        pyautogui.click()
        time.sleep(self.delay)

        # Select recipients and send snaps
        pyautogui.moveTo(self.shortcut)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.select_all)
        pyautogui.click()
        pyautogui.moveTo(self.send_snap_button)
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
