from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
)

from bootstrap_modal_forms.generic import BSModalCreateView

from .forms import (
    IncidentCreateForm,
)

from .models import (
    Incident,
)


class IncidentCreateView(LoginRequiredMixin, BSModalCreateView):
    model = Incident
    form_class = IncidentCreateForm
    success_message = 'IT IS FINE'
    success_url = reverse_lazy('tracker:index')

    # https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-editing/#models-and-request-user
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class IncidentDetailView(LoginRequiredMixin, DetailView):
    model = Incident


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'tracker/index.html'
