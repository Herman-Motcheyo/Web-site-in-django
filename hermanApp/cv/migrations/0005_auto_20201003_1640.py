# Generated by Django 3.1.1 on 2020-10-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_auto_20201003_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='image',
            field=models.FilePathField(path='/cv/images'),
        ),
    ]
