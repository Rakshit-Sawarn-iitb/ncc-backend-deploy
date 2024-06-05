from django.db import models

# Create your models here.
class alum(models.Model):
    firstName=models.CharField(null=False, blank=False, max_length=100)
    lastName=models.CharField(null=True, max_length=100)
    mobile=models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=300)
    gender = models.CharField(max_length=2)
    joiningDate = models.DateField()
    passingDate = models.DateField()
    achievments = models.CharField(max_length=500)
    present = models.CharField(max_length=200)
    branch = models.CharField(max_length=100)
    employment = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    work = models.CharField(max_length=200)