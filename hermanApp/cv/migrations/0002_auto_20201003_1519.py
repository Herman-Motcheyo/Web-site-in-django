# Generated by Django 3.1.1 on 2020-10-03 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='decription',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='cv',
            name='image',
            field=models.FilePathField(path='cv/images'),
        ),
    ]
