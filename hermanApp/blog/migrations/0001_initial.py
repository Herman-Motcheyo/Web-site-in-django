# Generated by Django 3.1.1 on 2020-09-29 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
    ]
