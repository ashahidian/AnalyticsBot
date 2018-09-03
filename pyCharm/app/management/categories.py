# create categories receiving the list of things to be in the category
names = []
currencies = []
deals = []
platforms = []
volume = []
cc = []
total_cc = []
rollover_ratio = []
netvolume = []
tradestatus = ['new', 'amended']
legs = ['near leg', 'far leg', 'spot']
dealside = ['buy', 'sell']
crds_code = []

dimensions = ['tradestatus', 'tenor', 'productkey', 'product group',
              'product', 'platform', 'netclientposition', 'maxfuturedate',
              'marketingclientkey', 'marketer', 'localblotter', 'leg',
              'fardatekey', 'expiry date', 'deal id', 'deal date',
              'date today', 'currencypairgroup', 'currency pair', 'crdscode',
              'client deal side', 'client', 'broker_fxt', 'ndf fixing date']

metrics = ['volume','transactionnumber', 'totaltrades', 'stddevrolloverdays',
           'spot Price Strike', 'RolloverRatio', 'Rank', 'NewTrade',
           'netvolumeratio', 'netvolume', 'neartenordays', 'NearLegVolume',
           'latestrolloverdays', 'fromdays', 'fartenordays', 'ev',
           'cc total', 'cc nonrisk', 'cc atrisk', 'averagerolloverdays'
           'maxabsnetvolume']


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


def category_volume(list_volume):

    for v in list_volume:
        volume.append(v)


def category_cc(list_cc):

    for c in list_cc:
        cc.append(c)


def category_total_cc(list_total_cc):

    for tc in list_total_cc:
        total_cc.append(tc)


def category_r_ratio(list_r_ratio):

    for rr in list_r_ratio:
        rollover_ratio.append(rr)


def category_net_volume(list_net_volume):

    for nv in list_net_volume:
        netvolume.append(nv)


def crdscode(list_crds):

    for code in list_crds:
        crds_code.append(code)
