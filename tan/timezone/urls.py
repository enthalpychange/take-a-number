from django.urls import path

from .views import set_timezone

urlpatterns = [
    path('', set_timezone, name='set-timezone'),
]
