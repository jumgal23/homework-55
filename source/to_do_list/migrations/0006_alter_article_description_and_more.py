# Generated by Django 4.2.7 on 2023-12-18 22:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0005_article_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='detailed_description',
            field=models.TextField(blank=True, validators=[django.core.validators.MinLengthValidator(20)], verbose_name='Детальное описание'),
        ),
    ]
