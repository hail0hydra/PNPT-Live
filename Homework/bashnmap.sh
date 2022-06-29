#!/usr/bin/bash

# Day 2

echo -e "\033[1;31m--==[[ Bash Port Scanner by Hail_Hydra ]]==--\033[0m" 
echo "" ""

if [[ $1 = ""  ]] || [[ $2 = ""  ]]; then
	echo -e "\033[94mUsage ./bashnmap.sh <ip-address> <port-range> (ie, 65535)"

else
	for port in `seq 1 $2`;do
		echo >/dev/tcp/$1/$port  && echo -e "\033[1;32m$port on $1 open!\033[0m" || : 

	done 2>/dev/null

fi
