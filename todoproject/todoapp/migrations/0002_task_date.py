# Generated by Django 3.2.8 on 2021-11-12 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1996/11/27'),
            preserve_default=False,
        ),
    ]
