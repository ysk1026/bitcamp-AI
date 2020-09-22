from dataclasses import dataclass


@dataclass
class Entity:

    context: str
    fname: str
    train: object
    text: object
    id: str
    label: str
