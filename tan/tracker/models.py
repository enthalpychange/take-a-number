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


class Incident(Process):
    """Incident model.
    """
    description = models.TextField()
    owner = models.ForeignKey(
        Identity,
        null=True,
        on_delete=models.PROTECT,
        related_name='owner_set',
        related_query_name='owner',
    )
    queue = models.ForeignKey(
        Queue,
        null=True,
        on_delete=models.PROTECT,
    )
    resolution = models.TextField()
    resolved = models.DateTimeField(null=True, default=None)
    resolver = models.ForeignKey(
        Identity,
        null=True,
        on_delete=models.PROTECT,
        related_name='resolver_set',
        related_query_name='resolver',
    )

    def get_absolute_url(self):
        return reverse('tracker:incident-detail', kwargs={'pk': self.pk})

    class Meta:
        permissions = [
            ('can_work_incidents', 'Can work incidents'),
        ]
