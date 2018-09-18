# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from forms import QuestionInputForm

#class QuestionForm(forms.Form):
#    question = forms.CharField(max_length=100, required=True)

from processing.nlp_processing import tokenizing, stop_words, \
    spacy_tokenization, spacy_pos_tagging, spacy_ner


def dashboard_view(request):
    if request.method == 'POST':
        form_q = QuestionInputForm(request.POST)

        # if question is valid, then clean, and pass to tokenizer file
        if form_q.is_valid():
            question_submitted = form_q.cleaned_data.get('question_input')
            tokenized = tokenizing(question_submitted)
            pure_question = stop_words(question_submitted)
            spacy = spacy_tokenization(question_submitted)
            pos, html = spacy_pos_tagging(question_submitted)
            ner, ner_diagram = spacy_ner(question_submitted)
            return render(request, 'dashboard.html',
                          {'form': form_q, 'tokenized': tokenized,'pure_question': pure_question,
                           'spacy': spacy, 'pos': pos, 'ner': ner, 'html': html,
                           'ner_diagram': ner_diagram})

    else:
        form_q = QuestionInputForm()
    return render(request, 'dashboard.html', {'form': form_q})