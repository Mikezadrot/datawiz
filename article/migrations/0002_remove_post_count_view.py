# Generated by Django 3.1.7 on 2021-03-03 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='count_view',
        ),
    ]