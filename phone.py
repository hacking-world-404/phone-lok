#------------- IMPORT -------------#
from os import system as c
import time

#------------- COLOUR -------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

#------------- LOGO -------------#
def logo():
    c('clear')
    print(f"""{G}
██████╗░░█████╗░███╗░░██╗███████╗░██████╗
██╔══██╗██╔══██╗████╗░██║██╔════╝██╔════╝
██████╔╝███████║██╔██╗██║█████╗░░╚█████╗░
██╔═══╝░██╔══██║██║╚████║██╔══╝░░░╚═══██╗
██║░░░░░██║░░██║██║░╚███║███████╗██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═════╝░
        {P}VIP PHONESPLOIT PRO INSTALLER
""")

#------------- ANIMATION -------------#
def loading(txt):
    logo()
    print(f"{C}{txt}")
    for i in range(1, 11):
        bar = f"{Y}[{G}{'='*i}{A}>{' '*(10-i)}] {i*10}%"
        print(bar, end="\r")
        time.sleep(0.25)
    print(f"\n{G}[✓] DONE!\n")
    time.sleep(1)

#------------- INSTALL PHONESPLOIT -------------#
def install_phonesploit():
    logo()
    print(f"{Y}[+] INSTALLING PHONESPLOIT-PRO...\n")
    time.sleep(1)
    c("pkg update && pkg upgrade -y")
    c("pkg install git python android-tools -y")
    c("git clone https://github.com/FDX100/PhoneSploit-Pro.git")
    c("cd PhoneSploit-Pro && pip install -r requirements.txt")
    loading("INSTALLATION COMPLETE")
    print(f"{G}[✓] INSTALLATION FINISHED!\n")
    print(f"{Y}NOW RUN: {C}cd PhoneSploit-Pro && python3 main.py\n")
    input(f"{A}Press Enter to return to menu...")
    menu()

#------------- ABOUT TOOL -------------#
def about_tool():
    logo()
    print(f"{P} VIP PhoneSploit Installer by HACKING WORLD")
    print(f"{C} Automates installing PhoneSploit-Pro")
    print(f"{Y} GitHub: {G}https://github.com/FDX100/PhoneSploit-Pro\n")
    input(f"{A}Press Enter to return to menu...")
    menu()

#------------- MAIN MENU -------------#
def menu():
    logo()
    print(f"{G}[1] INSTALL PHONESPLOIT-PRO")
    print(f"{G}[2] ABOUT TOOL")
    print(f"{R}[0] EXIT")
    print(f"{G}--------------------------------------------------")
    choice = input(f"{Y}[?] SELECT OPTION: {A}")
    if choice == '1':
        install_phonesploit()
    elif choice == '2':
        about_tool()
    elif choice == '0':
        c('clear')
        print(f"{R}EXITING... STAY VIP HACKER!")
        time.sleep(1)
        exit()
    else:
        print(f"{R}[!] INVALID OPTION, TRY AGAIN")
        time.sleep(1)
        menu()

#------------- START TOOL -------------#
menu()