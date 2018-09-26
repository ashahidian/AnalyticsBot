from app.management.sempre_query import *
from app.natural_language.date_expressions import *
from app.natural_language.synonyms import *


def to_sempre(question):
    query = SQLQuestionMapper().convert(question)

    return query


def currency_swap(currency):
    split = currency.split("/")
    new_currency = split[1] + "/" + split[0]
    # currencies = [currency, new_currency]

    return new_currency


def get_max_match(question_tokens):
    one_grams = ngrams(question_tokens, 1)
    two_grams = ngrams(question_tokens, 2)
    three_grams = ngrams(question_tokens, 3)
    four_grams = ngrams(question_tokens, 4)
    match = ''
    words_grammar = []
    words_sempre = []
    words_with_synonym = []
    found = 0

    for grams in one_grams:

        if grams != '':

            if grams[0] not in words_with_synonym:

                actual_word = synonym_check(grams[0], 0)

                if actual_word != '':

                    words_grammar.append(synonym_check(grams[0], 0))
                    words_sempre.append(synonym_check(grams[0], 1))

                    match = match + " " + grams[0]
                    words_with_synonym.append(grams[0])
                    found = 1

    for grams in two_grams:

        if grams != '':

            if grams[0] not in words_with_synonym and grams[1] not in words_with_synonym:

                actual_word = synonym_check(grams[0] + " " + grams[1], 0)

                if actual_word != '':

                    words_grammar.append(synonym_check(grams[0] + " " + grams[1], 0))
                    words_sempre.append(synonym_check(grams[0] + " " + grams[1], 1))

                    match = match + " " + grams[0] + " " + grams[1]
                    words_with_synonym.extend((grams[0], grams[1]))
                    found = 1

    for grams in three_grams:
        if grams != '':

            if grams[0] not in words_with_synonym and grams[1] not in words_with_synonym and grams[2] not in words_with_synonym:

                actual_word = synonym_check(grams[0] + " " + grams[1] + " " + grams[2], 0)

                if actual_word != '':

                    words_grammar.append(synonym_check(grams[0] + " " + grams[1] + " " + grams[2], 0))
                    words_sempre.append(synonym_check(grams[0] + " " + grams[1] + " " + grams[2], 1))

                    match = match + " " + grams[0] + " " + grams[1] + " " + grams[2]
                    words_with_synonym.extend((grams[0], grams[1], grams[2]))
                    found = 1

    for grams in four_grams:

        if grams != '':

            if grams[0] not in words_with_synonym and grams[1] not in words_with_synonym and grams[2] not in words_with_synonym and grams[4] not in words_with_synonym:

                actual_word = synonym_check(
                    grams[0] + " " + grams[1] + " " + grams[2] + " " + grams[3], 0)

                if actual_word != '':

                    words_grammar = words_grammar + " " + synonym_check(
                        grams[0] + " " + grams[1] + " " + grams[2] + " " + grams[3], 0)
                    words_sempre = words_sempre + " " + synonym_check(
                        grams[0] + " " + grams[1] + " " + grams[2] + " " + grams[3], 1)

                    match = match + " " + grams[0] + " " + grams[1] + " " + grams[2] + " " + grams[3]
                    words_with_synonym.extend((grams[0], grams[1], grams[2], grams[3]))
                    found = 1

    if found == 0:
        return ''
    else:
        return match, words_grammar, words_sempre


def get_date_match(question_tokens):
    one_grams = ngrams(question_tokens, 1)
    two_grams = ngrams(question_tokens, 2)
    three_grams = ngrams(question_tokens, 3)
    match = ''
    days = []
    date = []
    words_with_date = []
    found = 0

    for grams in three_grams:

        if grams != '':
            if grams[0] not in words_with_date and grams[1] not in words_with_date and grams[2] not in words_with_date:
                aux = " ".join(grams)
                actual_word = date_synonyms(aux, 0)
                #actual_word = date_synonyms(list(grams[0] + " " + grams[1] + " " + grams[2]), 0)

                if actual_word != '':

                    days.append(date_synonyms(aux, 0))
                    date.append(date_synonyms(aux, 1))

                    match = match + " " + grams[0] + " " + grams[1] + " " + grams[2]
                    words_with_date.extend((grams[0], grams[1], grams[2]))
                    found = 1

    for grams in two_grams:
        if grams[0] not in words_with_date and grams[1] not in words_with_date:
            if grams != '':

                aux = " ".join(grams)
                actual_word = date_synonyms(aux, 0)
                # actual_word = date_synonyms(list(grams[0] + " " + grams[1]), 0)

                if actual_word != '':
                    days.append(date_synonyms(aux, 0))
                    date.append(date_synonyms(aux, 1))

                    match = match + " " + grams[0] + " " + grams[1]
                    words_with_date.extend((grams[0], grams[1]))
                    found = 1

    for grams in one_grams:
        if grams != '':
            if grams[0] not in words_with_date:

                aux = " ".join(grams)
                actual_word = date_synonyms(aux, 0)

                if actual_word != '':

                    days.append(date_synonyms(aux, 0))
                    print(days)
                    date.append(date_synonyms(aux, 1))
                    print(date)

                    match = match + " " + grams[0]
                    words_with_date.append(grams[0])
                    found = 1

    if found == 0:
        return ''
    else:
        return match, days, date


def date_question_prep(matched_synonyms, og_question):
    date_ready_q = []

    for w in og_question:

        if w not in matched_synonyms:

            date_ready_q.append(str(w))

    return date_ready_q

