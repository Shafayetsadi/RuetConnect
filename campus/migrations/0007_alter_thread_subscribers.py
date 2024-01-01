# Generated by Django 5.0 on 2023-12-25 11:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0006_alter_post_thread'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='subscribers',
            field=models.ManyToManyField(null=True, related_name='subscribed_threads', through='campus.Subscribed', to=settings.AUTH_USER_MODEL),
        ),
    ]
