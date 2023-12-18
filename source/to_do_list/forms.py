from django import forms
from django.forms import widgets
from to_do_list.models import Status, Type, Article



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        field = ('description', 'detailed_description', 'status', 'type', 'created_at', 'updated_at')
        exclude = ('types',)
