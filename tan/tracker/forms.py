from django.forms import Textarea

from bootstrap_modal_forms.forms import BSModalForm

from .models import Incident


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
