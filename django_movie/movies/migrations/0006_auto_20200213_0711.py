# Generated by Django 3.0.3 on 2020-02-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_movie_iframe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='iframe',
            field=models.CharField(max_length=400, null=True, verbose_name='Ссылки'),
        ),
    ]
