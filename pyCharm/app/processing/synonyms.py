from synonyms_lists import *


def synonym_check(word, type):
    # type 0 = semantic grammar
    # type 1 = SEMPRE

    if word in exclude_synonyms:
        return 'exclude'

    elif word in higher_synonyms:
        return 'higher'

    elif word in expire_synonyms:
        if type == 0:
            return 'Expiry Date'
        elif type == 1:
            return 'expire'

    elif word in crdscode_synonyms:
        if type == 0:
            return 'CRDSCode'
        elif type == 1:
            return 'crdscode'

    elif word in client_synonyms:
        if type == 0:
            'Client'
        elif type == 1:
            return 'client'

    elif word in currency_synonyms:
        if type == 0:
            return 'Currency Pair'
        elif type == 1:
            return 'currency'

    elif word in deal_id_synonyms:
        if type == 0:
            return 'Deal ID'
        elif type == 1:
            return 'deal'

    elif word in deal_date_synonyms:
        if type == 0:
            return 'Deal Date'
        elif type == 1:
            return 'date'

    elif word in std_dev_rollover_days_synonyms:
        if type == 0:
            return 'StdDevRolloverDays'
        elif type == 1:
            return 'stddevrollover'

    elif word in rollover_synonyms:
        if type == 0:
            return 'LatestRolloverDays'
        elif type == 1:
            return 'rollover'

    elif word in rollover_ratio_synonyms:
        if type == 0:
            return 'RolloverRatio'
        elif type == 1:
            return 'rolloverratio'

    elif word in average_rollover_synonyms:
        if type == 0:
            return 'AverageRolloverDays'
        elif type == 1:
            return 'avgrollover'

    elif word in client_deal_side_synonyms:
        if type == 0:
            return 'Client Deal Side'
        elif type == 1:
            return 'clientdeal'

    elif word in volume_synonyms:
        if type == 0:
            return 'Volume'
        elif type == 1:
            return 'volume'

    elif word in total_trades_synonyms:
        if type == 0:
            return 'TotalTrades'
        elif type == 1:
            return 'totaltrades'

    elif word in spot_price_synonyms:
        if type == 0:
            return 'Spot Price Strike'
        elif type == 1:
            return 'spotpricestrike'

    elif word in rank_synonyms:
        if type == 0:
            return 'Rank'
        elif type == 1:
            return 'rank'

    elif word in net_volume_ratio_synonyms:
        if type == 0:
            return 'NetVolumeRatio'
        elif type == 1:
            return 'netvolumeratio'

    elif word in net_volume_synonyms:
        if type == 0:
            return 'NetVolume'
        elif type == 1:
            return 'netvolume'

    elif word in near_leg_volume_synonyms:
        if type == 0:
            return 'NearLegVolume'
        elif type == 1:
            return 'nearlegvolume'

    elif word in ev_synonyms:
        if type == 0:
            return 'EV'
        elif type == 1:
            return 'ev'

    elif word in cc_total_synonyms:
        if type == 0:
            return 'CC Total'
        elif type == 1:
            return 'cctotal'

    elif word in cc_non_risk_synonyms:
        if type == 0:
            return 'CC NonRisk'
        elif type == 1:
            return 'ccnonrisk'

    elif word in cc_at_risk_synonyms:
        if type == 0:
            return 'CC AtRisk'
        elif type == 1:
            return 'ccatrisk'

    elif word in max_abs_net_volume_synonyms:
        if type == 0:
            return 'MaxAbsNetVolume'
        elif type == 1:
            return 'maxabsnetvolume'

    elif word in trade_status_synonyms:
        if type == 0:
            return 'TradeStatus'
        elif type == 1:
            return 'tradestatus'

    elif word in tenor_synonyms:
        if type == 0:
            return 'Tenor'
        elif type == 1:
            return 'tenor'

    elif word in product_group_synonyms:
        if type == 0:
            return 'Product Group'
        elif type == 1:
            return 'productgroup'

    elif word in product_synonyms:
        if type == 0:
            return 'Product'
        elif type == 1:
            return 'product'

    elif word in platform_synonyms:
        if type == 0:
            return 'Platform'
        elif type == 1:
            return 'platform'

    elif word in new_trade_synonyms:
        if type == 0:
            return 'NewTrade'
        elif type == 1:
            return 'newtrade'

    elif word in net_client_position_synonyms:
        if type == 0:
            return 'NetClientPosition'
        elif type == 1:
            return 'netclientposition'

    elif word in near_tenor_days_synonyms:
        if type == 0:
            return 'NearTenorDays'
        elif type == 1:
            return 'neartenordays'

    elif word in max_future_date_synonyms:
        if type == 0:
            return 'MaxFutureDate'
        elif type == 1:
            return 'maxfuturedate'

    elif word in marketer_synonyms:
        if type == 0:
            return 'Marketer'
        elif type == 1:
            return 'marketer'

    elif word in local_blotter_synonyms:
        if type == 0:
            return 'LocalBlotter'
        elif type == 1:
            return 'localblotter'

    elif word in leg_synonyms:
        if type == 0:
            return 'Leg'
        elif type == 1:
            return 'leg'

    elif word in from_days_synonyms:
        if type == 0:
            return 'FromDays'
        elif type == 1:
            return 'fromdays'

    elif word in far_tenor_days_synonyms:
        if type == 0:
            return 'FarTenorDays'
        elif type == 1:
            return 'fartenordays'

    elif word in currency_pair_group_synonyms:
        if type == 0:
            return 'CurrencyPairGroup'
        elif type == 1:
            return 'currencypairgroup'

    elif word in brooker_fxt_synonyms:
        if type == 0:
            return 'Brooker_FXT'
        elif type == 1:
            return 'brooker'

    elif word in ndf_fixing_date_synonyms:
        if type == 0:
            return 'NDF Fixing Date'
        elif type == 1:
            return 'ndfdate'

    else:
        return word
