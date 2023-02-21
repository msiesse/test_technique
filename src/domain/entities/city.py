from dataclasses import dataclass


@dataclass
class City:
    uuid: str
    name: str
    department: str
    price: float
    population: int
    note: float