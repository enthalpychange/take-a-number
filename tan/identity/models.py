from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from tan.core.models import TimeStampedModel


class IdentityManager(BaseUserManager):

    def _create_identity(self, identifier, password=None, **kwargs):
        identifier = self.model.normalize_username(identifier)
        identity = self.model(identifier=identifier, **kwargs)
        identity.set_password(password)
        identity.save(using=self._db)
        return identity

    def create_user(self, identifier, password=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_identity(identifier, password, **kwargs)

    def create_superuser(self, identifier, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self._create_identity(identifier, password, **kwargs)


class Identity(AbstractBaseUser, PermissionsMixin):
    identifier = models.CharField(max_length=256, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'identities'

    objects = IdentityManager()

    USERNAME_FIELD = 'identifier'
    EMAIL_FIELD = 'identifier'
    REQUIRED_FIELDS = []


class Location(TimeStampedModel):
    name = models.CharField(max_length=256, unique=True, null=True)
    street = models.CharField(max_length=512, blank=True, verbose_name='Street Address')
    post_office_box = models.CharField(max_length=256, blank=True, verbose_name='PO Box')
    city = models.CharField(max_length=256, blank=True)
    state = models.CharField(max_length=256, blank=True, verbose_name='State/Province')
    country = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name


class UserProfile(TimeStampedModel):
    identifier = models.OneToOneField(Identity, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=256, blank=True)
    middle_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    office = models.CharField(max_length=256, blank=True)
    phone_number = models.CharField(max_length=256, blank=True)
    mobile_number = models.CharField(max_length=256, blank=True)
    title = models.CharField(max_length=256, blank=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])
