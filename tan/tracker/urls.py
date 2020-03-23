from django.urls import path

from .views import (
    IndexView,
    IncidentCreateView,
    IncidentListView,
    IncidentDetailView,
    QueueChangeView,
    OwnerChangeView,
    AssignSelfView,
    ResolveView,
    IncidentReopenView,
)

app_name = 'tracker'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('incidents/<int:pk>/', IncidentDetailView.as_view(), name='incident-detail'),
    path('incidents/<int:pk>/change-queue/', QueueChangeView.as_view(), name='incident-change-queue'),
    path('incidents/<int:pk>/change-owner/', OwnerChangeView.as_view(), name='incident-change-owner'),
    path('incidents/<int:pk>/assign-self/', AssignSelfView.as_view(), name='incident-assign-self'),
    path('incidents/<int:pk>/resolve/', ResolveView.as_view(), name='incident-resolve'),
    path('incidents/<int:pk>/reopen/', IncidentReopenView.as_view(), name='incident-reopen'),
    path('incidents/', IncidentListView.as_view(), name='incident-list'),
    path('incidents/create/', IncidentCreateView.as_view(), name='incident-create'),
]
