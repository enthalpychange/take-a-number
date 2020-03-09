# Generated by Django 3.0.3 on 2020-03-08 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('ended', models.DateTimeField(default=None, null=True)),
                ('status', models.CharField(choices=[('SM', 'Submitted'), ('AS', 'Assigned'), ('RS', 'Resolved'), ('CL', 'Closed'), ('RO', 'Reopened')], default='SM', max_length=2)),
                ('description', models.TextField()),
                ('resolution', models.TextField()),
                ('resolved', models.DateTimeField(default=None, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tracker_incident_creator', related_query_name='tracker_incidents', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tracker_incident_owner', related_query_name='tracker_incidents', to=settings.AUTH_USER_MODEL)),
                ('queue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tracker_incident_queue', related_query_name='tracker_incidents', to='tracker.Queue')),
                ('resolver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tracker_incident_resolver', related_query_name='tracker_incidents', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('can_work_incidents', 'Can work incidents')],
            },
        ),
    ]
