from flask import request

from api.edr.programs.web.programs_api import get_programs

def programs_route(app_route):
    @app_route.route('/api/programs', methods = ['POST'])
    async def programs_def():
        return await get_programs(request)
