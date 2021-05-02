from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, first_name=None, last_name=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password, first_name=None, last_name=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Accounts(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    # @property
    # def is_admin(self):
    #     "Is the user a admin member?"
    #     return self.is_admin

    # @property
    # def is_active(self):
    #     "Is the user active?"
    #     return self.is_active
