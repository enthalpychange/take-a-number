from django.urls import path

from .views import (
    index,
    IncidentCreateView,
    IncidentDetailView,
)

app_name = 'tracker'

urlpatterns = [
    path('', index, name='index'),
    path('incidents/<int:pk>/', IncidentDetailView.as_view(), name='incident-detail'),
    path('incidents/create/', IncidentCreateView.as_view(), name='incident-create'),
]
