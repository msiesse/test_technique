import pytest

from scraping.notes_scraping import scraping_notes


# These are not really tests, but a way to launch scraping quickly
class TestScrappingData:

    @pytest.mark.skip("Scraping of notes already done")
    def test_should_get_notes_of_cities(self):
        scraping_notes()

    def test_should_get_price_of_appartment_rent_by_square_meter_from_csv(self):
        pass