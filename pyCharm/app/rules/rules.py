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

    if 'client' in question_tokens:
        dimension = 'Client'
    elif 'deal' in question_tokens:
        dimension = 'Deal ID'
    else:
        dimension = ''

    if dimension:

     if c:
        new_currency = currency_swap_order(c)
        nc = str(new_currency)
        # what is client currency x
        # what is deal currency x
        # what is client currency + new_currency_string
        # what is deal currency " + new_currency_string)
        print("SELECT ", dimension, " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE  Currency = ", c)
        print("SELECT ", dimension, " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE  Currency = ", nc)

    elif m:
        if 'highest' in question_tokens:
            # clients with highest metric
            print("SELECT TOP 10 ", dimension, " , ", m, " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities]")

        else:
            # what is client with metric value x
            # FINISH
            print("SELECT ", dimension, " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ", m, " = ",)

    elif p:
        if 'exclude' in question_tokens:
            # clients excluding platform x
            print("SELECT ", dimension, " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE Platform != ", p)

        else:
            # clients in platform x
            print("SELECT ", dimension, " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE Platform = ", p)

    elif t:
        # client with trade status x
        print("SELECT ", dimension, " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE TradeStatus = ", t)

    elif l:
        # client with leg x
        print("SELECT ", dimension, " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = Leg ", l)

    elif ds:
        # client with deal side x
        print("SELECT ", dimension, " FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = Client Deal Side ", ds)

    if 'client' in question_tokens:

        if n:

            if d:
                # "what is client x deal id"
                print("SELECT Deal ID FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE Client = ", n)

            elif m:
                # "what is client x metric"
                # what is deal x metric
                print("SELECT ", m, "FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ", dimension, " = ", )

        elif 'expire' in question_tokens:
            # client with expiration x
            # deal with expiration x
            # FINISH
            print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

    elif 'deal' in question_tokens:

        if deal_present(question_tokens):

            if 'client' in question_tokens:
                # what is deal x's client
                print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")
