from dataclasses import dataclass


@dataclass
class Entity:

    context: str = '/Users/youngseonkim/Documents/SbaProjects/titanic/data/'
    fname: str = ''
    train: object = None
    text: object = None
    id: str = ''
    label: str = ''
