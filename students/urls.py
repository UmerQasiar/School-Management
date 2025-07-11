from django.urls import path
from .views import StudentRegisterAPIView, StudentListAPIView

urlpatterns = [
    path('register/', StudentRegisterAPIView.as_view(), name='student-register'),
    path('', StudentListAPIView.as_view(), name='student-list'),
]
