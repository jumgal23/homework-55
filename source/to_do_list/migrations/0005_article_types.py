# Generated by Django 4.2.7 on 2023-12-15 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0004_alter_status_name_alter_type_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='types',
            field=models.ManyToManyField(blank=True, related_name='articles', to='to_do_list.type', verbose_name='Типы'),
        ),
    ]
