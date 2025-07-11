
from django.urls import path
from .views import GradeListCreateAPIView

urlpatterns = [
    path('', GradeListCreateAPIView.as_view(), name='grade-list-create'),
]
