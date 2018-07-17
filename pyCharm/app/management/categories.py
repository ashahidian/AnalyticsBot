# create categories receiving the list of things to be in the category
names = []
currencies = []
deals = []
metrics = ['volume', 'cc', 'total cc']
platforms = []
tradestatus = []
legs = []
dealside = []


def category_names(list_names):

    for name in list_names:
        names.append(name)


def category_currency(list_currencies):

    for currency in list_currencies:
        currencies.append(currency)


def category_deal_id(list_deal_id):

    for deal_id in list_deal_id:
        deals.append(deal_id)