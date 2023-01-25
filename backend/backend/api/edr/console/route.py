from flask import request

from api.edr.console.web.console_api import get_console

def console_route(app_route):
    @app_route.route('/api/console', methods = ['POST'])
    async def console_def():
        return await get_console(request)
