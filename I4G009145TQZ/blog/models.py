from statistics import mode
from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField(null = True, blank = True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

