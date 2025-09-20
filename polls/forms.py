from random import choice

from django import forms
from django.forms import inlineformset_factory
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

ChoiceFormSet = inlineformset_factory(Question, Choice, fields=['choice_text'], extra=5, can_delete=True)