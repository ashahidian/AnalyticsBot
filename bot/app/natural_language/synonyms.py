from synonyms_lists import *


def synonym_check(word, type):

    # type 0 = semantic grammar
    # type 1 = SEMPRE

    if word in exclude_synonyms:
        return 'exclude'

    elif word in higher_synonyms:
        return 'highest'

    elif word in expire_synonyms:
        if type == 0:
            return 'expiry date'
        elif type == 1:
            return 'expire'

    elif word in crdscode_synonyms:
        return 'crdscode'

    elif word in client_deal_side_synonyms:
        if type == 0:
            return 'client deal side'
        elif type == 1:
            return 'clientdeal'

    elif word in client_synonyms:
        return 'client'

    elif word in deal_date_synonyms:
        if type == 0:
            return 'deal date'
        elif type == 1:
            return 'date'

    elif word in deal_id_synonyms:
        if type == 0:
            return 'deal id'
        elif type == 1:
            return 'deal'

    elif word in std_dev_rollover_days_synonyms:
        if type == 0:
            return 'stddevrolloverdays'
        elif type == 1:
            return 'stddevrollover'

    elif word in rollover_synonyms:
        if type == 0:
            return 'latestrolloverdays'
        elif type == 1:
            return 'rollover'

    elif word in rollover_ratio_synonyms:
        return 'rolloverratio'

    elif word in average_rollover_synonyms:
        if type == 0:
            return 'averagerolloverdays'
        elif type == 1:
            return 'avgrollover'

    elif word in total_trades_synonyms:
        return 'totaltrades'

    elif word in spot_price_synonyms:
        if type == 0:
            return 'spot price strike'
        elif type == 1:
            return 'spotpricestrike'

    elif word in rank_synonyms:
        return 'rank'

    elif word in net_volume_ratio_synonyms:
        return 'netvolumeratio'

    elif word in net_volume_synonyms:
        return 'netvolume'

    elif word in near_leg_volume_synonyms:
        return 'nearlegvolume'

    elif word in volume_synonyms:
        return 'volume'

    elif word in ev_synonyms:
        return 'ev'

    elif word in cc_total_synonyms:
        if type == 0:
            return 'cc total'
        elif type == 1:
            return 'cctotal'

    elif word in cc_non_risk_synonyms:
        if type == 0:
            return 'cc nonrisk'
        elif type == 1:
            return 'ccnonrisk'

    elif word in cc_at_risk_synonyms:
        if type == 0:
            return 'cc atrisk'
        elif type == 1:
            return 'ccatrisk'

    elif word in max_abs_net_volume_synonyms:
        return 'maxabsnetvolume'

    elif word in trade_status_synonyms:
        return 'tradestatus'

    elif word in tenor_synonyms:
        return 'tenor'

    elif word in product_group_synonyms:
        if type == 0:
            return 'product group'
        elif type == 1:
            return 'productgroup'

    elif word in product_synonyms:
        return 'product'

    elif word in platform_synonyms:
        return 'platform'

    elif word in net_client_position_synonyms:
        return 'netclientposition'

    elif word in near_tenor_days_synonyms:
        return 'neartenordays'

    elif word in max_future_date_synonyms:
        return 'maxfuturedate'

    elif word in marketer_synonyms:
        return 'marketer'

    elif word in local_blotter_synonyms:
        return 'localblotter'

    elif word in leg_synonyms:
        return 'leg'

    elif word in from_days_synonyms:
        return 'fromdays'

    elif word in far_tenor_days_synonyms:
        return 'fartenordays'

    elif word in currency_pair_group_synonyms:
        return 'currencypairgroup'

    elif word in currency_synonyms:
        if type == 0:
            return 'currency pair'
        elif type == 1:
            return 'currency'

    elif word in broker_fxt_synonyms:
        if type == 0:
            return 'broker_fxt'
        elif type == 1:
            return 'broker'

    elif word in ndf_fixing_date_synonyms:
        if type == 0:
            return 'ndf fixing date'
        elif type == 1:
            return 'ndfdate'

    else:
        return ''
