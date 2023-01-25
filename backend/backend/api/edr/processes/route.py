from flask import request

from api.edr.processes.web.processes_api import get_processes

def processes_route(app_route):
    @app_route.route('/api/processes', methods = ['POST'])
    async def prcesses_def():
        return await get_processes(request)
