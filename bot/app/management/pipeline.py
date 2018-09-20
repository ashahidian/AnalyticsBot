from bot.app.management.category_builder import *
from bot.app.processing.nlp_processing import *
from bot.app.processing.date_expressions import *
from bot.app.rules.grammar import *
from bot.app.management.sempre_query import *
from creating_rules_sempre import *
from categories import *
from bot.app.processing.synonyms import *
import subprocess


def pipeline(question):
    #currencies = ''
    #new_question = ''
    new_question_sempre = ''
    new_question_grammar = ''
    # call initial setup to gather data from database
    #setup_categories()

    # lowercase the question submitted
    lower_question = lowercase_words(question)
    #remove stop words
    q = stop_words(lower_question)

    # check synonyms for each token in question (in case its an attribute/measure/keyword)
    for i in q:
        synonym_sempre = synonym_check(i, 1)
        synonym_grammar = synonym_check(i, 0)

        # if no synonym found, check for word in categories (to make sure the word is valid)
        if synonym_grammar == '':

            category = identify_category(i)

            # if the word is not found, abort mission
            if category == '':
                exit(1)

            else:
                # add value to new formatted question
                new_question_sempre = new_question_sempre + " " + i
                new_question_grammar = new_question_grammar + " " + i

        else:
            # add value to new formatted question
            new_question_sempre = new_question_sempre + " " + str(synonym_sempre)
            new_question_grammar = new_question_grammar + " " + str(synonym_grammar)

    sg = grammar_function(new_question_grammar)
    sm = to_sempre(new_question_sempre)

    return sg, sm


    #     if i in currency_pair:
    #         split = i.split("/")
    #         new_token = split[1] + "/" + split[0]
    #         currencies = [i, new_token]
    #
    # # CHECK IF DATE WORDS IN LIST
    # expression_days_sempre = date_synonyms(new_question_sempre, 0)
    # expression_days_grammar = date_synonyms(new_question_grammar, 1)
    # expression_date_sempre = date_synonyms(new_question_sempre, 0)
    # expression_date_grammar = date_synonyms(new_question_grammar, 1)
    #
    # expression_days_sempre = str(expression_days_sempre)
    # expression_days_grammar = str(expression_days_grammar)
    # expression_date_sempre = str(expression_date_sempre)
    # expression_date_grammar = str(expression_date_grammar)
    #
    # if currencies == '':
    #     if expression_days_sempre != "0":
    #         old_question_sempre = remove_date_expressions(new_question_sempre)
    #         old_question_grammar = remove_date_expressions(new_question_grammar)
    #
    #         new_question_days_sempre = old_question_sempre
    #         new_question_days_grammar = old_question_grammar
    #         new_question_date_sempre = old_question_sempre
    #         new_question_date_grammar = old_question_grammar
    #
    #         for i in expression_days_sempre:
    #             new_question_days_sempre = new_question_days_sempre + " " + str(i)
    #             create_sempre_rule(i)
    #
    #         for i in expression_days_grammar:
    #             new_question_days_grammar = new_question_days_grammar + " " + str(i)
    #
    #         for j in expression_date_sempre:
    #             new_question_date_sempre = new_question_date_sempre + " " + str(j)
    #             create_sempre_rule(j)
    #
    #         for j in expression_date_grammar:
    #             new_question_date_grammar = new_question_date_grammar + " " + str(j)
    #             create_sempre_rule(j)
    #
    #         sg_days = grammar_function(new_question_days_grammar)
    #         sg_date = grammar_function(new_question_date_grammar)
    #         s_days = to_sempre(new_question_days_sempre)
    #         s_date = to_sempre(new_question_date_sempre)
    #
    #         #if sg_days != "":
    #         return sg_days, sg_date, s_days, s_date
    #         #else:
    #            # return sg_date, s_date
    #
    #     else:


    # else:
    #     new_question_currency_grammar = new_question_grammar.replace(currencies[0], currencies[1])
    #     new_question_currency_sempre = new_question_sempre.replace(currencies[0], currencies[1])
    #
    #     other_currency_grammar = new_question_grammar.replace(currencies[0], currencies[1])
    #     other_currency_sempre =  new_question_sempre.replace(currencies[0], currencies[1])
    #
    #     if expression_days_sempre != "0":
    #         old_question_sempre = remove_date_expressions(new_question_sempre)
    #         old_question_grammar = remove_date_expressions(new_question_grammar)
    #         old_question_currency_sempre = remove_date_expressions(other_currency_sempre)
    #         old_question_currency_grammar = remove_date_expressions(other_currency_grammar)
    #
    #         new_question_days_sempre = old_question_sempre
    #         new_question_days_grammar = old_question_grammar
    #         new_question_days_currency_sempre = old_question_currency_sempre
    #         new_question_days_currency_grammar = old_question_currency_grammar
    #
    #         new_question_date_sempre = old_question_sempre
    #         new_question_date_grammar = old_question_grammar
    #         new_question_date_currency_sempre = old_question_currency_sempre
    #         new_question_date_currency_grammar = old_question_currency_grammar
    #
    #         for i in expression_days_sempre:
    #             new_question_days_sempre = new_question_days_sempre + " " + str(i)
    #             new_question_days_currency_sempre = new_question_days_currency_sempre + " " + str(i)
    #             create_sempre_rule(i)
    #
    #         for i in expression_days_grammar:
    #             new_question_days_grammar = new_question_days_grammar + " " + str(i)
    #             new_question_days_currency_grammar = new_question_days_currency_grammar + " " + str(i)
    #
    #         for j in expression_date_sempre:
    #             new_question_date_sempre = new_question_date_sempre + " " + str(j)
    #             new_question_date_currency_sempre = new_question_date_currency_sempre + " " + str(j)
    #             create_sempre_rule(j)
    #
    #         for j in expression_date_grammar:
    #             new_question_date_grammar = new_question_date_grammar + " " + str(j)
    #             new_question_date_currency_grammar = new_question_date_currency_grammar + " " + str(j)
    #
    #         sg_days = grammar_function(new_question_days_grammar)
    #         sg_days_currency = grammar_function(new_question_days_currency_grammar)
    #         sg_date = grammar_function(new_question_date_grammar)
    #         sg_date_currency = grammar_function(new_question_date_currency_grammar)
    #         s_days = to_sempre(new_question_days_sempre)
    #         s_days_currency = to_sempre(new_question_days_currency_sempre)
    #         s_date = to_sempre(new_question_date_sempre)
    #         s_date_currency = to_sempre(new_question_date_currency_sempre)
    #
    #         return sg_days, s_days, sg_days_currency, s_days_currency, sg_date, s_date, sg_date_currency, s_date_currency
    #
    #     else:
    #         sg = grammar_function(new_question_grammar)
    #         sg_currency = grammar_function(new_question_currency_grammar)
    #         s = to_sempre(new_question_sempre)
    #         s_currency = to_sempre(new_question_currency_sempre)
    #
    #     return sg, s, sg_currency, s_currency


def to_sempre(question):
    query = (SQLQuestionMapper().convert(question))
    return query


def currency_swap(currency):
    split = currency.split("/")
    new_currency = split[1] + "/" + split[0]
    currencies = [currency, new_currency]
    return currencies

if __name__ == '__main__':
    s = pipeline("which client has highest ev?")


#    s = grammar_function("Volume test")
    print(s)

    #print(pipeline("Volume test"))