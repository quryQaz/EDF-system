from __future__ import annotations
from utils.logger import logger
from api.assets.responses import success_response, error_response
from tarantool import Connection
from api.const import const
import socket
from time import sleep
import datetime

async def disconnect(request):
    data = request.json
    logger('data')
    logger(data)
    ip = data.get('ip')
    try:
        logger(f'{ip} disconnect')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as SOCKET_CHANNEL:
            SOCKET_CHANNEL.connect((const.get('SOCKET_IP'), const.get('SOCKET_PORT')))
            data = f'{const.get("SECRET")}|{ip}|disconnect|'
            SOCKET_CHANNEL.send(data.encode("utf-8"))
            SOCKET_CHANNEL.close()
    except BaseException as e:
        logger(e)
        return error_response(message = str(e))
    return success_response(message = "OK")

async def clear(request):
    data = request.json
    logger('data')
    logger(data)
    ip = data.get('ip')
    try:
        connection = Connection("host.docker.internal", 3301)
        drivers = connection.space("drivers")
        processes = connection.space("processes")
        registry = connection.space("registry")
        logs = connection.space("logs")
        errors = connection.space("errors")
        programs = connection.space("programs")
        users = connection.space("users")

        __delete_from_space(drivers, ip)
        __delete_from_space(processes, ip)
        __delete_from_space(registry, ip)
        __delete_from_space(logs, ip)
        __delete_from_space(errors, ip)
        __delete_from_space(programs, ip)
        __delete_from_space(users, ip)

    except BaseException as e:
        logger(e)
        return error_response(message = str(e))
    return success_response(message = "OK")

def __delete_from_space(space, ip):
    result = space.select(ip, index="ip")
    for i in  result:
        space.delete(i[0])
