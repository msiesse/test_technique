from domain.entities.city import City


def create_city(
        uuid: str = "Paris",
        name: str = "Paris",
        department: str = "75",
        price: float = 30,
        population: int = 2000000,
        note: float = 3.7
) -> City:
    return City(uuid, name, department, price, population, note)
