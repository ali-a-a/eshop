# Generated by Django 3.0.8 on 2020-09-14 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='link',
        ),
    ]
