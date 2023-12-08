from django import forms
from django.forms import widgets

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class ArticleForm(forms.Form):
    status = forms.ChoiceField(required=True, label="Статус", choices=status_choices, initial='new', widget=forms.Select(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=200, required=True, label='Описание')
    detailed_description = forms.CharField(max_length=3000, required=True, label='Подробное описание', widget=widgets.Textarea())
    created_at = forms.DateField(label='Дата выполнения')
