# Generated by Django 5.0 on 2023-12-26 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0015_thread_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='vote',
        ),
        migrations.AddField(
            model_name='vote',
            name='vote_type',
            field=models.IntegerField(default=0),
        ),
    ]
