# Generated by Django 3.2.9 on 2022-01-11 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='tags',
            field=models.CharField(default='tag', max_length=120),
        ),
    ]
