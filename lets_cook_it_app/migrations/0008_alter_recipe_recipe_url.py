# Generated by Django 3.2.8 on 2021-10-15 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lets_cook_it_app', '0007_auto_20211015_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_url',
            field=models.URLField(null=True, unique=True),
        ),
    ]
