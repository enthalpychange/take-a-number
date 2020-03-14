from django.urls import path

from .views import (
    IndexView,
    IncidentCreateView,
    IncidentDetailView,
)

app_name = 'tracker'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('incidents/<int:pk>/', IncidentDetailView.as_view(), name='incident-detail'),
    path('incidents/create/', IncidentCreateView.as_view(), name='incident-create'),
]
