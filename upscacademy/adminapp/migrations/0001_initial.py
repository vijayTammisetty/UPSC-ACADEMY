# Generated by Django 4.1.2 on 2022-10-18 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UpscInterviewVideos',
            fields=[
                ('video_id', models.AutoField(primary_key=True, serialize=False)),
                ('video_title', models.CharField(max_length=255)),
                ('subject_name', models.CharField(max_length=255)),
                ('uplode_video', models.FileField(null=True, upload_to='videos/')),
                ('video_link', models.CharField(max_length=255, null=True)),
                ('uplode_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'upsc_videos',
            },
        ),
        migrations.CreateModel(
            name='UpscMockTest',
            fields=[
                ('mock_test_id', models.AutoField(primary_key=True, serialize=False)),
                ('mock_test_title', models.CharField(max_length=255)),
                ('mock_subject_name', models.CharField(max_length=255)),
                ('uploded_file', models.FileField(null=True, upload_to='materials/')),
                ('test_date', models.DateField(auto_now_add=True)),
                ('test_updated', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'upsc_mock_test_papers',
            },
        ),
        migrations.CreateModel(
            name='UpscStudyMaterial',
            fields=[
                ('material_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('subject_name', models.CharField(max_length=255)),
                ('uploded_file', models.FileField(null=True, upload_to='materials/')),
                ('uplode_photo', models.ImageField(null=True, upload_to='images/')),
                ('Published_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_date', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'study_materials',
            },
        ),
    ]
