from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


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
