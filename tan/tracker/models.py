from django.contrib.auth.models import Group
from django.db import models
from django.urls import reverse


from tan.core.models import Process
from tan.identity.models import Identity


class Queue(models.Model):
    """Model for incident queues.
    """
    name = models.CharField(max_length=255)
    groups = models.ManyToManyField(Group)


class BaseIncident(Process):
    """Abstract base model for incidents.
    """
    owner = models.ForeignKey(
        Identity,
        null=True,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_owner',
        related_query_name='%(app_label)s_%(class)ss',
    )
    queue = models.ForeignKey(
        Queue,
        null=True,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_queue',
        related_query_name='%(app_label)s_%(class)ss',
    )
    resolution = models.TextField()
    resolved = models.DateTimeField(null=True, default=None)
    resolver = models.ForeignKey(
        Identity,
        null=True,
        on_delete=models.PROTECT,
        related_name='%(app_label)s_%(class)s_resolver',
        related_query_name='%(app_label)s_%(class)ss',
    )

    class Meta:
        abstract = True
        permissions = [
            ('can_work_incidents', 'Can work incidents'),
        ]


class Incident(BaseIncident):
    """Simple incident.
    """
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('tracker:incident-detail', kwargs={'pk': self.pk})
