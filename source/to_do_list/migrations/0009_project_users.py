# Generated by Django 4.2.7 on 2024-01-09 02:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('to_do_list', '0008_rename_article_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи'),
        ),
    ]
