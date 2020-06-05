from dataclasses import dataclass


@dataclass
class Player:
    type: str
    full_name: str
    indicators: list
    last_train: str

