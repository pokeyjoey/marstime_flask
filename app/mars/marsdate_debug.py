import datetime
import calendar
import math
import roman

from collections import OrderedDict

class MarsDate(object):
    """
    TITLE:  ZubrinCalendar
    AUTHOR: Jeffery R Roche
    DATE  : 1/26/2015
     
    PURPOSE:
        This program calculates the current date on Mars according to a calendar
        invented by Dr. Robert Zubrin.
    """
    SOLS_IN_YEAR = 669
    MONTHS_OF_MARS = {
        61  : "Gemini",
        126 : "Cancer",
        192 : "Leo",
        257 : "Virgo",
        317 : "Libra",
        371 : "Scorpius",
        421 : "Sagittarius",
        468 : "Capricorn",
        514 : "Aquarius",
        562 : "Pisces",
        613 : "Aries",
        669 : "Taurus"
    }

    def __init__(self):
        self.months_of_mars = OrderedDict(
            sorted(self.MONTHS_OF_MARS.items(), key=lambda t: t[0]))

    def today(self):
        """ Return todays Martian Calendar date provided with an equivalent 
            Earth date represented by a datetime.date object.
        """
        today = datetime.date.today()
        todays_martian_date = self.get_date(today)

        return todays_martian_date

    def get_date(self, datetime_date_object):
        """ Return martian date for the Zubrin Calendar as represented
            by the provided datetime.date object.

            - returns date of the form: year-month- day of month (Roman Numberal)
                example - 29 Pisces XLIX
        """
        # get month, day, and year
        month = datetime_date_object.month
        day = datetime_date_object.day
        year = datetime_date_object.year
        day_of_year = datetime_date_object.timetuple().tm_yday
        days_in_earth_year = 366.0 if calendar.isleap(year) else 365.0

        # calculate constants for martian date calculation
        day_of_year_earth = datetime_date_object.timetuple().tm_yday
        print 'day_of_year_earth', day_of_year_earth
        earth_year_complete = (day_of_year/days_in_earth_year)
        print 'earth_year_complete', earth_year_complete
        earth_date = (year + earth_year_complete)
        print 'earth_date', earth_date
        mars_date = ((8.0/15.0) * (earth_date - 1961.0)) + 1.0
        print 'mars_date', mars_date
        mars_year = math.floor(mars_date)
        print 'mars_year', mars_year
        mars_date_complete = (mars_date - mars_year)
        print "mars_date_complete", mars_date_complete
        day_of_year_mars = round(self.SOLS_IN_YEAR * mars_date_complete)
        print "day_of_year_mars", day_of_year_mars

        # calculate the Martian month and day of month
        month_mars = self._month_mars(day_of_year_mars)
        day_mars = self._month_mars_day_of_month(day_of_year_mars)
	print 'month_mars', month_mars
	print 'day_mars', day_mars

        todays_date_mars = "{0} {1} {2}".format(
            int(day_mars), month_mars, roman.toRoman(int(mars_year)))

        return todays_date_mars

    def _month_mars(self, day_of_year_mars):
        """ Return the string for the current Martian month.
        """
        mars_month = "Set Me"
        print 'day_of_year_mars', day_of_year_mars

        # month_mars dictionary has a key value of the day of the 
        # martian year that corresponds to the last day of the month
        # of each of the 12 Martian months.
        # - iterate through the keys until we hit a day of the year
        #   less than the key. 
        # - Dictionary keys are organized from lowest to highest.
        for last_day_of_month in self.months_of_mars.iterkeys():
            print 'last_day_of_month', last_day_of_month
            if day_of_year_mars <= last_day_of_month:
                print 'day_of_year_mars', day_of_year_mars
                print 'last_day_of_month', last_day_of_month
                mars_month = self.months_of_mars[last_day_of_month]
                break

        return mars_month

    def _month_mars_day_of_month(self, day_of_year_mars):
        """ Return the string for the day of the current Martian month.
        """
        # initialize to Gemini the first month of the MArtian year
        last_day_of_previous_month = 61 
        day_of_month = 0

        # if we are in the first month Gemini, day_of_month equals
        # the day_of_year_mars.
        if day_of_year_mars <= 61:
            day_of_month = day_of_year_mars
            return day_of_month

        # determine which month we are in so we can calculate the day
        # of the month.            
        for last_day_of_month in self.months_of_mars.iterkeys():
            if day_of_year_mars <= last_day_of_month:
                day_of_month = \
                    (day_of_year_mars - (last_day_of_previous_month + 1)) + 1
                break

            last_day_of_previous_month = last_day_of_month

        return day_of_month
                   
