from nltk import *
import spacy
from spacy import displacy
from app.q_a.rules import rules


def tokenizing(question):
    return word_tokenize(question)


def stop_words(question):
    word_tokens = tokenizing(question)
    stop = ['in', 'the', 'to', 'with',
            'is', 'are',
            'has', 'have',
            'does', 'do',
            'currency', 'deal', 'client', 'last']
    pure_question = []

    for w in word_tokens:
        if w not in stop:
            pure_question.append(w)

    return pure_question


def wh_extraction(question):
    word_tokens = tokenizing(question)
    wh_words = ['which', 'what', 'who', 'when', 'where']
    wh = []

    for w in word_tokens:
        if w in wh_words:
            wh.append(w)
            # note: this procedure will not discriminate if more than one wh-word is present
            # if meant to only accept one wh-word, then the return should be here

    return wh


def spacy_tokenization(question):
    nlp = spacy.load('en')
    doc = nlp(question)

    tokens = []
    for token in doc:
        tokens.append(token.text)

    return tokens


def spacy_pos_tagging(question):
    # text_ original text
    # lemma_ base form
    # pos_ simple part of speech
    # tag_ detailed part of speech
    # dep_ syntactic dependency
    # shape_ capitalisation, punctuation, digits
    # is_alpha is it alpha
    # is_stop is it part of most common words

    nlp = spacy.load('en')
    doc = nlp(question)
    result = displacy.render(doc, style='dep')
    token_tags = []

    for token in doc:
        token_tags.extend((token.text, token.lemma_, token.pos_,
                           token.tag_, token.dep_))

    return token_tags, result


def spacy_ner(question):
    # text entity text
    # start_char starting index
    # end_char ending index
    # label entity label, type
    nlp = spacy.load('en')
    doc = nlp(question)
    graph = displacy.render(doc, style='ent')

    name_labels = []
    for ent in doc.ents:
        name_labels.extend((ent.text, ent.label_))

    rules(question)
    return name_labels, graph
