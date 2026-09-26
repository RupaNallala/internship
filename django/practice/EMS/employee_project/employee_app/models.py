from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_id=models.IntegerField(unique=True)
    emp_email=models.EmailField(max_length=100)
    emp_dep=models.CharField(max_length=100)
    emp_jobrole=models.CharField(max_length=100)
    emp_salary=models.IntegerField()
    emp_joindate=models.DateField()
    emp_woringstatus=models.BooleanField(default=True)
    