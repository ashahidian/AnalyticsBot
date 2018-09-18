import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'MEASURE', 'ATTRIBUTE', 'EXCLUDE', 'TOKEN', 'COMPARE', 'DATE')

# Tokens
t_MEASURE = r'Volume|TotalTrades|StdDevRolloverDays|Spot\sPrice\sStrike|RolloverRatio|Rank|NetVolumeRatio|NetVolume' \
            r'NearLegVolume|LatestRolloverDays|EV|CC\sTotal|CC\sNonRisk|CC\sAtRisk|AverageRolloverDays|MaxAbsNetVolume'

t_ATTRIBUTE = r'TradeStatus|Tenor|Product\sGroup|Product|Platform|NewTrade|NetClientPosition|NearTenorDays|' \
              r'MaxFutureDate|Marketer|LocalBlotter|Leg|FromDays|FarTenorDays|Expiry\sDate|Deal\sID|Deal Date' \
              r'|CurrencyPairGroup|Currency\sPair|CRDSCode|Client\sDeal\sSide|Client' \
              r'|Broker_FXT|NDF|Fixing\sDate'

t_TOKEN = r'[a-zA-Z_0-9]+'

t_DATE = r'(next|last)\s([0-9\s]*)(day|week|year|quarter) | ([0-9]{4}) | yesterday | tomorrow | this year '


def t_EXCLUDE(t):
    r'exclude'
    return t


def t_COMPARE(t):
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
    ''' statement : MEASURE TOKEN
                | ATTRIBUTE TOKEN '''

    p[0] = "".join(('SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[1], ' = ', p[2]))


def p_statement_single_second(p):
    ''' statement : TOKEN MEASURE
                | TOKEN ATTRIBUTE '''
    p[0] = "".join(('SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[2], ' = ', p[1]))


def p_statement_exclude(p):
    ''' statement : MEASURE TOKEN EXCLUDE
                | ATTRIBUTE TOKEN EXCLUDE '''
    p[0] = "".join(('SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[1], ' != ', p[2]))


def p_statement_exclude_middle(p):
    ''' statement : MEASURE EXCLUDE TOKEN
                | ATTRIBUTE EXCLUDE TOKEN '''
    p[0] = "".join(('SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[1], ' != ', p[3]))


def p_statement_exclude_first(p):
    ''' statement : EXCLUDE MEASURE TOKEN
                | EXCLUDE ATTRIBUTE TOKEN '''
    p[0] = "".join(('SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[2], ' != ', p[3]))


def p_statement_exclude_large(p):
    ''' statement : MEASURE EXCLUDE ATTRIBUTE TOKEN
                | ATTRIBUTE EXCLUDE MEASURE TOKEN
                | ATTRIBUTE EXCLUDE ATTRIBUTE TOKEN
                | MEASURE EXCLUDE MEASURE TOKEN '''
    p[0] = "".join(
        ('SELECT ', p[1], ' FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[3], ' != ', p[4]))


def p_statement_multiple_token_second(p):
    ''' statement : ATTRIBUTE TOKEN MEASURE
                | MEASURE TOKEN ATTRIBUTE
                | ATTRIBUTE TOKEN ATTRIBUTE '''
    p[0] = "".join(
        ('SELECT ', p[3], ' FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[1], ' = ', p[2]))


def p_statement_multiple_token_third(p):
    ''' statement : ATTRIBUTE MEASURE TOKEN
                | MEASURE ATTRIBUTE TOKEN
                | ATTRIBUTE ATTRIBUTE TOKEN '''
    p[0] = "".join(
        ('SELECT ', p[1], ' FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[2], ' = ', p[3]))


def p_statement_multiple_token_four(p):
    ''' statement : ATTRIBUTE TOKEN MEASURE TOKEN
                | MEASURE TOKEN ATTRIBUTE TOKEN
                | ATTRIBUTE TOKEN ATTRIBUTE TOKEN'''
    p[0] = "".join(('SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[1], ' = ', p[2],
                    ' AND ', p[3], ' = ', p[4]))


def p_statement_compare(p):
    ''' statement : ATTRIBUTE COMPARE MEASURE
                | MEASURE COMPARE ATTRIBUTE
                | ATTRIBUTE COMPARE ATTRIBUTE '''
    p[0] = "".join(
        ('SELECT TOP 10 ', p[3], ', ', p[1], ' FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] '))


def p_statement_time(p):
    '''statement : ATTRIBUTE DATE'''

    p[0] = "".join(
        ('SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[1], ' = ', p[2]))


def p_statement_attribute_time(p):
    '''statement : ATTRIBUTE ATTRIBUTE DATE
                | MEASURE ATTRIBUTE DATE'''

    p[0] = "".join(
        ('SELECT ', p[1], ' FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[2], ' = ', p[3]))


def p_statement_time_time(p):
    '''statement : ATTRIBUTE DATE DATE'''

    p[0] = "".join(
        ('SELECT * FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[1], ' >= ', p[2], ' AND ',
         p[1], ' <= ', p[3]))


def p_statement_attribute_time_time(p):
    '''statement : ATTRIBUTE ATTRIBUTE DATE DATE
                | MEASURE ATTRIBUTE DATE DATE'''

    p[0] = "".join(
        ('SELECT ', p[1], ' FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities] WHERE ', p[2], ' >= ', p[3],
         ' AND ',
         p[2], ' <= ', p[4]))


def p_error(p):
    print(p)
    print("Syntax error at '%s'" % p.value)


yacc.yacc()
# TotalTrades
# TradeStatus
# Volume
# Tenor
try:
    s = 'Broker_FXT x'
except EOFError:
    pass
r = yacc.parse(s)
print(r)
