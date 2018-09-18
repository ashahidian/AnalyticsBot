from bot.app.management.category_builder import *
from bot.app.processing.nlp_processing import *
from bot.app.processing.date_expressions import *
from categories import *
import subprocess


def pipeline(question):
    # call initial setup to gather data from database
    #setup_categories()
    lower_question = lowercase_words(question)
    pure_q = stop_words(lower_question)

    new_question = ' '.join(pure_q)

    expression_days = date_synonyms(new_question, 0)
    expression_date = date_synonyms(new_question, 1)

    expression = str(expression_days)

    if expression != " ":
        old_question = remove_date_expressions(new_question)

        new_question_days = old_question
        new_question_date = old_question

        for i in expression_days:
            new_question_days = new_question_days + " " + str(i)

        for j in expression_date:
            new_question_date = new_question_date + " " + str(j)

        sg_days = to_semantic_grammar(new_question_days)
        sg_date = to_semantic_grammar(new_question_date)
        s_days = to_sempre(new_question_days)
        s_date = to_sempre(new_question_date)

        if sg_days != "":
            return sg_days, s_days
        else:
            return sg_date, s_date

    else:

        to_semantic_grammar(new_question)
        to_sempre(new_question)


    return





def to_semantic_grammar(question):



def to_sempre(question):


# if __name__ == '__main__':
    #print(new_question)