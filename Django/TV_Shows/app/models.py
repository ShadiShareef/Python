from platform import release
from sys import maxsize
from turtle import title
from django.db import models

# Create your models here.
class moves(models.Model):
    title=models.CharField(max_length=100)
    network=models.CharField(max_length=100)
    releasedate=models.DateTimeField(max_length=100)
    description=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


