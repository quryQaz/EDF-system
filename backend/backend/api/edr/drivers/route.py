from flask import request

from api.edr.drivers.web.drivers_api import get_drivers

def drivers_route(app_route):
    @app_route.route('/api/drivers', methods = ['POST'])
    async def drivers_def():
        return await get_drivers(request)
