from django.db import models



class Event(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.title
