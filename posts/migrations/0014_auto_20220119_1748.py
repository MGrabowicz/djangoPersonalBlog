# Generated by Django 3.2.9 on 2022-01-19 16:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0013_comments_addedat'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='likeCount',
            field=models.BigIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='comments',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
