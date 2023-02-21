import pytest

from scraping.cities_population import save_cities_population
from scraping.notes_scraping import scraping_notes
from scraping.price_rent_from_csv import save_square_meter_rent_price


# These are not really tests, but a way to launch scraping quickly
class TestScrappingData:

    # @pytest.mark.skip("Scraping of notes already done")
    def test_should_get_notes_of_cities(self):
        scraping_notes()

    # @pytest.mark.skip("Scraping of rent prices already done")
    def test_should_get_price_of_appartment_rent_by_square_meter_from_csv(self):
        save_square_meter_rent_price()

    # @pytest.mark.skip("Scraping of population already done")
    def test_should_get_population_of_cities(self):
        save_cities_population()