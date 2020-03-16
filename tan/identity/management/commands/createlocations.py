from datetime import datetime

from django.core.management.base import BaseCommand
from tan.identity.factories import fake, factory, LocationFactory


class Command(BaseCommand):
    help = 'Create random locations in the database'

    def add_arguments(self, parser):
        parser.add_argument(
            'number',
            type=int,
            help='Number of locations to add'
        )

        parser.add_argument(
            '--random',
            action='store_true',
            help='Use a random seed',
        )

    def handle(self, *args, **options):
        if options['random']:
            fake.seed_instance(datetime.now())
        locations = factory.create_batch(LocationFactory, options['number'])
        if len(locations) <= 10:
            for location in locations:
                self.stdout.write(self.style.SUCCESS(f'Created location {location.name}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Created {len(locations)} locations'))
