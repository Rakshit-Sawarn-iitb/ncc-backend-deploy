from django.db import models

class Blog(models.Model):
    image = models.CharField(max_length=200)  
    title = models.CharField(max_length=200)
    display_content = models.TextField()  
    main_content = models.TextField()  
    likes = models.IntegerField(default=0) 