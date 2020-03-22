from django.forms import Textarea

from bootstrap_modal_forms.forms import BSModalForm

from .fields import FirstAndLastNameChoiceField
from .models import Incident
from .selectors import get_workers
from .services import update_incident_pre


class IncidentCreateForm(BSModalForm):
    class Meta:
        model = Incident
        fields = [
            'name',
            'description',
        ]
        widgets = {
            'description': Textarea(attrs={'rows': 3})
        }

    def save(self, commit=True):
        incident = super().save(commit=commit)
        # Business logic on incident creation
        return incident


class QueueChangeForm(BSModalForm):
    class Meta:
        model = Incident
        fields = ['queue']

    def save(self, commit=True):
        self.instance = update_incident_pre(incident=self.instance, changed_fields=self.changed_data)
        incident = super().save(commit=commit)
        # Business logic when queue changes
        return incident


class OwnerChangeForm(BSModalForm):
    class Meta:
        model = Incident
        fields = ['owner']

    # Limit owner list to incident workers
    # Display first and last name of workers
    owner = FirstAndLastNameChoiceField(queryset=get_workers())

    def save(self, commit=True):
        self.instance = update_incident_pre(incident=self.instance, changed_fields=self.changed_data)
        incident = super().save(commit=commit)
        # Business logic when owner changes
        return incident


class IncidentResolveForm(BSModalForm):
    class Meta:
        model = Incident
        fields = ['resolution']

    def save(self, commit=True):
        self.instance = update_incident_pre(incident=self.instance, changed_fields=self.changed_data)
        incident = super().save(commit=commit)
        # Business logic when queue changes
        return incident
