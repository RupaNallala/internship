from django.db import models

# Create your models here.
class student(models.Model):
    stu_name=models.CharField(max_length=10)
    stu_id=models.IntegerField()
    stu_email=models.EmailField()
    stu_phone=models.IntegerField()
    stu_course=models.CharField()
    stu_year=models.IntegerField()
    stu_admission_date=models.DateField()
    stu_status=models.BooleanField(default=True)