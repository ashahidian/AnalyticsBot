# first, call the database and gather the client names, id's and currencies
from bot.app.management.sql_connection import sql_call

other = ['exclude', 'higher']
tradestatus = ['new', 'ammended']
tenor = []
product_group = []
product = []
platform = []
new_trade = []
net_client_position = []
near_tenor_days = []
max_future_date = []
marketer = []
local_blotter = []
legs = ['near leg', 'far leg', 'spot']
from_days = []
far_tenor_days = []
expiration_date = []
deal_id = []
deal_date = []
currency_pair_group = []
currency_pair = ["usd/eur", "eur/usd"]
crds_code = []
dealside = ['buy', 'sell']
client = ['jpmorgan', 'axl']
brooker = []
ndf_fixing_date = []

volume = []
total_trades = []
std_dev_rollover_days = []
spot_price = []
rollover_ratio = []
rank = []
net_volume_ratio = []
net_volume = []
near_leg_volume = []
latest_rollover = []
ev = []
cc_total = []
cc_nonrisk = []
cc_atrisk = []
avg_rollover = []
max_abs_net_volume = []

entries = ['tradestatus', 'tenor', 'productgroup',
              'product', 'platform', 'netclientposition', 'maxfuturedate',
              'marketer', 'localblotter', 'leg',
               'expire', 'deal', 'date',
              'currencypairgroup', 'currency', 'crdscode',
              'clientdeal', 'client', 'brooker', 'ndfdate',
           'volume','totaltrades', 'stddevrollover',
           'spotpricestrike', 'rolloverratio', 'rank',
           'netvolumeratio', 'netvolume', 'neartenordays', 'nearlegvolume',
           'rollover', 'fromdays', 'fartenordays', 'ev',
           'cctotal', 'ccnonrisk', 'ccatrisk', 'averagerollover'
           'maxabsnetvolume']

# call sql_call function to get the values from the database
# def setup_categories():
#     tenor = sql_call("SELECT DISTINCT STRING_AGG(Tenor, ', ') FROM example_table")
#     product_group = sql_call("SELECT DISTINCT STRING_AGG(Product Group, ', ') FROM example_table")
#     product = sql_call("SELECT DISTINCT STRING_AGG(Product, ', ') FROM example_table")
#     platform = sql_call("SELECT DISTINCT STRING_AGG(Platform, ', ') FROM example_table")
#     new_trade = sql_call("SELECT DISTINCT STRING_AGG(NewTrade, ', ') FROM example_table")
#     net_client_position = sql_call("SELECT DISTINCT STRING_AGG(NetClientPosition, ', ') FROM example_table")
#     near_tenor_days = sql_call("SELECT DISTINCT STRING_AGG(NearTenorDays, ', ') FROM example_table")
#     max_future_date = sql_call("SELECT DISTINCT STRING_AGG(MaxFutureDate, ', ') FROM example_table")
#     marketer = sql_call("SELECT DISTINCT STRING_AGG(Marketer, ', ') FROM example_table")
#     local_blotter = sql_call("SELECT DISTINCT STRING_AGG(LocalBlotter, ', ') FROM example_table")
#     from_days = sql_call("SELECT DISTINCT STRING_AGG(FromDays, ', ') FROM example_table")
#     far_tenor_days = sql_call("SELECT DISTINCT STRING_AGG(FarTenorDays, ', ') FROM example_table")
#     expiration_date = sql_call("SELECT DISTINCT STRING_AGG(Expiry Date, ', ') FROM example_table")
#     deal_id = sql_call("SELECT DISTINCT STRING_AGG(Deal ID, ', ') FROM example_table")
#     deal_date = sql_call("SELECT DISTINCT STRING_AGG(Deal Date, ', ') FROM example_table")
#     currency_pair_group = sql_call("SELECT DISTINCT STRING_AGG(CurrencyPairGroup, ', ') FROM example_table")
#     currency_pair = sql_call("SELECT DISTINCT STRING_AGG(Currency Pair, ', ') Pair FROM example_table")
#     crds_code = sql_call("SELECT DISTINCT STRING_AGG(CRDS Code, ', ') FROM example_table")
#     client = sql_call("SELECT DISTINCT STRING_AGG(Client, ', ') FROM example_table")
#     brooker = sql_call("SELECT DISTINCT STRING_AGG(Broker_FXT, ', ') FROM example_table")
#     ndf_fixing_date = sql_call("SELECT DISTINCT STRING_AGG(NDF Fixing Date, ', ') FROM example_table")
#
#     volume = sql_call("SELECT DISTINCT STRING_AGG(Volume, ', ') FROM example_table")
#     total_trades = sql_call("SELECT DISTINCT STRING_AGG(TotalTrades, ', ') FROM example_table")
#     std_dev_rollover_days = sql_call("SELECT DISTINCT STRING_AGG(StdDevRolloverDays, ', ') FROM example_table")
#     spot_price = sql_call("SELECT DISTINCT STRING_AGG(Spot Price Strike, ', ') FROM example_table")
#     rollover_ratio = sql_call("SELECT DISTINCT STRING_AGG(RolloverRatio, ', ') FROM example_table")
#     rank = sql_call("SELECT DISTINCT STRING_AGG(Rank, ', ') FROM example_table")
#     net_volume_ratio = sql_call("SELECT DISTINCT STRING_AGG(NetRolloverRatio, ', ') FROM example_table")
#     net_volume = sql_call("SELECT DISTINCT STRING_AGG(NetVolume, ', ') FROM example_table")
#     near_leg_volume = sql_call("SELECT DISTINCT STRING_AGG(NearLegVolume, ', ') FROM example_table")
#     latest_rollover = sql_call("SELECT DISTINCT STRING_AGG(LatestRolloverDays, ', ') FROM example_table")
#     ev = sql_call("SELECT DISTINCT STRING_AGG(EV, ', ') FROM example_table")
#     cc_total = sql_call("SELECT DISTINCT STRING_AGG(CC Total, ', ') FROM example_table")
#     cc_nonrisk = sql_call("SELECT DISTINCT STRING_AGG(CC NonRisk, ', ') FROM example_table")
#     cc_atrisk = sql_call("SELECT DISTINCT STRING_AGG(CC AtRisk, ', ') FROM example_table")
#     avg_rollover = sql_call("SELECT DISTINCT STRING_AGG(AverageRolloverDays, ', ') FROM example_table")
#     max_abs_net_volume = sql_call("SELECT DISTINCT STRING_AGG(MaxAbsNetVolume, ', ') FROM example_table")

#    return 0



