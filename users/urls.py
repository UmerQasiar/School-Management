from django.urls import path
from .views import CurrentUserAPIView, UserListAPIView

urlpatterns = [
    path('me/', CurrentUserAPIView.as_view(), name='current-user'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
]
