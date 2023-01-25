import winapps
import socket
import time

RPORT = 8080
RHOST = "127.0.0.1"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as SOCKET_CHANNEL:
    SOCKET_CHANNEL.connect((RHOST, RPORT))
    while True:
        recv_data = SOCKET_CHANNEL.recv(1024)
        if recv_data:
            data = recv_data.decode('utf-8')
            if data == "ls":
                print("sended")
                SOCKET_CHANNEL.send("$$$Console$$$ ls test files".encode('utf-8'))
            print(recv_data)
