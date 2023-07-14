import os
import sys
import re

from colorama import Fore, Back, Style
from simple_term_menu import TerminalMenu

helpmenu = """
 +-COMMAND-+-HELP-------------------------------------+
 | exit    | Exits the ZEUS DoS tool.                 |
 | help    | Shows this message.                      |
 | dosmenu | Starts the DoS menu.                     |
 +---------+------------------------------------------+
"""

def show_menu(options:list):
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    return options[menu_entry_index]

def check_cmd(cmd, cmd_l, networking):
    if cmd_l == "h" or cmd_l == "help":
        print(helpmenu)
    if cmd_l == "dosmenu":
        print()
        res_1 = show_menu(["TCP (not working now)", "UDP", "HTTP (not working now)", "Quit"])
        if res_1 == "Quit":
            return
        if res_1.startswith("TCP"):
            print(" [-] TCP is not working for now. (coming soon)") # TODO
            return
        if res_1.startswith("UDP"):
            target = input(" [*] Please input the target IP address: ")
            port = input(" [*] Please input the target port: ")
            threads = input(" [*] Please enter an amount of threads: ")
            print(" [*] Checking all options you just entered...")
            errors = False
            try:
                port = int(port)
            except:
                errors = True
                print(" [!] Port must be int.")
            try:
                threads = int(threads)
            except:
                errors = True
                print(" [!] Threads must be int.")
            if errors:
                return
            else:
                networking.UDP_based_attack(target, int(port), int(threads))

        if res_1.startswith("HTTP"):
            print(" [-] HTTP is not working for now. (coming soon)") # TODO
