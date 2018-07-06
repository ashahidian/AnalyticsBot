from categories import names, currencies, deals, metrics
import categories


def name_present(question_tokens):

    for w in question_tokens:
        if w in names:
            return True, w


def currency_present(question_tokens):

    for w in question_tokens:
        if w in currencies:
            return True, w


def deal_present(question_tokens):

    for w in question_tokens:
        if w in deals:
            return True, w


def metric_present(question_tokens):

    for w in question_tokens:
        if w in metrics:
            return True, w


def read_sentence(question_tokens):
    if 'client' in question_tokens:

        if name_present(question_tokens):
            if deal_present(question_tokens):
                print("what is client x deal id")

            elif metric_present(question_tokens):
                print("what is client x metric")

        elif currency_present(question_tokens):
            print ("what is client currency x")

        elif metric_present(question_tokens):
            if 'highest' in question_tokens:
                print("clients with highest metric")
            else:
                print("what is client with metric value x")

        elif 'expire' in question_tokens:
            print("client with expiration x")

        elif 'platform' in question_tokens:
            if 'exclude' in question_tokens:
                print("clients excluding platform x")
            else:
                print("clients in platform x")

        elif 'trade status' in question_tokens:
            print("client with trade status x")

        elif 'leg' in question_tokens:
            print("client with leg x")

        elif 'deal side' in question_tokens:
            print("client with deal side x")

    elif 'deal' in question_tokens:

        if deal_present(question_tokens):

            if 'client' in question_tokens:
                print("what is deal x's client")

            elif 'expire' in question_tokens:
                print("when does deal x expire")

            elif metric_present(question_tokens):
                print ("what is deal x metric")

        elif currency_present(question_tokens):
            print ("what is deal currency x")

        elif metric_present(question_tokens):
            if 'highest' in question_tokens:
                print("deal with highest metric")
            else:
                print("what is deal with metric value x")

        elif 'expire' in question_tokens:
            print("deal with expiration x")

        elif 'platform' in question_tokens:
            if 'exclude' in question_tokens:
                print("deals excluding platform x")
            else:
                print("deals in platform x")

        elif 'trade status' in question_tokens:
            print("deal with trade status x")

        elif 'leg' in question_tokens:
            print("deals with leg x")

        elif 'deal side' in question_tokens:
            print("deals with deal side x")