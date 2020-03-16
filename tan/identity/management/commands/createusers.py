from datetime import datetime

from django.core.management.base import BaseCommand
from tan.identity.factories import fake, factory, IdentityFactory


class Command(BaseCommand):
    help = 'Create random users in the database'

    def add_arguments(self, parser):
        parser.add_argument(
            'number',
            type=int,
            help='Number of users to add'
        )

        parser.add_argument(
            '--random',
            action='store_true',
            help='Use a random seed',
        )

    def handle(self, *args, **options):
        if options['random']:
            fake.seed_instance(datetime.now())
        users = factory.create_batch(IdentityFactory, options['number'])
        if len(users) <= 10:
            for user in users:
                self.stdout.write(self.style.SUCCESS(f'Created user {user.identifier}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Created {len(users)} users'))
