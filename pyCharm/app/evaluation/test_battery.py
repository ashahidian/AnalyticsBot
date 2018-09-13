import subprocess
from subprocess import call, check_output

# testing SEMPRE rules
from time import sleep

# ultimas duas questoes temporais precisam de ser trabalhadas
# pergunta 7 e 9 tambem precisa de tratamento
# TODO

question_list = [
    "what is client x 's volume?",
    "who are the clients with rollover ratio x?",
    "what are the deals with currency eur/usd?",
    "who are the clients with the highest volume?",
    "what is deal x expiration date?",
    "what is client x expiration date?",
    "what is x expiration date?",
    "what is client x deal id?",
    "what is deal x client name?",
    "which is x's deal id?",
    "what is deal x volume?",
    "which are the clients with currency eur/usd?",
    "what is the deal with highest cc total?",
    "what are the deals in platform x?",
    "show me the deals of all platforms excluding x",
    "which are the clients present in platform x?",
    "which are the clients that are not in platform x?",
    "what are deals with trade status new?",
    "which clients have trade status amended?",
    "what are the deals in a near leg?",
    "what are clients with far leg?",
    "what are deals with client side sell?",
    "which clients have a client side buy?",
    "which deals were signed in 2016?",
    "who rollovered in the last 5 months?"
]


def call_shell():
    ps = subprocess.Popen('cd /home/anisa/Documents/AnalyticsBot/sempre && ./run @mode=simple -Grammar.inPaths /home/anisa/Documents/AnalyticsBot/sempre/analyticsBot/interface.grammar',
                         shell=True, stdin=subprocess.PIPE, stdout=open("/tmp/output", 'w'), bufsize=10)

    sleep(1)
    for q in question_list:
        ps.stdin.write(q + "\n")
    sleep(2)
    with open("/tmp/output", "r") as f:
        print(f.read())
