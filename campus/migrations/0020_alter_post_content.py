# Generated by Django 5.0 on 2023-12-31 18:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0019_rename_name_thread_thread_name_remove_thread_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
