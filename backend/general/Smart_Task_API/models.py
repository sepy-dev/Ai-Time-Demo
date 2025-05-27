# models.py
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
