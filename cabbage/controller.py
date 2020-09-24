import sys
sys.path.insert(0, '/Users/youngseonkim/Documents/SbaProjects')
from cabbage.entity import Entity
from cabbage.service import Service
class Controller():
    def __init__(self):
        self.entity = Entity()
        self.service = Service()
        