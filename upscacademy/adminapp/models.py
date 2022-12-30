from django.db import models

# Create your models here.


class UpscStudyMaterial(models.Model):
    material_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    subject_name = models.CharField(max_length=255)
    uploded_file = models.FileField(upload_to='materials/', null=True)
    uplode_photo = models.ImageField(upload_to='images/', null=True)
    Published_date = models.DateField(auto_now_add = True,null=True)
    updated_date = models.DateField(auto_now = True,null=True)

    class Meta:
        db_table = 'study_materials'

    def __str__(self):
        return self.title


class UpscInterviewVideos(models.Model):
    video_id = models.AutoField(primary_key=True)
    video_title=models.CharField(max_length=255)
    subject_name=models.CharField(max_length=255)
    uplode_video = models.FileField(upload_to='videos/',null=True)
    videos_image = models.ImageField(upload_to='images/', null=True)
    video_link = models.CharField(max_length=255,null=True)
    uplode_date = models.DateField(auto_now_add=True,null=True) 
    updated_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'upsc_videos'

    def  __str__(self):
        return self.video_title


class UpscMockTest(models.Model):
    mock_test_id = models.AutoField(primary_key=True)
    mock_test_title = models.CharField(max_length=255)
    mock_subject_name = models.CharField(max_length=255)
    uploded_file = models.FileField(upload_to='materials/', null=True)
    upload_image = models.ImageField(upload_to='images/', null=True)
    test_date = models.DateField(auto_now_add=True)
    test_updated = models.DateField(auto_now_add=True)
 

    class Meta:
        db_table = 'upsc_mock_test_papers'

    def __str__(self):
        return self.mock_test_title


