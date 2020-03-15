from django.contrib import admin

from .models import (
    Incident,
    Queue,
)


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    pass


@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    pass
