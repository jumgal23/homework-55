from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



class Type(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Типы')

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Статусы')

    def __str__(self):
        return self.name


class Project(models.Model):
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    users = models.ManyToManyField(User, blank=True, related_name='projects', verbose_name='Пользователи')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='created_projects')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('to_do_list:project_detail', kwargs={'pk': self.pk})


class Task(models.Model):
    description = models.CharField(max_length=255, verbose_name='Описание', validators=[MinLengthValidator(10)])
    detailed_description = models.TextField(blank=True, verbose_name='Детальное описание', validators=[MinLengthValidator(20)])
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Статус')
    type = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    types = models.ManyToManyField('to_do_list.Type', blank=True, related_name='articles', verbose_name='Типы')
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.SET_NULL, related_name='tasks',
                                verbose_name='Проект')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='created_tasks')

    def __str__(self):
        return f'{self.id}. {self.description}. {self.status}'

