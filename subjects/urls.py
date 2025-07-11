from django.urls import path
from .views import SubjectListCreateAPIView

urlpatterns = [
    path('', SubjectListCreateAPIView.as_view(), name='subject-list-create'),
]
