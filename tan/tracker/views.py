from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
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


class ModalContextMixin:
    """
    Default context mixin for modal forms to pass extra arguments to the
    template.
    """
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault('view', self)
        context.setdefault('modal_title', 'Update')
        context.setdefault('submit_button', 'Submit')
        context['debug_view'] = bool(self.request.GET.get('debug', False))
        if self.extra_context is not None:
            context.update(self.extra_context)
        return context


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


class QueueChangeView(LoginRequiredMixin, ModalContextMixin, BSModalUpdateView):
    model = Incident
    template_name = 'tracker/incident_detail_modal_form.html'
    form_class = QueueChangeForm
    extra_context = {
        'modal_title': 'Change Queue',
        'submit_button': 'Change',
    }

    # Redirect back to incident when queue has changed
    def get_success_url(self):
        return reverse_lazy('tracker:incident-detail', kwargs={'pk': self.object.id})


class OwnerChangeView(LoginRequiredMixin, ModalContextMixin, BSModalUpdateView):
    model = Incident
    template_name = 'tracker/incident_detail_modal_form.html'
    form_class = OwnerChangeForm
    extra_context = {
        'modal_title': 'Change Owner',
        'submit_button': 'Change',
    }

    # Redirect back to incident when owner has changed
    def get_success_url(self):
        return reverse_lazy('tracker:incident-detail', kwargs={'pk': self.object.id})


class AssignSelfView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        incident = Incident.objects.filter(id=kwargs.get('pk'))
        incident.update(owner=self.request.user, status='AS')
        return redirect(reverse_lazy('tracker:incident-detail', kwargs=kwargs))


class ResolveView(LoginRequiredMixin, ModalContextMixin, BSModalUpdateView):
    model = Incident
    template_name = 'tracker/incident_detail_modal_form.html'
    form_class = IncidentResolveForm
    extra_context = {
        'modal_title': 'Resolve Ticket',
        'submit_button': 'Resolve',
    }

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
