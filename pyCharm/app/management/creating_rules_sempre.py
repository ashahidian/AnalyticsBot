# documentation
# https://docs.python.org/2/tutorial/inputoutput.html

# create def for creating the rules (for each category)


# function to write the new rules in the file
def write_rules(rule):

    f = open('/home/anisa/Documents/AnalyticsBot/sempre/analyticsBot/interface.grammar')

    string_rule = str(rule)
    f.write(string_rule)
