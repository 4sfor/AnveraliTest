# Generated by Django 5.0.4 on 2024-04-22 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catuser',
            name='cat_user',
            field=models.CharField(max_length=15, verbose_name='Категория полльзователя'),
        ),
    ]