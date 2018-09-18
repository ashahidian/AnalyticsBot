# create categories receiving the list of things to be in the category

names = []
currencies = []
deals = []
platforms = []
volume = []
at_risk_cc = []
non_risk_cc = []
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


def category_at_risk_cc(list_at_risk_cc):

    for c in list_at_risk_cc:
        at_risk_cc.append(c)


def category_non_risk_cc(list_non_risk_cc):

    for c in list_non_risk_cc:
        non_risk_cc.append(c)


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


def identify_category(token):
    if token in names :
        return 'Client'

    elif token in currencies:
        return 'Currency Pair'

    elif token in deals:
        return 'Deal ID'

    elif token in platforms:
        return 'Platform'

    elif token in volume:
        return 'Volume'

    elif token in at_risk_cc:
        return 'CC AtRisk'

    elif token in non_risk_cc:
        return 'CC NonRisk'

    elif token in total_cc:
        return 'CC Total'

    elif token in rollover_ratio:
        return 'RolloverRatio'

    elif token in netvolume:
        return 'NetVolume'

    elif token in tradestatus:
        return 'TradeStatus'

    elif token in legs:
        return 'Leg'

    elif token in dealside:
        return 'Client Deal Side'

    elif token in crds_code:
        return 'CRDSCode'

    else:
        return ''