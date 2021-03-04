# Generated by Django 3.1.7 on 2021-03-04 13:37

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20210303_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish')], default='draft', max_length=20),
        ),
    ]