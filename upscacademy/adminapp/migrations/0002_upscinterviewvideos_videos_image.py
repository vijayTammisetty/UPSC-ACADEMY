# Generated by Django 4.1.2 on 2022-10-24 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upscinterviewvideos',
            name='videos_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
