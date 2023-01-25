from __future__ import annotations
from utils.logger import logger
from api.assets.responses import success_response, error_response
from tarantool import Connection

async def get_drivers(request):
    data = request.json
    logger('data')
    logger(data)
    ip = data.get('ip')
    try:
        connection = Connection("host.docker.internal", 3301)
        processes = connection.space("drivers")
        result = processes.select(ip, index="ip")
        data = build_response(result)
        connection.close()
    except BaseException as e:
        logger(e)
        return error_response(message = str(e))

    logger(data)
    return success_response(data = data)


def build_response(response):
    data = []
    for _data in response:
        data.append({
            'ip': _data[1],
            'data': _data[2],
            'date': _data[3]
        })
    return data
