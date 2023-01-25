from flask import request

from api.edr.alerts.web.alerts_api import get_alerts

def alerts_route(app_route):
    @app_route.route('/api/alerts', methods = ['GET'])
    async def alerts_def():
        return await get_alerts(request)
