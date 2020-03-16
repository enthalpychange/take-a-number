import factory

from django.db.utils import IntegrityError
from faker import Faker
from tan.identity.models import Identity, Location, UserProfile

fake = Faker()
fake.seed_instance(1)
locations = Location.objects.all()


def generate_identifier(obj):
    """Generate a random identifier.

    Function is passed to LazyAttribute.
    """
    return f'{fake.first_name()}.{fake.last_name()}'.lower()


def generate_city(obj):
    """Generate a random city.

    Function is passed to LazyAttribute.
    """
    return fake.city()


class IdentityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Identity

    identifier = factory.LazyAttribute(generate_identifier)
    password = 'password'

    # Override _create to set password
    # https://factoryboy.readthedocs.io/en/latest/recipes.html#custom-manager-methods
    def _create(cls, *args, **kwargs):
        suffix = 0
        identifier = kwargs['identifier']
        password = kwargs['password']
        manager = Identity._default_manager

        # Handle name conflicts by adding a number
        # e.g. John.Doe, John.Doe.1, John.Doe.2
        while True:
            try:
                return manager.create_user(*args, identifier=identifier, password=password)
            except IntegrityError:
                suffix += 1
                identifier = kwargs['identifier'] + '.' + str(suffix)

    # Create user profile after creating user
    # https://factoryboy.readthedocs.io/en/latest/reference.html#factory.post_generation
    @factory.post_generation
    def create_profile(obj, create, extracted, **kwargs):
        class UserProfileFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = UserProfile

            title = fake.job()
            identifier = obj
            first_name = obj.identifier.split('.')[0].capitalize()
            last_name = obj.identifier.split('.')[1].capitalize()
            phone_number = fake.msisdn()
            mobile_number = fake.msisdn()
            location = fake.random_element(locations)

        UserProfileFactory()


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    name = factory.LazyAttribute(generate_city)
    street = fake.street_address()
    city = name
    state = fake.state_abbr(include_territories=False)
    country = 'United States'
    postal_code = fake.postalcode_in_state(state_abbr=state)
