from django.contrib.auth.models import Permission
from django.db.models import Q

from .models import Incident

from tan.identity.models import Identity


def get_incident():
    queryset = Incident.objects.all()
    queryset = queryset.select_related('creator')
    queryset = queryset.select_related('owner__userprofile')
    queryset = queryset.select_related('creator__userprofile__location')
    queryset = queryset.select_related('queue')
    return queryset


def get_workers():
    perm = Permission.objects.get(codename='work_incident')
    queryset = Identity.objects.filter(Q(groups__permissions=perm) | Q(user_permissions=perm))
    queryset = queryset.distinct()
    queryset = queryset.select_related('userprofile')
    queryset = queryset.order_by('userprofile__first_name')
    return queryset
