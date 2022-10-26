from enum import unique
from pyexpat import model
from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.TextField(max_length=200)
    slug = models.SlugField(unique=True)
    tags = models.TextField()
    image = models.FileField(upload_to="pic/")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-id',)
    
