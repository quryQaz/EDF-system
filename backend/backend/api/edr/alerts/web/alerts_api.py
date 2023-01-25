from __future__ import annotations
from utils.logger import logger
from api.assets.responses import success_response, error_response
from tarantool import Connection

import psycopg2

async def get_alerts(request):

    ip_list = []
    alerts = []
    try:
        conn = psycopg2.connect(dbname='lms', user='admin',
                                password='postgres', host='postgres-db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ti LIMIT 10')
        records = cursor.fetchall()
        cursor.close()
        conn.close()

        for res in records:
            ip_list.append(res[1])

        logger(ip_list)
        
        connection = Connection("host.docker.internal", 3301)
        drivers = connection.select("drivers")
        processes = connection.select("processes")
        registry = connection.select("registry")
        logs = connection.select("logs")
        errors = connection.select("errors")
        programs = connection.select("programs")

        _alerts = __check_space(drivers, ip_list)
        if _alerts:
            alerts += (_alerts)

        _alerts = __check_space(processes, ip_list)
        if _alerts:
            alerts += (_alerts)

        _alerts = __check_space(registry, ip_list)
        if _alerts:
            alerts += (_alerts)

        _alerts = __check_space(logs, ip_list)
        if _alerts:
            alerts += (_alerts)

        _alerts = __check_space(errors, ip_list)
        if _alerts:
            alerts += (_alerts)

        _alerts = __check_space(programs, ip_list)
        if _alerts:
            alerts += (_alerts)

        data = build_response(alerts)
        connection.close()
    except BaseException as e:
        logger(e)
        return error_response(message = str(e))

    logger(data)
    return success_response(data = data)

def __check_space(space, ip_list):
    alerts = []
    for i in space:
        for ip in ip_list:
            if ip in i[2]:
                i.append(ip)
                alerts.append(i)
    return alerts

def build_response(alerts):
    data = []
    logger(alerts)
    for _data in alerts:
        data.append({
            'ipFrom': _data[1],
            'log': _data[2],
            'date': _data[3],
            'ip': _data[4]
        })
    return data
