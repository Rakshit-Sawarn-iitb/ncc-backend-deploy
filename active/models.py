from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    cadet = models.CharField(max_length=100)
    username = models.CharField(null = True ,unique = True, blank = True , max_length = 25)
    def __str__(self):
        return self.username