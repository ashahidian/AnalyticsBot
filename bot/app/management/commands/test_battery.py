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
        "what is client JHKL 's volume?",
        "who are the clients with rollover ratio x?",
        "what are the deals with currency eur/usd?",
        "who are the clients with the highest volume?",
        "what is deal tyui expiration date?",
        "what is client JHKL expiration date?",
        "what is deal tyui expiration date?",
        "what is client JHKL deal id?",
        "what is deal tyui client name?",
        "which is client JHKL's deal id?",
        "what is deal tyui volume?",
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






