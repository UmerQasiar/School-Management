from django.db import models
from students.models import Student
from teachers.models import Teacher

# Create your models here.
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='attendances')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late')
    ])

    def __str__(self):
        return f"{self.student.user.username} - {self.date} - {self.status}"
