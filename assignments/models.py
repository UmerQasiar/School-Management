from django.db import models
from classes.models import Class
from subjects.models import Subject
from teachers.models import Teacher

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='assignments')
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name='assignments')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='assignments')
    due_date = models.DateField()


    def __str__(self):
        return self.title
