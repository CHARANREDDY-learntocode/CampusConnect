# Generated by Django 3.1.1 on 2020-09-19 23:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20200919_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_liked',
        ),
        migrations.AddField(
            model_name='post',
            name='is_liked',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]