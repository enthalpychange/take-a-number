from django.urls import path

from .views import (
    IdentityLoginView,
)

app_name = 'identity'

urlpatterns = [
    path('login/', IdentityLoginView.as_view(), name='login')
]
