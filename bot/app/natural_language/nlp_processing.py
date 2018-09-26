from nltk import *


def lowercase_words(question):
    return question.lower()
    # decode('utf-8').lower()


def tokenizing(question):
    return word_tokenize(question)


def stop_words(question):
    word_tokens = tokenizing(question)
    stop = ["in", "the", "to", "with", "than", "that", "of", "a", "an", "for",
            "is", "s", "are",
            "has", "have",
            "does", "do",
            "who", "when", "what", "which", "how",
            "give", "can", "show", "tell",
            "me", "you",
            "all", "present",
            "?", "!", ".", ";", ",", "'"]
    cleaned_question = []

    for w in word_tokens:
        if w not in stop:
            cleaned_question.append(str(w))

    return cleaned_question

