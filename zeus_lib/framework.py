import os
import sys

def start_framework_shell(networking, commands, args):
    print(" [*] Initializing classes.")
    network = networking.Network()
    print(" [+] All objects Initialized!")
    print()
    while True:
        cmd = input(" ZEUS[~] ➤ ")
        cmd_l = cmd.lower()
        if cmd_l == "exit" or cmd_l == "quit" or cmd_l == "e" or cmd_l == "q":
            exit()
        commands.check_cmd(cmd, cmd_l, network)