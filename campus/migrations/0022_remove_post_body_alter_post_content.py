# Generated by Django 5.0 on 2024-01-02 06:04

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0021_post_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(blank=True, null=True),
        ),
    ]
