#!/bin/bash

function ctrl_c(){
  echo -e "\n\n[!] Saliendo...\n"
  tput cnorm; exit 1
}
tput cnorm; 
function checkPort(){

  (exec 3<> /dev/tcp/$1/$2) 2>/dev/null

  if [ $? -eq 0 ]; then
    echo -e "[+] Host $1 - Port $2 (ABIERTO)"
  fi

  exec 3<&-
  exec 3>&-
}

# Ctrl+C 
trap ctrl_c SIGINT

declare -a ports=( $(seq 1 65535)  )

tput civis

  if [ $1 ]; then 
    for port in ${ports[@]}; do
      checkPort $1 $port &
    done

  else
    echo -e "\n[!] Uso: $0 <ip-adress>\n"
  fi  

wait
tput cnorm
