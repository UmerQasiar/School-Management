from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    employee_id = models.CharField(max_length=100, blank=True)
    date_joined = models.DateField(blank=True)

    def __str__(self):
        return f"Teacher: {self.user.username}"
