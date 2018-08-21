
from aux_rules import *


def read_sentence(question_tokens):
    n = name_present(question_tokens)
    c = currency_present(question_tokens)
    m = metric_present(question_tokens)
    d = deal_present(question_tokens)
    p = platform_present(question_tokens)
    t = tradestatus_present(question_tokens)
    l = leg_present(question_tokens)
    ds = dealside_present(question_tokens)
    ccd = crdscode_present(question_tokens)

    #dimension = [ccd, deal_id, client]
    # metric: currency pair, platform, (expiration date), (trade status), (leg), (deal side)
