from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 64)
    age = models.IntegerField()
    roll_no = models.IntegerField()
    addr = models.CharField(max_length = 64)
    phno = models.IntegerField()
    department = models.CharField(max_length = 64)