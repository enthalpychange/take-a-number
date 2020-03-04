from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
)

from .models import (
    Incident,
)


class IncidentCreateView(LoginRequiredMixin, CreateView):
    model = Incident
    fields = [
        'name',
        'description',
    ]

    # https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-editing/#models-and-request-user
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class IncidentDetailView(LoginRequiredMixin, DetailView):
    model = Incident


def index(request):
    return render(request, 'tracker/index.html')
