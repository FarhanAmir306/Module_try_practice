# Generated by Django 4.2.7 on 2023-12-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagorymodel',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]
