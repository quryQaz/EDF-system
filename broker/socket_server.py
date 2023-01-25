import sys
import types
import socket
import selectors
from models.status import Status
from utils.process_data import process_data

sel = selectors.DefaultSelector()

host = "0.0.0.0"
port = 8080

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print(f"Listening on {(host, port)}")
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

__added_key = None

def accept_wrapper(sock):                                   # принять подключение
    conn, addr = sock.accept()
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE   # Типы событий. не думаю что запись понядобится,
                                                            # но пусть будет на всякий
    sel.register(conn, events, data=data)
    status = Status(addr[0])
    status.update('active')                                 # при успешном подключении обновить статус

def service_connection(key, mask):                          # обслужить подключение
    global __added_key
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:                                       # если есть данные, записать
            if "SuperSecretKey" in recv_data.decode('utf-8'):
                do_action(recv_data.decode('utf-8'), key)
            process_data(data.addr[0], recv_data, sel, __added_key)
            print(f"Recieve {recv_data}")
        else:                                               # отключение
            print(f"Closing connection to {data.addr}")
            sel.unregister(sock)
            sock.close()
            if __added_key != key:
                status = Status(data.addr[0])
                status.update('inactive')                       # при успешном отключении обновить статус
            if __added_key == key:
                __added_key = None

def do_action(_data, added_key):
    global __added_key
    __added_key = added_key
    data = _data.split('|')
    if data[2] == 'command':
        keys = sel.select(timeout=0)
        for key, mask in events:
            print(key.fileobj)
            print(key.fileobj.getpeername()[1])
            print(added_key.fileobj.getpeername()[1])
            if key.fileobj.getpeername()[0] == data[1] and key.fileobj.getpeername()[1] == 65531:
                print(key.fileobj)
                sock = key.fileobj
                sock.send(data[3].encode('utf-8'))
                break

    elif data[2] == 'disconnect':
        keys = sel.select(timeout=0)
        for key, mask in events:
            if key.fileobj.getpeername()[0] == data[1] and key.fileobj.getpeername()[1] != added_key.fileobj.getpeername()[1]:
                sock = key.fileobj
                sock.close()
                sel.unregister(sock)
                status = Status(key.data.addr[0])
                status.update('inactive')
                break

        # for key, mask in events:
        #     if key.data is None:                            # регистация соединения или обработка данных
        #         accept_wrapper(key.fileobj)
        #     else:
        #         service_connection(key, mask)
        #     i+=1
try:
    while True:
        try:
            events = sel.select(timeout=None)
            i = 0
            for key, mask in events:
                if key.data is None:                            # регистация соединения или обработка данных
                    accept_wrapper(key.fileobj)
                else:
                    try:
                        service_connection(key, mask)
                    except:
                        pass
                i+=1
        except ConnectionResetError:
            sel.unregister(events[i][0].fileobj)
            status = Status(events[i][0].fileobj.getpeername()[0])
            status.update('inactive')
            events[i][0].fileobj.close()
            continue

except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()
