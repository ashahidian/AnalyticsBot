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

# rule to fire to get volume value for given client
def on_match_volume_client(matcher, doc, i, matches):

    print("SELECT Volume FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities]"
          " WHERE Client = " + doc[2:3])


# rule to fire to get client name for given volume
def on_match_client_volume(matcher, doc, i, matches):
    print("SELECT Client FROM [CIA].[FileViz].[GCA_FX_Insight_RolloverOpportunities]"
          " WHERE Volume = " + doc[2:3])


def rules(question):
    matcher = Matcher(nlp.vocab)

    # alternative method is writing pattern
    # pattern = [{'case': "word"}, {'case': "word"}]
    # matcher.add("name", action(), pattern)

    matcher.add('volume_client', on_match_volume_client, [{'LOWER': 'volume'}, {'LOWER': 'client'}, {'POS': 'Noun'}])
    matcher.add('client_volume', on_match_client_volume, [{'LOWER': 'client'}, {'LOWER': 'volume'}, {'POS': 'Noun'}])

    doc = nlp(question)
    matches = matcher(doc)

    return matches
