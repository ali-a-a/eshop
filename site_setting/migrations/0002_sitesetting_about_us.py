# Generated by Django 3.0.8 on 2020-09-15 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='about_us',
            field=models.TextField(blank=True, null=True),
        ),
    ]
