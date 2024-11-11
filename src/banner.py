from colorama import Fore
import time

# Banner and Version Information
def print_banner():
    print(Fore.GREEN + "   _____             _   _  __         ____        _   ")
    print(Fore.GREEN + "  / ____|           | | (_)/ _|       |  _ \\      | |  ")
    print(Fore.GREEN + " | (___  _ __   ___ | |_ _| |_ _   _  | |_) | ___ | |_ ")
    print(Fore.GREEN + "  \\___ \\| '_ \\ / _ \\| __| |  _| | | | |  _ < / _ \\| __|")
    print(Fore.GREEN + "  ____) | |_) | (_) | |_| | | | |_| | | |_) | (_) | |_ ")
    print(Fore.GREEN + " |_____/| .__/ \\___/ \\__|_|_|  \\__, | |____/ \\___/ \\__|")
    print(Fore.GREEN + "        | |                     __/ |                  ")
    print(Fore.GREEN + "        |_|                    |___/                   ")
    time.sleep(0.5)
    print("Version 1.0.1\n" + "-"*65)