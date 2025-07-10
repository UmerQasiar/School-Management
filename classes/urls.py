from django.urls import path
from .views import ClassCreateAPIView

urlpatterns = [
    path('', ClassCreateAPIView.as_view(), name='class-create'),
]