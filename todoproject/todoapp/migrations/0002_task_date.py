# Generated by Django 3.2.4 on 2021-07-21 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2020-08-03'),
            preserve_default=False,
        ),
    ]
