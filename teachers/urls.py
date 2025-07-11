from django.urls import path
from teachers.views import TeacherRegisterAPIView, TeacherListAPIView, TeacherClassesAPIView

urlpatterns = [
    path('register/', TeacherRegisterAPIView.as_view(), name='teacher_register'),
    path('', TeacherListAPIView.as_view(), name='teacher_list'),
    path('<int:id>/classes/', TeacherClassesAPIView.as_view(), name='teacher-classes')
]
