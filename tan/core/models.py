from django.db import models


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
        'identity.Identity',
        on_delete=models.PROTECT,
        related_name='creator_set',
        related_query_name='creator',
    )
    ended = models.DateTimeField(null=True, blank=True, default=None)
    status = models.CharField(
        max_length=2,
        choices=Statuses.choices,
        default=Statuses.SUBMITTED,
    )

    class Meta:
        abstract = True
