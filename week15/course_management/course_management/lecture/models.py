from django.db import models

# Create your models here.


class Lecture(models.Model):
    name = models.TextField(max_length=100)
    week = models.TextField(max_length=10)
    url = models.TextField(max_length=1000)
