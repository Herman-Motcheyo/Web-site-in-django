# Generated by Django 3.1.1 on 2020-10-03 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20201003_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='image',
            field=models.FilePathField(),
        ),
    ]
