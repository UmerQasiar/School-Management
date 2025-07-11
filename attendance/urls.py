
from django.urls import path
from .views import AttendanceListCreateAPIView

urlpatterns = [
    path('', AttendanceListCreateAPIView.as_view(), name='attendance-list-create'),
]
