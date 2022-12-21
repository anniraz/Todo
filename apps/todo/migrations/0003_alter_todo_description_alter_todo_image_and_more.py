# Generated by Django 4.1.4 on 2022-12-21 20:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0002_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='todo_img/'),
        ),
        migrations.AlterUniqueTogether(
            name='todo',
            unique_together={('user', 'title')},
        ),
    ]