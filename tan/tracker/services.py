from typing import List

from django.utils import timezone

from .models import Incident


def update_incident_pre(*,
                        incident: Incident = None,
                        changed_fields: List[str] = [],
                        ) -> Incident:

    # When queue is changed:
    # * status should be Enqueued
    # * owner should be blank
    if 'queue' in changed_fields:
        incident.status = 'EQ'
        incident.owner = None

    # When owner is assigned:
    # * status should be Assigned
    if 'owner' in changed_fields:
        incident.status = 'AS'

    # When incident is resolved:
    # * resolution datetime should be current datetime
    # * status should be Resolved
    if 'resolution' in changed_fields:
        incident.resolved = timezone.now()
        incident.status = 'RS'

    # When incident is reopened:
    # * append previous resolution to description
    # * clear resolution
    # * clear resolution datetime
    # * clear resolver
    if 'status' in changed_fields and incident.status == 'RO':
        resolution = f'Resolution by {incident.resolver} at {incident.resolved}:\n{incident.resolution}\n\n'
        incident.description = resolution + incident.description
        incident.resolution = ''
        incident.resolved = None
        incident.resolver = None

    return incident
