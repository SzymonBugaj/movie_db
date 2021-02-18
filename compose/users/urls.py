# Django
from django.urls import path

# Local
from .views import UserDetailView

urlpatterns = [
    path('profile/', UserDetailView.as_view(), name='profile'),
]
