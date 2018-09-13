from datetime import datetime, timedelta, date
# import parsedatetime as pdt #pip
import re


def time_synonyms(expression, type):
    matched = re.search(r"(next|last)\s([0-9\s]*)(day|week|year|quarter)", expression)
    year_request = re.search(r"([0-9]{4})", expression)

    now = datetime.today()
    formatted_now = "{:%Y-%m-%d}".format(now)

    if expression == 'yesterday':
        yesterday = now - timedelta(days=1)

        if type == 1:
            return "{:%Y-%m-%d}".format(yesterday)
        else:
            difference = now.date() - yesterday.date()
            return difference.days

    elif expression == 'tomorrow':
        tomorrow = "{:%Y-%m-%d}".format(now + timedelta(days=1))
        return tomorrow

    elif expression == 'this year':
        # calculating the current year
        return ["{:%Y-%m-%d}".format(datetime(now.year, 1, 1)), "{:%Y-%m-%d}".format(datetime(now.year, 12, 31))]

    elif year_request:
        return[datetime(int(year_request.group(1)), 1, 1), datetime(int(year_request.group(1)), 12, 31)]

    elif matched.group(1) == 'next':
        if matched.group(3) == 'day':
            if matched.group(2) != "":
                number = int(matched.group(2))
                other = "{:%Y-%m-%d}".format(now + timedelta(days=number))
                return [formatted_now, other]

            else:
                number = 1
                other = "{:%Y-%m-%d}".format(now + timedelta(days=number))
                return [formatted_now, other]

        elif matched.group(3) == 'week':
            if matched.group(2) != "":
                number = int(matched.group(2))
                other = "{:%Y-%m-%d}".format(now + timedelta(weeks=number))
                return [formatted_now, other]

            else:
                number = 1
                other = "{:%Y-%m-%d}".format(now + timedelta(weeks=number))
                return [formatted_now, other]

        elif matched.group(3) == 'year':
            if matched.group(2) != "":
                number = int(matched.group(2))
                other = "{:%Y-%m-%d}".format(now + timedelta(weeks=number * 52))
                return [formatted_now, other]

            else:
                number = 1
                other = "{:%Y-%m-%d}".format(now + timedelta(weeks=number * 52))
                return [formatted_now, other]

        elif matched.group(3) == 'quarter':
            return calculate_next_quarter()

    elif matched.group(1) == 'last':
        if matched.group(3) == 'day':
            if matched.group(2) != "":
                number = int(matched.group(2))
                other = "{:%Y-%m-%d}".format(now - timedelta(days=number))
                return [other, formatted_now]

            else:
                number = 1
                other = "{:%Y-%m-%d}".format(now - timedelta(days=number))
                return [other, formatted_now]

        elif matched.group(3) == 'week':
            if matched.group(2) != "":
                number = int(matched.group(2))
                other = "{:%Y-%m-%d}".format(now - timedelta(weeks=number))
                return [other, formatted_now]

            else:
                number = 1
                other = "{:%Y-%m-%d}".format(now - timedelta(weeks=number))
                return [other, formatted_now]

        elif matched.group(3) == 'year':
            if matched.group(2) != "":
                number = int(matched.group(2))
                other = "{:%Y-%m-%d}".format(now - timedelta(weeks=number * 52))
                return [other, formatted_now]

            else:
                number = 1
                other = "{:%Y-%m-%d}".format(now - timedelta(weeks=number * 52))
                return [other, formatted_now]

        elif matched.group(3) == 'quarter':
            return calculate_last_quarter()


def calculate_last_quarter():
    now = datetime.now()
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
#    test = time_synonyms("next 2 years")

#    print(test)
#    last = calculate_last_quarter()
#    next = calculate_next_quarter()

#    print(last, next)
