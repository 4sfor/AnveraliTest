# Generated by Django 5.0.4 on 2024-04-21 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(upload_to='avatars', verbose_name='Фото профиля'),
        ),
    ]
