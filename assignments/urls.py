from django.urls import path
from .views import AssignmentListCreateAPIView, AssignmentDetailAPIView

urlpatterns = [
    path('', AssignmentListCreateAPIView.as_view(), name='assignment-list-create'),
    path('<int:id>/', AssignmentDetailAPIView.as_view(), name='assignment-detail'),
]
