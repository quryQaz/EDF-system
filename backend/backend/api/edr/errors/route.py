from flask import request

from api.edr.errors.web.errors_api import get_errors

def errors_route(app_route):
    @app_route.route('/api/errors', methods = ['POST'])
    async def errors_def():
        return await get_errors(request)
