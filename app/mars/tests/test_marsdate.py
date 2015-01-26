import datetime

from nose.tools import raises, assert_equals
from app.mars.marsdate import MarsDate

class TestMarsDate(object):

    def setup(self):
        self.marsdate = MarsDate()

    def test_get_correct_first_date_of_calendar(self):
    	test_date = datetime.date(1961, 1, 1)
        mars_date = self.marsdate.get_date(test_date)

	assert_equals(mars_date, '1 Gemini I')

    def test_get_correct_mariner4_flyby(self):
        test_date = datetime.date(1965, 7, 15)
        mars_date = self.marsdate.get_date(test_date)

    	assert_equals(mars_date, '20 Pisces VI')

    def test_get_correct_mariner6_flyby(self):
        test_date = datetime.date(1969, 7, 31)
        mars_date = self.marsdate.get_date(test_date)

    	assert_equals(mars_date, '16 Sagittarius V')

    def test_get_correct_mariner7_flyby(self):
        test_date = datetime.date(1969, 8, 5)
        mars_date = self.marsdate.get_date(test_date)

    	assert_equals(mars_date, '20 Sagittarius V')

    def test_get_correct_mariner9_orbit(self):
        test_date = datetime.date(1971, 11, 14)
        mars_date = self.marsdate.get_date(test_date)

    	assert_equals(mars_date, '20 Pisces VI')

    def test_get_correct_mars2_mars3_land(self):
        test_date = datetime.date(1971, 12, 2)
        mars_date = self.marsdate.get_date(test_date)

    	assert_equals(mars_date, '37 Pisces VI')

    def test_get_correct_viking1_arrives_in_orbit(self):
    	test_date = datetime.date(1976, 6, 19)
        mars_date = self.marsdate.get_date(test_date)

    	assert_equals(mars_date, '41 Leo IX')

    def test_get_correct_viking2_landing(self):
    	test_date = datetime.date(1976, 9, 3)
        mars_date = self.marsdate.get_date(test_date)

    	assert_equals(mars_date, '49 Virgo IX')

    def test_get_correct_viking1_landing(self):
    	test_date = datetime.date(1976, 7, 20)
        mars_date = self.marsdate.get_date(test_date)

    	assert_equals(mars_date, '5 Virgo IX')

    def test_get_correct_date_2015(self):
	test_date = datetime.date(2015, 1, 27)
        mars_date = self.marsdate.get_date(test_date)

	assert_equals(mars_date, '48 Pisces XXIX')
