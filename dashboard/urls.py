from django.urls import path
from .views import dashboard_view, set_timezone

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('timezone/', set_timezone, name='set_timezone'),  # Example of a timezone URL
]
