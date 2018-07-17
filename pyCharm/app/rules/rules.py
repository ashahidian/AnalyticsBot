from pyCharm.app.management.categories import *


def name_present(question_tokens):

    for w in question_tokens:
        if w in names:
            return w


def currency_present(question_tokens):

    for w in question_tokens:
        if w in currencies:
            return w


def currency_swap_order(currency):
    currency_one = currency[:3]
    currency_two = currency[-3:]
    new_currency = str(currency_two) + "/" + str(currency_one)
    return new_currency


def deal_present(question_tokens):

    for w in question_tokens:
        if w in deals:
            return w


def metric_present(question_tokens):

    for w in question_tokens:
        if w in metrics:
            return w


def platform_present(question_tokens):

    for w in question_tokens:
        if w in platforms:
            return w


def tradestatus_present(question_tokens):
    for w in question_tokens:
        if w in tradestatus:
            return w


def leg_present(question_tokens):
    for w in question_tokens:
        if w in legs:
            return w


def dealside_present(question_tokens):
    for w in question_tokens:
        if w in dealside:
            return w


def read_sentence(question_tokens):
    n = name_present(question_tokens)
    c = currency_present(question_tokens)
    m = metric_present(question_tokens)
    d = deal_present(question_tokens)
    p = platform_present(question_tokens)
    t = tradestatus_present(question_tokens)
    l = leg_present(question_tokens)
    ds = dealside_present(question_tokens)

    if 'client' in question_tokens:

        if n:

            if d:
                # "what is client x deal id"
                print("SELECT Deal ID FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE Client = ", n)

            elif m:
                # "what is client x metric"
                print("SELECT ", m, "FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE  Client =", n)

        elif c:
            new_currency = currency_swap_order(c)
            nc = str(new_currency)
            # what is client currency x
            # what is client currency + new_currency_string
            print("SELECT Client FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE  Currency =", c)
            print("SELECT Client FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE  Currency =", nc)

        elif m:
            if 'highest' in question_tokens:
                # clients with highest metric
                print("SELECT TOP 10 ", c, " , ", m, " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunit ies]")

            else:
                # what is client with metric value x
                # FINISH
                print("SELECT Client FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ", m, " = ",)

        elif 'expire' in question_tokens:
            # client with expiration x
            # FINISH
            print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

        elif p:
            if 'exclude' in question_tokens:
                # clients excluding platform x
                print("SELECT Client FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE Platform != ", p)

            else:
                # clients in platform x
                print("SELECT Client FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE Platform = ", p)

        elif t:
            # client with trade status x
            print("SELECT Client FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE TradeStatus = ", t)

        elif l:
            # client with leg x
            print("SELECT Client FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = Leg ", l)

        elif ds:
            # client with deal side x
            print("SELECT Client FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = Client Deal Side ", ds)

    elif 'deal' in question_tokens:

        if deal_present(question_tokens):

            if 'client' in question_tokens:
                # what is deal x's client
                print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

            elif 'expire' in question_tokens:
                # when does deal x expire
                print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

            elif metric_present(question_tokens):
                # what is deal x metric
                print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

        elif currency_present(question_tokens):
            new_currency = currency_swap_order(currency_present(question_tokens))
            new_currency_string = str(new_currency)
            # what is deal currency x
            print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")
            # what is deal currency " + new_currency_string)
            print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

        elif metric_present(question_tokens):
            if 'highest' in question_tokens:
                # deal with highest metric
                print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

            else:
                # what is deal with metric value x
                print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

        elif 'expire' in question_tokens:
            # deal with expiration x
            print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

        elif 'platform' in question_tokens:
            if 'exclude' in question_tokens:
                # deals excluding platform x
                print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

            else:
                # deals in platform x
                print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

        elif 'trade status' in question_tokens:
            # deal with trade status x
            print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

        elif 'leg' in question_tokens:
            # deals with leg x
            print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

        elif 'deal side' in question_tokens:
            # deals with deal side x
            print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")