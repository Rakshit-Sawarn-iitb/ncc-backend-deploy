from django.db import models

# Create your models here.
class CouncilCard(models.Model):
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    photo = models.CharField(max_length=400)
    role = models.IntegerField(null=True, default=False)#0 for Head and 1 for secy
    year = models.IntegerField(null=True, default=False)#year they served in for 2024-25 year would be 2024
