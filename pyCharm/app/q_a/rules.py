import spacy
from spacy.matcher import Matcher
from spacy.symbols import ORTH, LEMMA, POS, TAG

# FILE WITH RULES TO MATCH
nlp = spacy.load('en')


# tokens
# ORTH exact verbatim text of token
# LOWER lower case form of token
# LENGTH length of token text
# IS_ALPHA alphanumeric characters?
# IS_ASCII ascii characters?
# IS_DIGIT digits?
# IS_LOWER lowercase?
# IS_UPPER uppercase?
# IS_TITLE title?
# IS_PUNCT punctuation?
# IS_SPACE whitespace?
# IS_STOP stopword?
# LIKE_NUM resembles a number
# LIKE_URL resembles url
# LIKE_EMAIL resembles emal
# POS simple part-of-speech tagging
# TAG extended part-of-speech tagging
# DEP dependency label
# LEMMA lemma
# SHAPE shape
# ENT_TYPE the token's entity label

# on match for word "which"
def on_match_which(matcher, doc, i, matches):
    print("SELECT DEAL")


# on match for word "when"
def on_match_when(matcher, doc, i, matches):
    print("SELECT DATE")


def on_match_who(matcher, doc, i, matches):
    print("SELECT NAME")


def on_match_location(matcher, doc, i, matches):
    print (matcher, doc, i, matches)


def rules(question):
    matcher = Matcher(nlp.vocab)

    # alternative method is writing pattern
    # pattern = [{'case': "word"}, {'case': "word"}]
    # matcher.add("name", action(), pattern)
    matcher.add('which', on_match_which, [{ORTH: 'which'}, ])
    matcher.add('when', on_match_when, [{ORTH: 'when'}])
    # rule to match "what client x"
    matcher.add('what', on_match_which, [{ORTH: 'what'}, {ORTH: 'client'}, {POS: 'Noun'}])
    matcher.add('who', on_match_who, [{ORTH: 'who'}])
    # matcher.add('location', on_match_location, [{LEMMA: 'be'}, {TAG: 'GPE'}])

    doc = nlp(question)
    matches = matcher(doc)

    return matches
