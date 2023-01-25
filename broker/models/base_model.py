from tarantool import Connection
import datetime

class BaseModel:

    ip = None

    def __init__(self, ip: str):
        self.ip = ip

    def select(self): # Выбор элементов по ip адресу
        try:
            connection = Connection("127.0.0.1", 3301)
            space = connection.space(str(self.__class__.__name__).lower())
            result = space.select(self.ip, index = 1)
            connection.close()
            return result
        except BaseException as e:
            print(f'ERROR {e}')

    def update(self, data: str): # обновление элемента по ip адресу. Пока используется только для статуса
        try:
            connection = Connection("127.0.0.1", 3301)
            space = connection.space(str(self.__class__.__name__).lower())
            result = space.select(self.ip, index = 1)
            if result: # Если элемент есть, то обновить
                response = space.update(result[0][0], [('=', 2, data)])
            else: # если нет, то записать новый
                response = space.call(f"box.space.{str(self.__class__.__name__).lower()}:auto_increment", [[self.ip, data]])
            connection.close()
            return response
        except BaseException as e:
            print(f'ERROR {e}')

    def insert(self, data: str): # Запись новых элементов
        try:
            connection = Connection("127.0.0.1", 3301)
            space = connection.space(str(self.__class__.__name__).lower())
            result = space.select(self.ip, index = 1)
            response = space.call(f"box.space.{str(self.__class__.__name__).lower()}:auto_increment", [[self.ip, data, datetime.datetime.now().strftime("%d.%m.%Y %H:%M")]])
            connection.close()
            return response
        except BaseException as e:
            print(f'ERROR {e}')
