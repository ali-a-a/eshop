# Generated by Django 3.0.8 on 2020-09-15 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
    ]
