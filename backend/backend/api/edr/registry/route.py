from flask import request

from api.edr.registry.web.registry_api import get_registry

def registry_route(app_route):
    @app_route.route('/api/registry', methods = ['POST'])
    async def registry_def():
        return await get_registry(request)
