# Generated by Django 3.2.9 on 2022-01-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220121_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profilePicture',
            field=models.ImageField(default='noimage.png', null=True, upload_to=''),
        ),
    ]