# Generated by Django 3.0.7 on 2020-06-06 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0003_comment_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SingUp',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.AlterField(
            model_name='image',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pics.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
