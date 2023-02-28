from tokenize import blank_re
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=256)
    article = models.TextField()
    picture = models.ImageField(upload_to='blog_pictures', blank=True)

class Lesson(models.Model):
    name = models.CharField(max_length=256)
    website = models.URLField(unique=True)
    description = models.TextField()
    when_completed = models.DateField()

# Create your models here.
