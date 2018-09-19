from bot.app.management.category_builder import *
from bot.app.processing.nlp_processing import *
from bot.app.processing.date_expressions import *
from bot.app.rules.grammar import *
from bot.app.management.sempre_query import *
from creating_rules_sempre import *
from categories import *
import subprocess


def pipeline(question):
    # call initial setup to gather data from database
    #setup_categories()

    lower_question = lowercase_words(question)
    q = stop_words(lower_question)
    new_question = ' '.join(q)

    # CHECK IF DATE WORDS IN LIST
    expression_days = date_synonyms(new_question, 0)
    expression_date = date_synonyms(new_question, 1)

    expression_days = str(expression_days)
    expression_date = str(expression_date)

    if expression_days != "0":
        old_question = remove_date_expressions(new_question)

        new_question_days = old_question
        new_question_date = old_question

        for i in expression_days:
            new_question_days = new_question_days + " " + str(i)
            create_sempre_rule(i)

        for j in expression_date:
            new_question_date = new_question_date + " " + str(j)
            create_sempre_rule(j)

        sg_days = grammar_function(new_question_days)
        sg_date = grammar_function(new_question_date)
        s_days = to_sempre(new_question_days)
        s_date = to_sempre(new_question_date)

        if sg_days != "":
            return sg_days, s_days
        else:
            return sg_date, s_date

    else:
        sg = grammar_function(new_question)
        s = to_sempre(new_question)

    return sg, s


#def to_semantic_grammar(question):
#    lex.lex()
#    yacc.yacc()

#    query = yacc.parse(question)

#    return query


def to_sempre(question):
    query = (SQLQuestionMapper().convert(question))
    return query


if __name__ == '__main__':
    s = pipeline("Volume test")
#    s = grammar_function("Volume test")
    print(s)

    #print(pipeline("Volume test"))