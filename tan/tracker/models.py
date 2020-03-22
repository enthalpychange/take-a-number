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

    def __str__(self):
        return self.name


class Incident(Process):
    """Incident model.
    """
    name = models.CharField(max_length=255, verbose_name='Subject')
    description = models.TextField(blank=True)
    owner = models.ForeignKey(
        Identity,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='owner_set',
        related_query_name='owner',
    )
    queue = models.ForeignKey(
        Queue,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )
    resolution = models.TextField(blank=True)
    resolved = models.DateTimeField(null=True, blank=True)
    resolver = models.ForeignKey(
        Identity,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='resolver_set',
        related_query_name='resolver',
    )

    def get_absolute_url(self):
        return reverse('tracker:incident-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ('work_incident', 'Can work incident'),
        ]
