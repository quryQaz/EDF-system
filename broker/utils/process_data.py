from models.logs import Logs
from models.users import Users
from models.errors import Errors
from models.drivers import Drivers
from models.registry import Registry
from models.programs import Programs
from models.processes import Processes
import re

def process_data(ip, data, sel, __added_key):
    print(ip)
    print(data)
    str_data = data.decode("utf-8")
    if "<PROCESSES_BEGIN>" in str_data:
        new_data = str_data.replace('<PROCESSES_BEGIN>', '').replace('<PROCESSES_END>', '')
        parsed_data = parse_data(new_data)
        processes = Processes(ip)
        return processes.insert(parsed_data)
    elif "<DRIVERS_BEGIN>" in str_data:
        new_data = str_data.replace('<DRIVERS_BEGIN>', '').replace('<DRIVERS_END>', '')
        # parsed_data = parse_data(new_data)
        drivers = Drivers(ip)
        return drivers.insert(new_data)
    elif "<SYSTEM_BEGIN>" in str_data:
        new_data = str_data.replace('<SYSTEM_BEGIN>', '').replace('<SYSTEM_END>', '')
        parsed_data = parse_data(new_data)
        registry = Registry(ip)
        return registry.insert(parsed_data)
    elif "<EVENTS_BEGIN>" in str_data:
        new_data = str_data.replace('<EVENTS_BEGIN>', '').replace('<EVENTS_END>', '')
        parsed_data = parse_data(new_data)
        logs = Logs(ip)
        return logs.insert(parsed_data)
    elif "<ERRORS_BEGIN>" in str_data:
        new_data = str_data.replace('<ERRORS_BEGIN>', '').replace('<ERRORS_END>', '')
        print(new_data)
        parsed_data = parse_data(new_data)
        print(parsed_data)
        errors = Errors(ip)
        return errors.insert(parsed_data)
    elif "<SOFTWARE_BEGIN>" in str_data:
        new_data = str_data.replace('<SOFTWARE_BEGIN>', '').replace('<SOFTWARE_END>', '')
        parsed_data = parse_data(new_data)
        programs = Programs(ip)
        return programs.insert(parsed_data)
    elif "<USERS_BEGIN>" in str_data:
        new_data = str_data.replace('<USERS_BEGIN>', '').replace('<USERS_END>', '')
        parsed_data = parse_data(new_data)
        users = Users(ip)
        return users.insert(parsed_data)
    elif "<CONSOLE_BEGIN>" in str_data:
        new_data = str_data.replace('<CONSOLE_BEGIN>', '')
        if __added_key:
            __added_key.fileobj.send(new_data.encode('utf-8'))

def parse_data(strings):
    _data = strings.split('/')
    result = ""
    for __data in _data:
        if len(re.findall(r'\[.*\]', __data)) >= 1:
            name = re.findall(r'\[.*\]', __data)[0]
            data = __data.replace(name, '')
            result += f'{name}: {data}\n\r'
    return result
