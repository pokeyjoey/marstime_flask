import datetime

from nose.tools import raises, assert_equals
from app.mars.marsdate import MarsDate

class TestMarsDate(object):

    def setup(self):
        self.marsdate = MarsDate()

    #def test_get_correct_first_date_of_calendar(self):
    #	test_date = datetime.date(1961, 1, 1)
        #    mars_date = self.marsdate.get_date(test_date)

	    #assert_equals(mars_date, '1 Gemini I')

    #def test_get_correct_viking1_landing_date(self):
    #    test_date = datetime.date(1971, 11, 14)
    #    mars_date = self.marsdate.get_date(test_date)

    #	assert_equals(mars_date, '20 Pisces VI')

    #def test_get_correct_viking1_landing_date(self):
    #	test_date = datetime.date(1993, 8, 21)
    #    mars_date = self.marsdate.get_date(test_date)

    #	assert_equals(mars_date, '16 Libra XVIII')

    def test_get_correct_date(self):
	test_date = datetime.date(2015, 1, 27)
        mars_date = self.marsdate.get_date(test_date)

	assert_equals(mars_date, '29 Pisces L')
