from datetime import datetime, timedelta


def time_synonyms(expression):

    if expression == 'yesterday':
        yesterday = datetime.today() - timedelta(days=1)
        return yesterday

    elif expression == 'last week':
        week = []
        for day in (1,7):
            week.append(datetime.today() - timedelta(days=day))

    elif expression == 'next week':
        week = []
        for day in (1,7):
            week.append(datetime.today() + timedelta(days=day))

    elif expression == 'this year':
        # calculating the current year
        now = datetime.now()
        return now.year

    elif expression == 'last year':
        now = datetime.now()
        last_year = now - timedelta(days=365)
        return last_year.year


expire_synonyms = ['expiration', 'expire', 'expires', 'expiration date', 'expiry date', 'expiry']
exclude_synonyms = ['exclude', 'excluding', 'remove']
higher_synonyms = ['more', 'greater', 'higher', 'superior', 'surpassing', 'larger', 'above']
crdscode_synonyms = ['crds code', 'crdscode']
client_synonyms = ['clients', 'client']
currency_synonyms = ['currency', 'currency pair']
deal_date_synonyms = ['deal date', 'signed', 'date', 'created']


def synonym_check(word):

    if word in expire_synonyms:
        return 'expire'
    elif word in exclude_synonyms:
        return 'exclude'
    elif word in higher_synonyms:
        return 'higher'
    elif word in crdscode_synonyms:
        return 'crdscode'
    elif word in client_synonyms:
        return 'client'
    elif word in currency_synonyms:
        return 'currency'
    elif word in deal_date_synonyms:
        return 'date'
    else:
        return word
