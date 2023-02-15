import time
import os
import requests
from colorama import Fore,Style
import logging
import socket
import platform
import speedtest
import subprocess
import string
import random
import json
import re
from requests import get

os.system("clear")
print(f'''…………..$……………………………………..$…………..
…………$$……………………………………..$$…………
…………$$……………………………………..$$…………
…………..$$s………………………………s$$…………..
…………….$$$$……………………….$$$$…………….
………………³$$$$..¶¶¶¶¶¶¶¶..$$$$³………………
………………..³$$$$..¶¶¶¶¶¶..$$$$³………………..
………………¶..$$$$$..¶¶¶¶..$$$$$..¶………………
…………….¶¶¶..$$$..¶¶¶¶¶¶..$$$..¶¶………………
…………….¶¶¶….¶¶¶¶¶¶¶¶¶¶….¶¶¶¶………………
…………….¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………
………………..¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………..
………………..¶¶……..¶¶¶¶……….¶……………………
………………..¶¶……..¶¶¶¶……….¶¶………………….
………………..¶¶¶¶¶¶¶¶..¶¶¶¶¶¶¶¶………………….
………………….¶¶¶¶¶¶……¶¶¶¶¶¶¶………………….
……………………….¶¶¶¶¶¶¶¶¶…………………………
……………………….¶..¶..¶..¶..¶…………………………
…………¶…………..¶…………..¶…………..¶…………..
……….¶¶……………………………………….¶¶…………
……….¶¶……………………………………….¶¶…………
……….¶¶…………..¶¶……….¶¶…………..¶¶…………
……….¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶…………
……¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶……..
….¶¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶¶……
……¶¶¶¶..¶¶..¶¶………………….¶¶..¶¶..¶¶¶¶……..
{Fore.RED}█▄░█ █▀▀ ▀█▀ █▀█ █░█ ▄▀█ █▄░█ ▀█▀ █▀█ █▀▄▀█
{Fore.WHITE}█░▀█ ██▄ ░█░ █▀▀ █▀█ █▀█ █░▀█ ░█░ █▄█ █░▀░█
  {Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  {Fore.RED}Developer{Fore.BLUE}: {Fore.WHITE}RetroPackets
  {Fore.RED}Instagram{Fore.BLUE}: {Fore.WHITE}retropacketz
  {Fore.RED}Github{Fore.BLUE}: {Fore.WHITE}https://github.com/RetroPackets
  {Fore.RED}Organization{Fore.BLUE}: {Fore.WHITE}THC {Fore.BLUE}- {Fore.WHITE}FHS
  {Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{Fore.WHITE}
''')


def get_random_mac_address():
    uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(uppercased_hexdigits)
        mac += ":"
    return mac.strip(":")


def get_current_mac_address(iface):
    output = subprocess.check_output(f"ifconfig {iface}", shell=True).decode()
    return re.search("ether (.+) ", output).group().split()[1].strip()
    


def change_mac_address(iface, new_mac_address):
    subprocess.check_output(f"ifconfig {iface} down", shell=True)
    subprocess.check_output(f"ifconfig {iface} hw ether {new_mac_address}", shell=True)
    subprocess.check_output(f"ifconfig {iface} up", shell=True)
    

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Mac Changer")
    parser.add_argument("interface", help="The network interface name on Linux")
    parser.add_argument("-r", "--random", action="store_true", help="Whether to generate a random MAC address")
    #parser.add_argument("Wlan0/eth0", help="Input = sudo python3 netpantom.py -r wlan0")
    args = parser.parse_args()
    iface = args.interface
    if args.random:
        new_mac_address = get_random_mac_address()
    elif args.mac:
        new_mac_address = args.mac
    # get the current MAC address
    old_mac_address = get_current_mac_address(iface)
    print(f"{Fore.RED}[{Fore.YELLOW}✗{Fore.RED}] {Fore.WHITE}Old MAC address{Fore.BLUE}:{Fore.WHITE}", old_mac_address)
    # change the MAC address
    change_mac_address(iface, new_mac_address)
    # check if it's really changed
    new_mac_address = get_current_mac_address(iface)
    print(f"{Fore.RED}[{Fore.GREEN}✢{Fore.RED}] {Fore.WHITE}New MAC address{Fore.BLUE}:{Fore.WHITE}", new_mac_address)



hostname = socket.gethostname() 
my_system = platform.uname()  
IPAddr = socket.gethostbyname(hostname)

os.system("service tor start")
os.system("anonsurf start >/dev/null 2>&1")


time.sleep(5)
os.system("anonsurf change ip >/dev/null 2>&1")
se = int(input(f"{Fore.MAGENTA}How many seconds between IP changes{Fore.YELLOW}?{Fore.BLUE}:{Fore.RED} "))
m = int(input(f"{Fore.MAGENTA}How many times should your IP change{Fore.YELLOW}?{Fore.BLUE}:{Fore.RED} "))

for i in range(m):
    time.sleep(se)
    externalIP  = os.popen('curl -s ifconfig.me').readline()
    os.system("service tor reload")
    os.system("anonsurf change ip >/dev/null 2>&1")
    time.sleep(3)
    print(f"""{Fore.RED}[{Fore.GREEN}✔{Fore.RED}] {Fore.WHITE}Your IP has been Changed {Fore.BLUE}:{Fore.GREEN} {externalIP}""")











