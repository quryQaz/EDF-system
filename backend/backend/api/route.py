from flask import Blueprint

from api.edr.status.route import status_route
from api.edr.processes.route import processes_route
from api.edr.drivers.route import drivers_route
from api.edr.registry.route import registry_route
from api.edr.logs.route import logs_route
from api.edr.errors.route import errors_route
from api.edr.programs.route import programs_route
from api.edr.users.route import users_route
from api.edr.alerts.route import alerts_route
from api.edr.console.route import console_route
from api.edr.actions.route import actions_route

app_route = Blueprint('route', __name__)

status_route(app_route)
processes_route(app_route)
drivers_route(app_route)
registry_route(app_route)
logs_route(app_route)
errors_route(app_route)
programs_route(app_route)
users_route(app_route)
alerts_route(app_route)
console_route(app_route)
actions_route(app_route)
