from datetime import datetime, timedelta
# import parsedatetime as pdt #pip
import re


def time_synonyms_simple(expression):
    matched = re.search(r"(next|last)\s([0-9\s]*)(day|week|year|quarter)")

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

    elif matched.group(1) == 'next':
        if matched.group(3) == 'day':
            if matched.group(2) != "":
                number = matched.group(2)
                other = "{:%Y-%m-%d}".format(datetime.today() + timedelta(days=number))
                return ["{:%Y-%m-%d}".format(datetime.today()), other]

            else:
                number = 1
                other = "{:%Y-%m-%d}".format(datetime.today() + timedelta(days=number))
                return ["{:%Y-%m-%d}".format(datetime.today()), other]

        elif matched.group(3) == 'week':
            if matched.group(2) != "":
                number = matched.group(2)
                other = "{:%Y-%m-%d}".format(datetime.today() + timedelta(weeks=number))
                return ["{:%Y-%m-%d}".format(datetime.today()), other]

            else:
                number = 1
                other = "{:%Y-%m-%d}".format(datetime.today() + timedelta(weeks=number))
                return ["{:%Y-%m-%d}".format(datetime.today()), other]

        elif matched.group(3) == 'year':
            if matched.group(2) != "":
                number = matched.group(2)
                other = "{:%Y-%m-%d}".format(datetime.today() + timedelta(weeks=number * 52))
                return ["{:%Y-%m-%d}".format(datetime.today()), other]

            else:
                number = 1
                other = "{:%Y-%m-%d}".format(datetime.today() + timedelta(weeks=number * 52))
                return ["{:%Y-%m-%d}".format(datetime.today()), other]

    elif matched.group(1) == 'last':
        if matched.group(3) == 'day':
            if matched.group(2) != "":
                number = matched.group(2)
                other = "{:%Y-%m-%d}".format(datetime.today() - timedelta(days=number))
                return [other, "{:%Y-%m-%d}".format(datetime.today())]

            else:
                number = 1
                other = "{:%Y-%m-%d}".format(datetime.today() + timedelta(days=number))
                return ["{:%Y-%m-%d}".format(datetime.today()), other]

        elif matched.group(3) == 'week':
            if matched.group(2) != "":
                number = matched.group(2)
                other = "{:%Y-%m-%d}".format(datetime.today() - timedelta(weeks=number))
                return [other, "{:%Y-%m-%d}".format(datetime.today())]

            else:
                number = 1
                other = "{:%Y-%m-%d}".format(datetime.today() + timedelta(weeks=number))
                return ["{:%Y-%m-%d}".format(datetime.today()), other]

        elif matched.group(3) == 'year':
            if matched.group(2) != "":
                number = matched.group(2)
                other = "{:%Y-%m-%d}".format(datetime.today() - timedelta(weeks=number * 52))
                return [other, "{:%Y-%m-%d}".format(datetime.today())]

            else:
                number = 1
                other = "{:%Y-%m-%d}".format(datetime.today() + timedelta(weeks=number * 52))
                return ["{:%Y-%m-%d}".format(datetime.today()), other]


def calculate_last_quarter():
    now = datetime(2018, 7, 28)
    quarter = (now.month - 1) / 3 + 1
    last_day_last_quarter = datetime(now.year, 3 * quarter - 2, 1)
    first_day_last_quarter = datetime(last_day_last_quarter.year if last_day_last_quarter.month - 3 >= 0
                                      else last_day_last_quarter.year - 1, (last_day_last_quarter.month - 3) % 12, 1)

    return [first_day_last_quarter, last_day_last_quarter]


def calculate_next_quarter():
    now = datetime.now()
    current_quarter = (now.month - 1) / 3 + 1
    future_quarter = (current_quarter + 4) % 4 + 1
    future_quarter_first = datetime(now.year if future_quarter != 1
                                    else now.year + 1, (current_quarter * 3 + 1) % 12, 1)
    future_quarter_last = datetime(now.year + 1 if (future_quarter == 1) or (future_quarter == 4)
                                   else now.year, (future_quarter * 3 + 1) % 12, 1)

    return [future_quarter_first, future_quarter_last]


#if __name__ == '__main__':
#    last = calculate_last_quarter()
#    next = calculate_next_quarter()

#    print(last, next)
