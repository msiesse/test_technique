from abc import ABC, abstractmethod

from domain.entities.city import City


class ICityRepository(ABC):
    @abstractmethod
    def save(self, city: City) -> None: ...

    @abstractmethod
    def find_all(self, **kwargs) -> list[City]: ...