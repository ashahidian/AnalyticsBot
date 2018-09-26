# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from forms import QuestionInputForm

from management import pipeline


def dashboard_view(request):
    r = None
    if request.method == 'POST':
        form_q = QuestionInputForm(request.POST)

        # if question is valid, then clean, and pass to tokenizer file
        if form_q.is_valid():
            question_submitted = form_q.cleaned_data.get('question_input')
            r = pipeline.pipeline(question_submitted)
    else:
        form_q = QuestionInputForm()
    return render(request, 'dashboard.html', {'form': form_q, 'pipeline_result': r})