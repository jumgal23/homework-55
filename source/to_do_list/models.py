from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class Article(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    created_at = models.DateField(null=True, blank=True, verbose_name='Дата выполнения')
    detailed_description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Подробное описание')
    status = models.CharField(max_length=50, null=False, blank=False, verbose_name="Статус", choices=status_choices, default='new')

    def __str__(self):
        return f'{self.id}. {self.description}. {self.status}'
