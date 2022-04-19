from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    firstName=models.CharField(max_length=255)
    lastName=models.CharField(max_length=255)
    notes=models.TextField()
    book=models.ManyToManyField(Book,related_name="Authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)