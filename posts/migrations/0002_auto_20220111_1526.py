# Generated by Django 3.2.9 on 2022-01-11 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='category',
        ),
        migrations.AddField(
            model_name='posts',
            name='postPicture',
            field=models.ImageField(default='noimage.png', upload_to=''),
        ),
    ]
