# Generated by Django 3.0.7 on 2020-06-05 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pics', '0002_follower'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilephoto', models.ImageField(blank=True, upload_to='profile/')),
                ('name', models.CharField(max_length=30)),
                ('bio', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='No comments', max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photo_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pics.Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
