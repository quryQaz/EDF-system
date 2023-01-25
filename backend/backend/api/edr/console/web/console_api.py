from __future__ import annotations
from utils.logger import logger
from api.assets.responses import success_response, error_response
from tarantool import Connection
from api.const import const
import socket
from time import sleep
import datetime

async def get_console(request):
    data = request.json
    logger('data')
    logger(data)
    ip = data.get('ip')
    command = data.get('command')
    recv_data = ""
    try:
        logger(f'{ip} {command}')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as SOCKET_CHANNEL:
            SOCKET_CHANNEL.connect((const.get('SOCKET_IP'), const.get('SOCKET_PORT')))
            data = f'{const.get("SECRET")}|{ip}|command|{command}'
            SOCKET_CHANNEL.settimeout(5)
            SOCKET_CHANNEL.send(data.encode("utf-8"))
            recv_data = SOCKET_CHANNEL.recv(1024)
            logger('test123 close')
            SOCKET_CHANNEL.close()
    except socket.timeout:
        logger("No data was recieved from client")
        return error_response(message = "No data was recieved from client")
    except BaseException as e:
        logger(e)
        return error_response(message = str(e))
    recv_data = recv_data.decode('utf-8')
    logger(recv_data)
    data = {
        'command': command,
        'date': datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),
        'output': recv_data
    }
    logger(data)
    return success_response(data = data)
