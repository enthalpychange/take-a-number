from django.urls import path

from .views import (
    IndexView,
    IncidentCreateView,
    IncidentListView,
    IncidentDetailView,
)

app_name = 'tracker'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('incidents/<int:pk>/', IncidentDetailView.as_view(), name='incident-detail'),
    path('incidents/', IncidentListView.as_view(), name='incident-list'),
    path('incidents/create/', IncidentCreateView.as_view(), name='incident-create'),
]
