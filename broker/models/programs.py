from models.base_model import BaseModel

class Programs(BaseModel):

    ip: str = ''

    def __init__(self, ip):
        super().__init__(ip)
