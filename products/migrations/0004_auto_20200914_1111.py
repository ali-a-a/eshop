# Generated by Django 3.0.8 on 2020-09-14 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productgallery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productgallery',
            old_name='titile',
            new_name='title',
        ),
    ]
