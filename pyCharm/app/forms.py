from django import forms


class QuestionInputForm(forms.Form):
    question_input = forms.CharField(label='Your question', help_text="Submit question", max_length=100)