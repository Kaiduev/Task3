# Generated by Django 3.0.3 on 2020-02-16 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_movieusers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MovieUsers',
        ),
    ]