from .models import Incident


def get_incident():
    queryset = Incident.objects.all()
    queryset = queryset.select_related('creator')
    queryset = queryset.select_related('creator__userprofile__location')
    queryset = queryset.select_related('queue')
    return queryset
