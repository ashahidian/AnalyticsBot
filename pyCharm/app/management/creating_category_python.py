# documentation
# https://docs.python.org/2/tutorial/inputoutput.html

# create def for creating the category


# function to write the list of clients into the category
def create_client_rule(rule):

    f = open('/home/anisa/Documents/AnalyticsBot/pyCharm/app/rules/rules.py')

    string_rule = str(rule)
    f.write(string_rule)

#maybe receive input list of values, instead of having this file