from django.db import models
from courses.models import Course

# Create your models here.


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(('password'), max_length=128)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    @classmethod
    def exists(cls, email):
        try:
            cls.objects.get(email=email)
            return True
        except cls.DoesNotExist:
            return False


class Student(User):
    course = models.ForeignKey(Course, null=True)


class Teacher(User):
    course = models.ForeignKey(Course, null=True)
