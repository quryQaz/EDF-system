from __future__ import annotations
from utils.logger import logger
from api.assets.responses import success_response, error_response
from tarantool import Connection

async def get_statuses(request):
    try:
        connection = Connection("host.docker.internal", 3301)
        result = connection.select("status")
        logger('result')
        logger(result)
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
            'status': _data[2]
        })
    return data
