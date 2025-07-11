from django.urls import path
from .views import ClassCreateAPIView, ClassListAPIView

urlpatterns = [
    path('create/', ClassCreateAPIView.as_view(), name='class-create'),
    path('', ClassListAPIView.as_view(), name='class-list'),
]
