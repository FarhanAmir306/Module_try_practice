# Generated by Django 4.2.7 on 2023-12-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_postmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/media/uploads/'),
        ),
    ]
