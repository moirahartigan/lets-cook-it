# Generated by Django 3.2.8 on 2021-10-27 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lets_cook_it_app', '0015_recipe_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
