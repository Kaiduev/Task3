# Generated by Django 3.0.3 on 2020-02-13 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_videofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='iframe',
            field=models.CharField(max_length=200, null=True, verbose_name='Ссылки'),
        ),
    ]
