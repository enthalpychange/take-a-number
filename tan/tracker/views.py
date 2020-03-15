from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
)

from bootstrap_modal_forms.generic import BSModalCreateView

from .forms import (
    IncidentCreateForm,
)

from .models import (
    Incident,
)

from .selectors import (
    get_incident,
)


class IncidentCreateView(LoginRequiredMixin, BSModalCreateView):
    model = Incident
    form_class = IncidentCreateForm
    success_message = 'Your ticket number is %(ticket_number)s. You will be contacted soon.'
    success_url = reverse_lazy('tracker:index')

    # https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-editing/#models-and-request-user
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    # Add ticket number to success message
    # https://docs.djangoproject.com/en/3.0/ref/contrib/messages/#adding-messages-in-class-based-views
    def get_success_message(self, cleaned_data):
        # Django calls this method twice. The first time self.object.id is None
        if self.object.id:
            incident_id = self.object.id
            # Pad with zeros
            return self.success_message % {'ticket_number': f'{incident_id:07}'}
        else:
            return 'Success!'


class IncidentListView(LoginRequiredMixin, ListView):
    model = Incident
    context_object_name = 'incidents'

    def get_queryset(self):
        return get_incident()


class IncidentDetailView(LoginRequiredMixin, DetailView):
    model = Incident
    context_object_name = 'incident'

    def get_queryset(self):
        return get_incident()


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'tracker/index.html'
