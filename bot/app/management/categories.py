# categories to be filled with the database information
# right now, they are being filled directly (for testing)

other = ['exclude', 'higher']
tradestatus = ['new', 'amended']
tenor = ['yup', 'gnqo', 'ollk', 'zxdv']
product_group = []
product = []
platform = ['x', 'y', '8i9', 'tex', 'n30o']
new_trade = []
net_client_position = []
near_tenor_days = []
max_future_date = []
marketer = ['opi', 'ghej', '3t7uu', 'thyl']
local_blotter = []
legs = ['near', 'far', 'spot']
from_days = []
far_tenor_days = []
expiration_date = []
deal_id = ['tyui', 'bnm', 't67y']
deal_date = []
currency_pair_group = []
currency_pair = ["usd/eur", "eur/usd"]
crds_code = []
dealside = ['buy', 'sell']
client = ['jpmorgan', 'axl', 'x', 'jhkl', '2w3e', 'e5ty', 'thyl', 't5joll', 'jiikk']
broker = []
ndf_fixing_date = []

volume = ['4890', '4gtj', '7890', '29099']
total_trades = []
std_dev_rollover_days = []
spot_price = []
rollover_ratio = []
rank = []
net_volume_ratio = []
net_volume = []
near_leg_volume = []
latest_rollover = []
ev = ['123r']
cc_total = ['6h7jk']
cc_nonrisk = []
cc_atrisk = []
avg_rollover = []
max_abs_net_volume = []

entries = ['tradestatus', 'tenor', 'productgroup',
           'product', 'platform', 'netclientposition', 'maxfuturedate',
           'marketer', 'localblotter', 'leg',
           'expire', 'deal', 'date',
           'currencypairgroup', 'currency', 'crdscode',
           'clientdeal', 'client', 'broker', 'ndfdate',
           'volume', 'totaltrades', 'stddevrollover',
           'spotpricestrike', 'rolloverratio', 'rank',
           'netvolumeratio', 'netvolume', 'neartenordays', 'nearlegvolume',
           'rollover', 'fromdays', 'fartenordays', 'ev',
           'cctotal', 'ccnonrisk', 'ccatrisk', 'averagerollover'
                                               'maxabsnetvolume']

# full list to help with going through all values
zero_list = entries + other + tradestatus + tenor + product_group + product + platform + new_trade + \
            net_client_position + near_tenor_days + max_future_date + marketer + local_blotter + legs + from_days + \
            far_tenor_days + expiration_date + deal_id + deal_date + currency_pair_group + crds_code + dealside + \
            client + broker + ndf_fixing_date + volume + total_trades + std_dev_rollover_days + spot_price + \
            rollover_ratio + rank + net_volume_ratio + net_volume + near_leg_volume + latest_rollover + ev + \
            cc_total + cc_nonrisk + cc_atrisk + avg_rollover + max_abs_net_volume


def identify_category(token):

    if token in zero_list:
        return '0'

    elif token in currency_pair:
        return '1'

    else:
        return ''
