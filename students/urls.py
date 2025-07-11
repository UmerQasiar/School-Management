from django.urls import path
from .views import StudentRegisterAPIView

urlpatterns = [
    path('register/', StudentRegisterAPIView.as_view(), name='student-register'),
]
