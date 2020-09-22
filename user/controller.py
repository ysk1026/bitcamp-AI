from user.entity import Entity
from user.service import Service


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()
