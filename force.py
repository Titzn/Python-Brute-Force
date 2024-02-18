import importlib
import subprocess
import hashlib
import requests
import colorama
from colorama import Fore
import time
import re
import threading
import sys
import requests
import hashlib
import os
import smtplib
import colorama
import tqdm
from datetime import datetime 
import fade 

colorama.init()

def print_separator():
    print(">------------------------------------------------------<")

def check_for_updates():
    url = "https://raw.githubusercontent.com/Titzn/Python-Brute-Force/main/force.py"
    response = requests.get(url)
    
    if response.status_code == 200:
        remote_code = response.text
        
        with open(__file__, 'r', encoding='utf-8', newline='') as file:
            local_code = file.read()
        
        if hashlib.sha256(remote_code.encode()).hexdigest() != hashlib.sha256(local_code.encode()).hexdigest():
            print("Updating the script...")
            with open(__file__, 'w', encoding='utf-8', newline='') as file:
                file.write(remote_code)
            print("Update successful. Please restart the program.")
            time.sleep(1)
            for i in range(3, 0, -1):
                print(i)
                time.sleep(1)
            print("Restarting")
            exit()
        else:
                faded_text2 = fade.greenblue("Script is update !")
                print(faded_text2)
    else:
        print(f"Failed to check for updates. Status Code: {response.status_code}")

def run_script(script_path):
    if os.path.exists(script_path):
        with open(script_path, 'r', encoding='utf-8', newline='') as file:
            script_content = file.read()
        exec(script_content)
    else:
        print(f"Error: Script not found at {script_path}")

def run_selected_script(script_dict, user_choice):
    if user_choice in script_dict:
        run_script(script_dict[user_choice])
    else:
        print("Invalid choice. Please choose a valid number.")

def main():
    check_for_updates()
    # Fading a ascii art text (green-blue)
    faded_text = fade.greenblue("""
                     vprebeta[0.1(stable version)]
 ______  ____  ______   ____  ____       ____   ____  __ __  ______    ___        _____   ___   ____      __    ___ 
|      ||    ||      | /    ||    \     |    \ |    \|  |  ||      |  /  _]      |     | /   \ |    \    /  ]  /  _]
|      | |  | |      ||  o  ||  _  |    |  o  )|  D  )  |  ||      | /  [_ _____ |   __||     ||  D  )  /  /  /  [_ 
|_|  |_| |  | |_|  |_||     ||  |  |    |     ||    /|  |  ||_|  |_||    _]     ||  |_  |  O  ||    /  /  /  |    _]
  |  |   |  |   |  |  |  _  ||  |  |    |  O  ||    \|  :  |  |  |  |   [_|_____||   _] |     ||  .  \\     ||     |
  |  |   |  |   |  |  |  |  ||  |  |    |     ||  .  \     |  |  |  |     |      |  |   |     ||  .  \\     ||     |
  |__|  |____|  |__|  |__|__||__|__|    |_____||__|\_|\__,_|  |__|  |_____|      |__|    \___/ |__|\_| \____||_____|
                                   [+]Github: https://github.com/Titzn/
                                   [+]Discord: titzn
    """)
    print(faded_text)
    time.sleep(0.1)

    script_dict = {
        "1": os.path.join("data", "instagram.py"),
    }

    print_separator()
    print(f"{Fore.BLUE}     [1] Instagram           {Fore.BLUE}[5] ...(Soon)")
    print(f"{Fore.LIGHTCYAN_EX}     [2] ...(Soon)           {Fore.LIGHTCYAN_EX}[6] ...(Soon)")
    print(f"{Fore.CYAN}     [3] ...(Soon)           {Fore.CYAN}[7] ...(Soon)")
    print(f"{Fore.MAGENTA}     [4] ...(Soon)           {Fore.MAGENTA}[8] Options" + Fore.RESET)
    print_separator()

    user_choice = input(Fore.YELLOW + "\nPlease choose a number: " + Fore.RESET)

    if user_choice == "8":
        print("You have chosen Options")
        # Add specific code for the Options here

    else:
        run_selected_script(script_dict, user_choice)

if __name__ == "__main__":
    main()
