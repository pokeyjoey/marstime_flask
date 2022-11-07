import pytest
import datetime

from app.mars.marsdate import MarsDate

@pytest.fixture
def calendar():
    calendar = MarsDate()

    yield calendar

def test_get_correct_first_date_of_calendar(calendar):
    test_date = datetime.date(1961, 1, 1)
    mars_date = calendar.get_date(test_date)

    assert mars_date == '1 Gemini I'

def test_get_correct_mariner6_flyby(calendar):
    test_date = datetime.date(1969, 7, 31)
    mars_date = calendar.get_date(test_date)

    assert mars_date == '15 Sagittarius V'

def test_get_correct_mariner7_flyby(calendar):
    test_date = datetime.date(1969, 8, 5)
    mars_date = calendar.get_date(test_date)

    assert mars_date == '20 Sagittarius V'

def test_get_correct_mariner9_orbit(calendar):
    test_date = datetime.date(1971, 11, 14)
    mars_date = calendar.get_date(test_date)

    assert mars_date == '20 Pisces VI'

def test_get_correct_mars2_mars3_land(calendar):
    test_date = datetime.date(1971, 12, 2)
    mars_date = calendar.get_date(test_date)

    assert mars_date == '37 Pisces VI'

def test_get_correct_viking1_arrives_in_orbit(calendar):
    test_date = datetime.date(1976, 6, 19)
    mars_date = calendar.get_date(test_date)

    assert mars_date == '41 Leo IX'

def test_get_correct_viking2_landing(calendar):
    test_date = datetime.date(1976, 9, 3)
    mars_date = calendar.get_date(test_date)

    assert mars_date == '49 Virgo IX'

def test_get_correct_viking1_landing(calendar):
    test_date = datetime.date(1976, 7, 20)
    mars_date = calendar.get_date(test_date)

    assert mars_date == '5 Virgo IX'

def test_get_correct_date_2015(calendar):
    test_date = datetime.date(2015, 1, 27)
    mars_date = calendar.get_date(test_date)

    assert mars_date == '48 Pisces XXIX'