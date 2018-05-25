from datetime import datetime, timedelta


def time_synonyms(word):
    if word == 'today':
        now = datetime.now()
        return now.strftime("%Y-%m-%d")

    if word == 'yesterday':
        yesterday = datetime.today() - timedelta(days=1)
        return yesterday

    if word == 'this year':
        # calculating the current year
        now = datetime.now()
        return now.year

    if word == 'last year':
        now = datetime.now()
        last_year = now - timedelta(days=365)
        return last_year.year

# there may be a better way to do this
    if word == 'first quarter':
        return ['january', 'february', 'march']

    if word == 'second quarter':
        return ['april', 'may', 'june']

    if word == 'third quarter':
        return ['july', 'august', 'september']

    if word == 'fourth quarter':
        return ['october', 'november', 'december']

    if word == 'last quarter':
        now = datetime.now()
        now_month = now.month
        last_quarter_month = now_month - 4

        if 4 > last_quarter_month:
            last_quarter = 'first_quarter'
        elif 4 <= last_quarter_month < 6:
            last_quarter = 'second quarter'
        elif 6 <= last_quarter_month < 9:
            last_quarter = 'third quarter'
        else:
            last_quarter = 'fourth quarter'

        return last_quarter
