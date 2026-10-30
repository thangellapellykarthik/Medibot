from django.db import models

from django.utils import timezone
# import datetime
# Create your models here.

class UserDetailsModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(help_text='mechanic_name',max_length=100)
    user_email = models.CharField(help_text='mechanic_email',max_length=40)
    user_number = models.BigIntegerField(help_text='mechanic_number',null=True)
    user_password = models.CharField(help_text='mechanic_password',max_length=8)
    user_pic = models.FileField(upload_to='images',null=True)
    user_status = models.CharField(help_text='status',max_length=10,null=True,default='Pending')
    
    class Meta:
        db_table='user_details'
        
class FeedbackModel(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    comment = models.CharField(help_text='comment',max_length=200)
    sentiment = models.CharField(help_text='sentiment',max_length=100)
    user =  models.ForeignKey(UserDetailsModel,models.CASCADE,null=True)
    rating = models.IntegerField(help_text='rating',null=True)   
    
    class Meta:
        db_table='user_feedback'  
           
class MedibotviewedModel(models.Model):
    view_id = models.AutoField(primary_key=True)
    viewed = models.IntegerField(help_text='viewed',default=1)
    user = models.ForeignKey(UserDetailsModel,models.CASCADE,null=True)
    date = models.DateTimeField(auto_now=True)
    class Meta:
        db_table='user_search'
               
           
           
           