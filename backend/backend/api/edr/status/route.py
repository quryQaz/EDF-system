from flask import request

from api.edr.status.web.status_api import get_statuses

def status_route(app_route):
    @app_route.route('/api/statuses', methods = ['GET'])
    async def statuses_def():
        return await get_statuses(request)
