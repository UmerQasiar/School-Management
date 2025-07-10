from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    enrollment_number = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return f"Student: {self.user.username}"
