# Generated by Django 4.1.2 on 2022-10-20 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspirantapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aspirantfeadbackmodel',
            name='rating',
        ),
        migrations.AddField(
            model_name='aspirantfeadbackmodel',
            name='rating1',
            field=models.IntegerField(help_text='c', null=True),
        ),
    ]