# documentation
# https://docs.python.org/2/tutorial/inputoutput.html


# function to write the rules in the file
def write_rules(rule):

    f = open('/home/anisa/Documents/AnalyticsBot/sempre/analyticsBot/interface.grammar', "a")

    string_rule = str(rule)
    f.write(string_rule)
    return string_rule

# create time rule when receiving a time expression
def create_time_rule(time_expression):
    return "\n(rule $Date (" + str(time_expression) + ") (ConstantFn (string '" + str(time_expression) + "')))"


def create_sempre_rule(time_expression):
    rule = create_time_rule(time_expression)
    write_rules(rule)
