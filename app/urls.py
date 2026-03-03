from django.urls import path
from .views import WeddingAPIView

urlpatterns = [
    path('wedding/', WeddingAPIView.as_view()),
    path('wedding/<int:pk>/', WeddingAPIView.as_view()),
]
