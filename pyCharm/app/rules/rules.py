import spacy


def metric_words(question_tokens):
    metrics = ['volume', 'cc', 'total cc']

    for w in question_tokens:
        if w in metrics:
            return True



#def rules(question):

 #   if metric_words() == True:


  #  return
