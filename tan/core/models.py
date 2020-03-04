from django.db import models

from tan.identity.models import Identity


class TimeStampedModel(models.Model):
    """Abstract base class model for created and modified timestamps.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Process(TimeStampedModel):
    """Abstract base class model for processes.
    """
    class Statuses(models.TextChoices):
        SUBMITTED = 'SM', 'Submitted'
        ASSIGNED = 'AS', 'Assigned'
        RESOLVED = 'RS', 'Resolved'
        CLOSED = 'CL', 'Closed',
        REOPENED = 'RO', 'Reopened'

    name = models.CharField(max_length=255)
    creator = models.ForeignKey(
        Identity,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_creator',
        related_query_name='%(app_label)s_%(class)ss',
    )
    ended = models.DateTimeField(null=True, default=None)
    status = models.CharField(
        max_length=2,
        choices=Statuses.choices,
        default=Statuses.SUBMITTED,
    )

    class Meta:
        abstract = True
