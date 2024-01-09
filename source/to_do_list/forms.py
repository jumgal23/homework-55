from django import forms
from django.forms import widgets
from to_do_list.models import Status, Type, Task, Project
from django.contrib.auth.models import User




class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        field = ('description', 'detailed_description', 'status', 'type', 'created_at', 'updated_at')
        exclude = ('types',)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'start_date', 'end_date')


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')


# class ProjectUserForm(forms.Form):
#     users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)


class ProjectUserForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Select Users'
    )

    class Meta:
        model = Project
        fields = []  # No need to include any fields from the Project model
