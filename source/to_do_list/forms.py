from django import forms
from django.forms import widgets
from to_do_list.models import Status, Type, Article, Project



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        field = ('description', 'detailed_description', 'status', 'type', 'created_at', 'updated_at')
        exclude = ('types',)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'start_date', 'end_date')


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')