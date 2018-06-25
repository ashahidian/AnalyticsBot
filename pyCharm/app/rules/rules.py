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

        elif metric_present(question_tokens):
            print("what is client with metric value x")

        elif deal_present(question_tokens):
            print("what is deal x's client")


