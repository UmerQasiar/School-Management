from django.urls import path
from teachers.views import TeacherRegisterAPIView

urlpatterns = [
    path('register/', TeacherRegisterAPIView.as_view(), name='teacher_register')
]
