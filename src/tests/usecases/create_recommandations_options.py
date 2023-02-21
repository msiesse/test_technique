from usecases.dtos import RecommandationsOptionsDTO


def create_recommandations_options(
        department: str = "75",
        surface: int = 1,
        price: int = 500
) -> RecommandationsOptionsDTO:
    return RecommandationsOptionsDTO(department, surface, price)