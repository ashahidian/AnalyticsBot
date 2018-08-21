# create categories receiving the list of things to be in the category
names = []
currencies = []
deals = []
platforms = []
volume = []
cc = []
total_cc = []
rollover_ration = []
netvolume = []
tradestatus = ['new', 'amended']
legs = ['near leg', 'far leg', 'spot']
dealside = ['buy', 'sell']
crds_code = []


def category_names(list_names):

    for name in list_names:
        names.append(name)


def category_currency(list_currencies):

    for currency in list_currencies:
        currencies.append(currency)


def category_deal_id(list_deal_id):

    for deal_id in list_deal_id:
        deals.append(deal_id)


def category_platform(list_platform):

    for platform in list_platform:
        platforms.append(platform)


def crdscode(list_crds):

    for code in list_crds:
        crds_code.append(code)
