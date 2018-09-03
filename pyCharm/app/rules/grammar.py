import ply.lex as lex
import ply.yacc as yacc


tokens = (
    'METRIC', 'DIMENSION', 'EXCLUDE', 'TOKEN', 'MEASURE')

# Tokens
t_METRIC = r'Volume|Transaction Number|TotalTrades'
t_DIMENSION = r'TradeStatus|Tenor|ProductKey'
t_TOKEN = r'[a-zA-Z_0-9]+'


def t_EXCLUDE(t):
    r'exclude'
    return t


def t_MEASURE(t):
    r'highest'
    return t


# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lex.lex()

# dictionary of names (for storing variables)
names = {}


def p_statement_single(p):
    ''' statement : METRIC TOKEN
                | DIMENSION TOKEN '''

    p[0] = "".join(('SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[1], ' = ', p[2]))


def p_statement_single_second(p):
    ''' statement : TOKEN METRIC
                | TOKEN DIMENSION '''
    p[0] = "".join(('SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[2], ' = ', p[1]))


def p_statement_exclude(p):
    ''' statement : METRIC TOKEN EXCLUDE
                | DIMENSION TOKEN EXCLUDE '''
    p[0] = "".join(('SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[1], ' != ', p[2]))


def p_statement_exclude_first(p):
    ''' statement : EXCLUDE METRIC TOKEN
                | EXCLUDE DIMENSION TOKEN '''
    p[0] = "".join(('SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[2], ' != ', p[3]))


def p_statement_multiple_token_second(p):
    ''' statement : DIMENSION TOKEN METRIC
                | METRIC TOKEN DIMENSION
                | DIMENSION TOKEN DIMENSION '''
    p[0] = "".join(('SELECT ', p[3], ' FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[1], ' = ', p[2]))


def p_statement_multiple_token_third(p):
    ''' statement : DIMENSION METRIC TOKEN
                | METRIC DIMENSION TOKEN
                | DIMENSION DIMENSION TOKEN '''
    p[0] = "".join(('SELECT ', p[1], ' FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[2], ' = ', p[3]))


def p_statement_multiple_token_four(p):
    ''' statement : DIMENSION TOKEN METRIC TOKEN
                | METRIC TOKEN DIMENSION TOKEN
                | DIMENSION TOKEN DIMENSION TOKEN'''
    p[0] = "".join(('SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[1], ' = ', p[2],
                    ' AND ', p[3], ' = ', p[4]))


def p_statement_measure(p):
    ''' statement : DIMENSION MEASURE METRIC
                | METRIC MEASURE DIMENSION
                | DIMENSION MEASURE DIMENSION '''
    p[0] ="".join(('SELECT TOP 10 ', p[1], ', ', p[3], ' FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] '))


def p_error(p):
    print(p)
    print("Syntax error at '%s'" % p.value)


yacc.yacc()


try:
    s = 'Tenor highest Volume'
except EOFError:
    pass
r = yacc.parse(s)
print(r)