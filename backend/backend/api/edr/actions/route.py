from flask import request

from api.edr.actions.web.actions_api import disconnect
from api.edr.actions.web.actions_api import clear

def actions_route(app_route):
    @app_route.route('/api/actions/disconnect', methods = ['POST'])
    async def disconnect_def():
        return await disconnect(request)

    @app_route.route('/api/actions/clear', methods = ['POST'])
    async def clear_def():
        return await clear(request)
