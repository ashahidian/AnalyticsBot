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

