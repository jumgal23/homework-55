# Generated by Django 4.2.7 on 2023-12-26 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0007_project_article_project'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Task',
        ),
    ]
