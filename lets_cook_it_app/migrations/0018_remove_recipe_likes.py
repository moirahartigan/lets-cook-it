# Generated by Django 3.2.8 on 2021-11-06 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lets_cook_it_app', '0017_categories_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='likes',
        ),
    ]
