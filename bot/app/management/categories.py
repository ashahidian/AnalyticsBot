from category_builder import *


def identify_category(token):

    if token in entries:
        return '0'

    elif token in other:
        return '0'

    elif token in tradestatus:
        return '0'

    elif token in tenor:
        return '0'

    elif token in product_group:
        return '0'

    elif token in product:
        return '0'

    elif token in platform:
        return '0'

    elif token in new_trade:
        return '0'

    elif token in net_client_position:
        return '0'

    elif token in near_tenor_days:
        return '0'

    elif token in max_future_date:
        return '0'

    elif token in marketer:
        return '0'

    elif token in local_blotter:
        return '0'

    elif token in legs:
        return '0'

    elif token in from_days:
        return '0'

    elif token in far_tenor_days:
        return '0'

    elif token in expiration_date:
        return '0'

    elif token in deal_id:
        return '0'

    elif token in deal_date:
        return '0'

    elif token in currency_pair_group:
        return '0'

    elif token in currency_pair:
        #currency_pair.append(new_token)
        return '1'

    elif token in crds_code:
        return '0'

    elif token in dealside:
        return '0'

    elif token in client:
        return '0'

    elif token in brooker:
        return '0'

    elif token in ndf_fixing_date:
        return '0'

    #
    elif token in volume:
        return '0'

    elif token in total_trades:
        return '0'

    elif token in std_dev_rollover_days:
        return '0'

    elif token in spot_price:
        return '0'

    elif token in rollover_ratio:
        return '0'

    elif token in rank:
        return '0'

    elif token in net_volume_ratio:
        return '0'

    elif token in net_volume:
        return '0'

    elif token in near_leg_volume:
        return '0'

    elif token in latest_rollover:
        return '0'

    elif token in ev:
        return '0'

    elif token in cc_total:
        return '0'

    elif token in cc_nonrisk:
        return '0'

    elif token in cc_atrisk:
        return '0'

    elif token in avg_rollover:
        return '0'

    elif token in max_abs_net_volume:
        return '0'

    else:
        return ''