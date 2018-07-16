from pyCharm.app.management.categories import names, currencies, deals, metrics


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


def read_sentence(question_tokens):
    if 'client' in question_tokens:

        if name_present(question_tokens):
            if deal_present(question_tokens):
                # "what is client x deal id"
                print("SELECT Deal ID FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE Client =")

            elif metric_present(question_tokens):
                # "what is client x metric"
                print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE  Client =")

        elif currency_present(question_tokens):
            new_currency = currency_swap_order(currency_present(question_tokens))
            new_currency_string = str(new_currency)
            # what is client currency x
            # what is client currency + new_currency_string
            print("SELECT Client FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE  Currency =")

        elif metric_present(question_tokens):
            if 'highest' in question_tokens:
                # clients with highest metric
                print("SELECT TOP 10 , FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities]")

            else:
                # what is client with metric value x
                print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

        elif 'expire' in question_tokens:
            # client with expiration x
            print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

        elif 'platform' in question_tokens:
            if 'exclude' in question_tokens:
                # clients excluding platform x
                print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

            else:
                # clients in platform x
                print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

        elif 'trade status' in question_tokens:
            # client with trade status x
            print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

        elif 'leg' in question_tokens:
            # client with leg x
            print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

        elif 'deal side' in question_tokens:
            # client with deal side x
            print("SELECT FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE = ")

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