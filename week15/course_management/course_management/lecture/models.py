from django.db import models
from courses.models import Course

# Create your models here.


class Lecture(models.Model):
    name = models.TextField(max_length=100)
    week = models.TextField(max_length=10)
    url = models.TextField(max_length=1000)
    course = models.ForeignKey(Course, null=True)
