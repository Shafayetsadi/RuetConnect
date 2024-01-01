# Generated by Django 5.0 on 2023-12-25 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0008_alter_subscribed_thread_alter_subscribed_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscribed',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='subscribed',
            name='thread',
        ),
        migrations.RemoveField(
            model_name='subscribed',
            name='user',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='subscribers',
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='vote',
            name='post',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='voters',
        ),
        migrations.RemoveField(
            model_name='post',
            name='thread',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Subscribed',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
