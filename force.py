# Add this import statement at the beginning of your force.py script
import re
import threading
import sys
import requests
import hashlib
import os
import smtplib
import colorama
from colorama import Fore
import time
from tqdm import tqdm
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
            print(Fore.GREEN + "The script is up to date.")
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

    print(Fore.GREEN + """

                     vprebeta[0.1]
 ______  ____  ______   ____  ____       ____   ____  __ __  ______    ___        _____   ___   ____      __    ___ 
|      ||    ||      | /    ||    \     |    \ |    \|  |  ||      |  /  _]      |     | /   \ |    \    /  ]  /  _]
|      | |  | |      ||  o  ||  _  |    |  o  )|  D  )  |  ||      | /  [_ _____ |   __||     ||  D  )  /  /  /  [_ 
|_|  |_| |  | |_|  |_||     ||  |  |    |     ||    /|  |  ||_|  |_||    _]     ||  |_  |  O  ||    /  /  /  |    _]
  |  |   |  |   |  |  |  _  ||  |  |    |  O  ||    \|  :  |  |  |  |   [_|_____||   _] |     ||    \ /   \_ |   [_ 
  |  |   |  |   |  |  |  |  ||  |  |    |     ||  .  \     |  |  |  |     |      |  |   |     ||  .  \\     ||     |
  |__|  |____|  |__|  |__|__||__|__|    |_____||__|\_|\__,_|  |__|  |_____|      |__|    \___/ |__|\_| \____||_____|
                                   [+]Github: https://github.com/Titzn/                                                                                  
                                                                                                          
    """ + Fore.RESET)

    frames = ["▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
    for _ in tqdm(range(5), desc=Fore.RED + "Loading modules...", ascii=False, ncols=75):
        time.sleep(0.1)

    script_dict = {
        "1": os.path.join("data", "instagram.py"),
        "2": os.path.join("data", "tiktok.py"),
        "3": os.path.join("data", "snapchat.py"),
        "4": os.path.join("data", "leboncoin.py"),
        "5": os.path.join("data", "ebay.py"),
        "6": os.path.join("data", "vinted.py"),
        "7": os.path.join("data", "gmail.py"),
    }

    print_separator()
    print(f"{Fore.BLUE}     [1] Instagram               {Fore.BLUE}[5] Ebay(Soon)")
    print(f"{Fore.LIGHTCYAN_EX}     [2] Tiktok(Soon)            {Fore.LIGHTCYAN_EX}[6] Vinted(Soon)")
    print(f"{Fore.CYAN}     [3] Snapchat(Soon)          {Fore.CYAN}[7] Gmail(Soon)")
    print(f"{Fore.MAGENTA}     [4] Leboncoin(Soon)         {Fore.MAGENTA}[8] Options" + Fore.RESET)
    print_separator()

    user_choice = input(Fore.YELLOW + "\nPlease choose a number: " + Fore.RESET)

    if user_choice == "8":
        print("You have chosen Options")
        # Add specific code for the Options here

    else:
        run_selected_script(script_dict, user_choice)

if __name__ == "__main__":
    main()
