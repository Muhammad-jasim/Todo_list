# Generated by Django 4.0.3 on 2022-04-09 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_alter_todolist_item_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]
