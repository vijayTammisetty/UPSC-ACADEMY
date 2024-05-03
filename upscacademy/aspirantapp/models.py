from django.db import models

# Create your models here.

class AspirantsModel(models.Model):
    aspirant_id = models.AutoField(primary_key=True)
    full_Name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=50,null=True)
    phone_Number = models.BigIntegerField()
    profile = models.ImageField(upload_to='images/',null=True)
    state = models.CharField(max_length=255,null=True)
    country = models.CharField(max_length=255, null=True)
    education = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)
    pin_number = models.CharField(max_length=255)
    register_date = models.DateField(auto_now_add=True,null=True)
    status = models.CharField(max_length=20, default='Pending')

    class Meta:
        db_table = 'Aspirants_Details'
    


class AspirantFeadbackModel(models.Model):
    feadback_id = models.AutoField(primary_key=True)
    aspirant = models.ForeignKey(AspirantsModel, on_delete=models.CASCADE, null=True)
    feedback_message= models.TextField()
    feedback_sentiment=models.CharField(max_length=20)
    feedback_date=models.DateField(auto_now_add=True)
    rating1 = models.IntegerField(help_text='rating1', null=True)
    rating2 = models.IntegerField(help_text='rating2', null=True)
    rating3 = models.IntegerField(help_text='rating3', null=True)

    class Meta:
        db_table = 'aspirant_feadback'




