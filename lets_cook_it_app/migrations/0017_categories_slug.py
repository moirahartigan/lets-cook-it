# Generated by Django 3.2.8 on 2021-10-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lets_cook_it_app', '0016_alter_comment_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=True, max_length=220, null=True, unique=True),
        ),
    ]