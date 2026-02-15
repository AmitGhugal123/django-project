from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):

    COURSE_CHOICES = [
        ('CS', 'Computer Science'),
        ('IT', 'Information Tech'),
        ('ME', 'Mechanical'),
        ('CE', 'Civil'),
    ]

    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=2, choices=COURSE_CHOICES)

    profile_pic = models.ImageField(upload_to='students/', blank=True, null=True)

    age = models.IntegerField()
    joined_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.course}"

