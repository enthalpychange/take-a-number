import factory

from faker import Faker
from tan.identity.models import Identity
from tan.tracker.models import Incident

fake = Faker()
fake.seed_instance(1)
users = Identity.objects.all()


def generate_description(obj):
    """Generate p paragraphs with s sentences each.
    """
    s = fake.random_int(min=3, max=12)
    p = fake.random_int(min=1, max=5)
    return '\n'.join([fake.paragraph(nb_sentences=s, variable_nb_sentences=True) for n in range(p)])


def random_user(obj):
    return fake.random_element(users)


class IncidentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Incident

    name = factory.Faker('sentence', nb_words=12, variable_nb_words=True)
    description = factory.LazyAttribute(generate_description)
    creator = factory.LazyAttribute(random_user)