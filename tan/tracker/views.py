from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
)

from django.views.generic import (
    View,
)

from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView

from .forms import (
    IncidentCreateForm,
    QueueChangeForm,
    OwnerChangeForm,
    IncidentResolveForm,
)

from .models import (
    Incident,
)

from .selectors import (
    get_incident,
)

from .services import (
    update_incident_pre,
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
    paginate_by = 100

    def get_queryset(self):
        return get_incident()


class IncidentDetailView(LoginRequiredMixin, DetailView):
    model = Incident
    context_object_name = 'incident'

    def get_queryset(self):
        return get_incident()


class QueueChangeView(LoginRequiredMixin, BSModalUpdateView):
    model = Incident
    template_name = 'tracker/incident_change_queue_form.html'
    form_class = QueueChangeForm

    # Redirect back to incident when queue has changed
    def get_success_url(self):
        return reverse_lazy('tracker:incident-detail', kwargs={'pk': self.object.id})


class OwnerChangeView(LoginRequiredMixin, BSModalUpdateView):
    model = Incident
    template_name = 'tracker/incident_change_owner_form.html'
    form_class = OwnerChangeForm

    # Redirect back to incident when owner has changed
    def get_success_url(self):
        return reverse_lazy('tracker:incident-detail', kwargs={'pk': self.object.id})


class AssignSelfView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        incident = Incident.objects.filter(id=kwargs.get('pk'))
        incident.update(owner=self.request.user, status='AS')
        return redirect(reverse_lazy('tracker:incident-detail', kwargs=kwargs))


class ResolveView(LoginRequiredMixin, BSModalUpdateView):
    model = Incident
    template_name = 'tracker/incident_resolve_form.html'
    form_class = IncidentResolveForm

    # https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-editing/#models-and-request-user
    def form_valid(self, form):
        form.instance.resolver = self.request.user
        return super().form_valid(form)

    # Redirect back to incident when owner has changed
    def get_success_url(self):
        return reverse_lazy('tracker:incident-detail', kwargs={'pk': self.object.id})


class IncidentReopenView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        incident = Incident.objects.filter(id=kwargs.get('pk'))[0]
        incident.status = 'RO'
        update_incident_pre(incident=incident, changed_fields=['status']).save()
        return redirect(reverse_lazy('tracker:incident-detail', kwargs=kwargs))


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'tracker/index.html'
