# Generated by Django 3.0.7 on 2020-06-08 09:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pics', '0008_auto_20200608_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='image',
            name='like',
        ),
        migrations.AddField(
            model_name='image',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]