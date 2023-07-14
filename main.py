#!/usr/bin/env python3

import sys
import os

import zeus_lib.network as networking
import zeus_lib.framework as framework
import zeus_lib.commands as commands
from colorama import Fore, Back, Style

banner = f"""
{Fore.MAGENTA}
 ZZZZZZZZZZZZZZZZZZZEEEEEEEEEEEEEEEEEEEEEEUUUUUUUU     UUUUUUUU   SSSSSSSSSSSSSSS 
 Z:::::::::::::::::ZE::::::::::::::::::::EU::::::U     U::::::U SS:::::::::::::::S
 Z:::::::::::::::::ZE::::::::::::::::::::EU::::::U     U::::::US:::::SSSSSS::::::S
 Z:::ZZZZZZZZ:::::Z EE::::::EEEEEEEEE::::EUU:::::U     U:::::UUS:::::S     SSSSSSS
 ZZZZZ     Z:::::Z    E:::::E       EEEEEE U:::::U     U:::::U S:::::S            
         Z:::::Z      E:::::E              U:::::D     D:::::U S:::::S            
        Z:::::Z       E::::::EEEEEEEEEE    U:::::D     D:::::U  S::::SSSS         
       Z:::::Z        E:::::::::::::::E    U:::::D     D:::::U   SS::::::SSSSS    
      Z:::::Z         E:::::::::::::::E    U:::::D     D:::::U     SSS::::::::SS  
     Z:::::Z          E::::::EEEEEEEEEE    U:::::D     D:::::U        SSSSSS::::S 
    Z:::::Z           E:::::E              U:::::D     D:::::U             S:::::S
 ZZZ:::::Z     ZZZZZ  E:::::E       EEEEEE U::::::U   U::::::U             S:::::S
 Z::::::ZZZZZZZZ:::ZEE::::::EEEEEEEE:::::E U:::::::UUU:::::::U SSSSSSS     S:::::S
 Z:::::::::::::::::ZE::::::::::::::::::::E  UU:::::::::::::UU  S::::::SSSSSS:::::S
 Z:::::::::::::::::ZE::::::::::::::::::::E    UU:::::::::UU    S:::::::::::::::SS 
 ZZZZZZZZZZZZZZZZZZZEEEEEEEEEEEEEEEEEEEEEE      UUUUUUUUU       SSSSSSSSSSSSSSS{Fore.RESET}

 {Fore.RED}DISCLAIMER: This tool is for educational purposes only!
 Otherwise I will not assume any liability.{Fore.RESET}

 [#] Author: Russian.Hzcker
 [#] Creation: 14-07-2023
 [#] Github: https://github.com/Br0k3r6/
"""

if __name__ == '__main__':
    print(banner)
    try:
        uid = os.getuid()
    except Exception:
        try:
            uid = os.geteuid()
        except Exception:
            print(" [-] Currupt python library 'os'. Are you on linux?")
            exit()
    if uid != 0:
        print(" [!] Please try running ZEUS with sudo permission.")
        exit()
    framework.start_framework_shell(networking, commands, sys.argv)