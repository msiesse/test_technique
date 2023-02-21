from tests.factories.city import create_city
from tests.usecases.create_recommandations_options import create_recommandations_options
from tests.usecases.fake_repositories import FakeInMemoryCityRepository
from usecases.get_recommandations_of_cities import GetRecommandationsOfCitiesUsecase


class TestGetRecommandationsOfCities:
    def setup_method(self):
        self.city_repository = FakeInMemoryCityRepository()
        self.recommand = GetRecommandationsOfCitiesUsecase(self.city_repository)

    def test_should_get_no_recommandations_when_budget_is_zero(self):
        self.save_city("Paris", 30)
        options = create_recommandations_options(price=0)
        assert self.recommand(options) == []

    def test_should_recommand_paris_with_high_budget(self):
        self.save_city("Paris", 30)
        options = create_recommandations_options(price=100000)
        assert self.recommand(options) == [self.paris]

    def test_should_not_recommand_paris_if_budget_is_too_low(self):
        self.save_city("Paris", 30)
        options = create_recommandations_options(price=29)
        assert self.recommand(options) == []

    def test_should_not_recommand_paris_if_budget_too_low_with_high_surface(self):
        self.save_city("Paris", 30)
        options = create_recommandations_options(price=2900, surface=100)
        assert self.recommand(options) == []

    def test_should_recommand_paris_if_budget_is_at_the_limit(self):
        self.save_city("Paris", 30.1)
        self.city_repository.save(self.paris)
        options = create_recommandations_options(price=3010, surface=100)
        assert self.recommand(options) == [self.paris]

    def test_should_not_recommand_paris_if_department_is_not_75(self):
        self.save_city("Paris", 30)
        self.city_repository.save(self.paris)
        options = create_recommandations_options(department="54", price=30)
        assert self.recommand(options) == []

    def save_city(self, name: str, price: float):
        self.paris = create_city(name=name, price=price)
        self.city_repository.save(self.paris)
