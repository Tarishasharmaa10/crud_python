from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=25,blqnk=False,null=False)
    email=models.EmailField()
    age=models.IntegerField()
    name=models.CharField(max_length=25,blqnk=False,null=False)