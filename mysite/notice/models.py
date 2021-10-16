from django.db import models

class board(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    date = models.DateTimeField("date published")
