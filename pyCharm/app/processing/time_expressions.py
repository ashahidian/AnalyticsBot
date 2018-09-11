from datetime import datetime, timedelta
#import parsedatetime as pdt #pip
import re


def time_synonyms_simple(expression):

    last_days = re.compile("last [0-9]+ days")
    next_days = re.compile("next [0-9]+ days")

    if expression == 'yesterday':
        yesterday = "{:%Y-%m-%d}".format(datetime.today() - timedelta(days=1))
        return yesterday

    elif expression == 'tomorrow':
        tomorrow = "{:%Y-%m-%d}".format(datetime.today() + timedelta(days=1))
        return tomorrow

    elif expression == 'last week':
        other = "{:%Y-%m-%d}".format(datetime.today() - timedelta(days=7))
        return [other, "{:%Y-%m-%d}".format(datetime.today())]

    elif expression == 'next week':
        other = "{:%Y-%m-%d}".format(datetime.today() + timedelta(days=7))
        return ["{:%Y-%m-%d}".format(datetime.today()), other]

    elif expression == 'this year':
        # calculating the current year
        now = datetime.now()
        return now.year

    elif expression == 'last year':
        now = datetime.now()
        last_year = now - timedelta(days=365)
        return [str(last_year.year) + str("-01-01"), str(last_year.year) + str("-12-31")]

    elif expression == 'next year':
        now = datetime.now()
        next_year = now + timedelta(days=365)
        return [str(next_year.year) + str("-01-01"), str(next_year.year) + str("-12-31")]

    elif last_days.match(expression):
        print "matched"


#def time_synonyms(expression):

   # date = datetime.datetime(*time_struct[:3])
   # return "{:%Y-%m-%d}".format(date)