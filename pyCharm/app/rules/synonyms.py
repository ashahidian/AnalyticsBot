from datetime import datetime, timedelta


def time_synonyms(word):

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


expire_synonyms = ['expiration', 'expire', 'expires', 'expiration date', 'expiry date', 'expiry']
deals_synonyms = []
higher_synonyms = ['more', 'greater', 'higher']


def synonym_check(word):

    if word in expire_synonyms:
        return 'expire'
    else:
        return word
