from datetime import datetime

from django.core.management.base import BaseCommand
from tan.tracker.factories import fake, factory, IncidentFactory


class Command(BaseCommand):
    help = 'Create random incidents in the database'

    def add_arguments(self, parser):
        parser.add_argument(
            'number',
            type=int,
            help='Number of incidents to add'
        )

        parser.add_argument(
            '--random',
            action='store_true',
            help='Use a random seed',
        )

    def handle(self, *args, **options):
        if options['random']:
            fake.seed_instance(datetime.now())
        incidents = factory.create_batch(IncidentFactory, options['number'])
        if len(incidents) <= 10:
            for incident in incidents:
                self.stdout.write(self.style.SUCCESS(f'Created incident {incident.id}: {incident.name}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Created {len(incidents)} incidents'))
