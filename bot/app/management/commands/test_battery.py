import json
import subprocess
from subprocess import call, check_output

# testing SEMPRE rules
from time import sleep

# TODO
import os

from django.core.management import BaseCommand

from app.management.pipeline import pipeline
from example.settings import BASE_DIR


class Command(BaseCommand):
    question_list = [
        # "What is the CC for client Axl?",
        # "Which client has highest EV?",
        # "Clients with currency eur/usd",
        # "deal side sell",
        # "what is client JHKL 's volume?",
        # "who are the clients with rollover ratio x?",
        # "what are the deals with currency eur/usd?",
        # "who are the clients with the highest volume?",
        # "what is deal tyui expiration date?",
        # "what is client JHKL expiration",
        # "what is client JHKL deal id?",
        # "what is deal tyui client name?",
        # "which is client jhkl's deal id?",
        # "what is deal tyui volume?",
        # "which are the clients with currency eur/usd?",
        # "what is the deal with highest cc total?",
        # "what are the deals in platform x?",
        # "show me the deals of all platforms excluding x",
        # "which are the clients present in platform x?",
        # "which are the clients that are not in platform x?",
        # "what are deals with trade status new?",
        # "which clients have trade status amended?",
        # "what are the deals in a near leg?",
        # "what are clients with far leg?",
        # "what are deals with client side sell?",
        # "which clients have a client side buy?",
        # "which deals were signed in 2016?",
        # "who rollovered in the last 5 months?",
        # "which deals expire tomorrow",
        # "which clients expire tomorrow",
        # "what are clients with tenor yup",
        # "what is netvolume of client jhkl",
        # "who is marketer of client jhkl",
        # "what is the net client postition for client jhkl",
        # "which leg is client jhkl",
        # "which leg is deal tyui",
        # "what is the rank of client jhkl",
        # "what are the std dev days of client jhkl",
        # "which are the std days of client jhkl",
        # "what are the std dev rollover days of client jhkl",
        # "what is the net volume ratio of client jhkl",
        # "what is the volume of client jhkl",
        # "who is the marketer for deal tyui",
        # "what is local blotter for deal tyui",
        # "what is deal tyui local blotter",
        # "which is product group for tenor gnqo",
        # "which is tenor gnqo deal id",
        # "what is ev for tenor gnqo",
        # "marketer tenor gnqo",
        # "ev tenor gnqo"
        "give me the clients with volume higher than 25m",
        "what are the expiries for blackrock",
        "what is the CC for jp morgan",
        "what are the deal details for deal id = 12345",
        "give me the top clients with higher ev",
        "show me the trades that are going to expire tomorrow",
        "what are the currency pairs used by blackrock",
        "what are the products used by blackrock",
        "Give me the top clients with higher cc",
        "Give me the marketer with higher cc",
        "Give me the marketer with higher ev",
        "How many clients have cc higher than 25M?",
        "How many clients have volume higher than 25M?",
        "what is the CC for client jpmorgan",
        "give me platforms with higher cc",
        "give me currencies with higher cc",
        "give me products with higher volume",
        "top marketeers with ev",
        "top clients with rank",
        "deals that expire tomorrow",
        "deals that expire today"
    ]

    def handle(self, *args, **options):
        results = dict()
        for question in self.question_list:
            try:
                results[question] = pipeline(question)
            except Exception as e:
                results[question] = "Error: %s" % e.message

        with open(os.path.join(BASE_DIR, 'app', 'evaluation', 'results.out'), 'w') as f:
            f.write(json.dumps(results, indent=2))

        print("Done")






