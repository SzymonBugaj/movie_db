# Django
from django.urls import path

# Local
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]
