from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.utils import timezone

from PIL import Image

class CustomUserManager(BaseUserManager):
    """The UserManager subclasses the BaseUserManager and overrides the methods create_user and create_superuser. These custom methods are needed because the default methods expect a username to be provided. The admin app and manage.py will call these methods."""

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(_("email address"), unique=True)

    bio = models.CharField(max_length=160, null=True, blank=True)
    img = models.ImageField(upload_to='uploads/', null=True, blank=True)
    header= models.ImageField(upload_to='uploads/', null=True, blank=True)


    is_staff = models.BooleanField(default=False) # required by the admin.
    is_superuser = models.BooleanField(default=False) # used by the PermissionsMixin to grant all permissions.
    is_active = models.BooleanField(default=True) # indicates whether the user is considered “active”.
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = 'email' # The name of the field that will be returned when get_email_field_name() is called on a User instance.
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.username}'
    
    "https://via.placeholder.com/240x180.jpg"


class Relationship(models.Model):
    from_user = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name='follower', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.from_user} to {self.to_user}'
