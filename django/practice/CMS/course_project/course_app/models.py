from django.db import models

# Create your models here.
class course(models.Model):
    course=models.CharField(max_length=100)
    duration=models.CharField()
    fee=models.CharField()
    trainer_name=models.CharField(max_length=100)
    mode_onlineoffline=models.CharField()
    start_date=models.DateField()
    noof_seats=models.CharField()
    course_status=models.CharField()