from flask import request

from api.edr.users.web.users_api import get_users

def users_route(app_route):
    @app_route.route('/api/users', methods = ['POST'])
    async def users_def():
        return await get_users(request)
