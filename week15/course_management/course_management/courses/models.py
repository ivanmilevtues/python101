from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def duration(self):
        return self.end_date - self.start_date
