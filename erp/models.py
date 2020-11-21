from django.db import models

# Create your models here.
class Attendence(models.Model):

    name=models.CharField(max_length=100)
    usn=models.CharField(max_length=30)
    semester=models.CharField(max_length=10)
    total_marks=models.IntegerField()
    obtained_marks=models.IntegerField()
