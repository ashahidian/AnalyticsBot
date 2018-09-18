from category_builder import *


def identify_category(token):
    if token in tradestatus:
        return 'TradeStatus'

    elif token in tenor:
        return 'Tenor'

    elif token in product_group:
        return 'Product Group'

    elif token in product:
        return 'Product'

    elif token in platform:
        return 'Platform'

    elif token in new_trade:
        return 'NewTrade'

    elif token in net_client_position:
        return 'NetClientPosition'

    elif token in near_tenor_days:
        return 'NearTenorDays'

    elif token in max_future_date:
        return 'MaxFutureDate'

    elif token in marketer:
        return 'Marketer'

    elif token in local_blotter:
        return 'LocalBlotter'

    elif token in legs:
        return 'Leg'

    elif token in from_days:
        return 'FromDays'

    elif token in far_tenor_days:
        return 'FarTenorDays'

    elif token in expiration_date:
        return 'Expiry Date'

    elif token in deal_id:
        return 'Deal ID'

    elif token in deal_date:
        return 'Deal Date'

    elif token in currency_pair_group:
        return 'CurrencyPairGroup'

    elif token in currency_pair:
        return 'Currency Pair'

    elif token in crds_code:
        return 'CRDS Code'

    elif token in dealside:
        return 'Client Deal Side'

    elif token in client:
        return 'Client'

    elif token in brooker:
        return 'Broker_FXT'

    elif token in ndf_fixing_date:
        return 'NDF Fixing Date'

    #
    elif token in volume:
        return 'Volume'

    elif token in total_trades:
        return 'TotalTrades'

    elif token in std_dev_rollover_days:
        return 'StdDevRolloverDays'

    elif token in spot_price:
        return 'Spot Price Strike'

    elif token in rollover_ratio:
        return 'RolloverRatio'

    elif token in rank:
        return 'Rank'

    elif token in net_volume_ratio:
        return 'NetRolloverRatio'

    elif token in net_volume:
        return 'NetVolume'

    elif token in near_leg_volume:
        return 'NearLegVolume'

    elif token in latest_rollover:
        return 'LatestRolloverDays'

    elif token in ev:
        return 'EV'

    elif token in cc_total:
        return 'CC Total'

    elif token in cc_nonrisk:
        return 'CC NonRisk'

    elif token in cc_atrisk:
        return 'CC AtRisk'

    elif token in avg_rollover:
        return 'AverageRolloverDays'

    elif token in max_abs_net_volume:
        return 'MaxAbsNetVolume'

    else:
        return ''