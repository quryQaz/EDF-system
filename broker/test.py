import re

def parse_data(strings):
    _data = strings.split('/')
    print()
    print(_data)
    result = ""
    for __data in _data:
        print(__data)
        if len(re.findall(r'\[.*\]', __data)) >= 1:
            name = re.findall(r'\[.*\]', __data)[0]
            print(name)
            data = __data.replace(name, '')
            print(data)
            result += f'{name}: {data}\n\r'
    return result

test = "<EVENTS_BEGIN>/[EVENT_NAME]Tcpip/[EVENT_TYPE]2/[EVENT_ID]-2147479421/[EVENT_CATEGORY]0/[EVENT_TIME]2022-12-16 19:31:21/[EVENT_DATA]('',)/<EVENTS_END>"
new_data = test.replace('<EVENTS_BEGIN>', '').replace('<EVENTS_END>', '')
print(new_data)
parsed_data = parse_data(new_data)
print(parsed_data)
