# Generated by Django 3.2.9 on 2022-01-19 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_comments_commentsthumbs'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='addedAt',
            field=models.DateTimeField(default='2001-12-01'),
        ),
    ]
