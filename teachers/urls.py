from django.urls import path
from teachers.views import TeacherRegisterAPIView, TeacherListAPIView

urlpatterns = [
    path('register/', TeacherRegisterAPIView.as_view(), name='teacher_register'),
    path('', TeacherListAPIView.as_view(), name='teacher_list')
]
