#!/usr/bin/python

import socket as sock
# import pyfiglet
import os
import sys

os.system("echo -e '\033[1;31m--==[[ Python Port Scanner by Hail_Hydra ]]==--\033[0m\n\n'")
# banner = pyfiglet.figlet_format('Python\nPort Scanner')
# print(banner)

def main():

    ports = int(sys.argv[2])
    ip = sys.argv[1]

    for i  in range(1,ports+1):
        try:
            s = sock.socket(sock.AF_INET,sock.SOCK_STREAM)
            s.connect((ip,i))
            # print(f"Found Open Port : {i}")
            os.system(f"echo -e  '\e[92m Found Open Port : {i} \e[0m'")
            s.shutdown()
        except:
            # print(f"Not Open {i}")
            pass

if __name__ == "__main__":
    try:
        main()
    except IndexError:
        os.system("echo -e '\033[36msomething is missing!\nUsage : ./pynmap <ip-address-here> <port-range-here> (i.e, 65536)\033[0m'")
    except:
        print("Not in the mood today :(")
