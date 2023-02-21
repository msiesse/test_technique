from dataclasses import dataclass


@dataclass
class RecommandationsOptionsDTO:
    department: str
    surface: int
    price: int
