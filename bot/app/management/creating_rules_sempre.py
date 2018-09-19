# documentation
# https://docs.python.org/2/tutorial/inputoutput.html

# create def for creating the rules (for each category)


# function to write the new rules in the file
def write_rules(rule):

    f = open('/home/anisa/Documents/AnalyticsBot/sempre/analyticsBot/interface.grammar', "a")

    string_rule = str(rule)
    f.write(string_rule)
    return string_rule


def create_time_rule(time_expression):
    return "\n(rule $Date (" + time_expression + ") (ConstantFn (string '" + time_expression + "')))"


def create_sempre_rule(time_expression):
    rule = create_time_rule(time_expression)
    write_rules(rule)


#if __name__ == '__main__':
#    create_rule("2-03-1998")

#    print("testing")