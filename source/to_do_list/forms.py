from django import forms
from django.forms import widgets
from to_do_list.models import Status, Type



class ArticleForm(forms.Form):
    description = forms.CharField(max_length=255, label='Описание')
    detailed_description = forms.CharField(required=True, label='Детальное описание', widget=widgets.Textarea())
    status = forms.ModelMultipleChoiceField(queryset=Status.objects.all(), label='Статус', required=False)
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='Тип', required=False)