# Generated by Django 4.0.3 on 2022-04-09 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0007_todolist_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='status',
        ),
    ]
