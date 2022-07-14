from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
=======
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
>>>>>>> 78e8157e87090d617eb91c9d38cd1e4995547a86
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.utils import timezone

<<<<<<< HEAD
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
=======
class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
	username = None
	email = models.EmailField(_("email address"), unique=True)

	# user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	bio = models.CharField(default='Hola, twitter', max_length=100)
	image = models.URLField(default='https://st.depositphotos.com/2218212/2938/i/450/depositphotos_29387653-stock-photo-facebook-profile.jpg')
	image_header = models.URLField(default='https://pbs.twimg.com/profile_banners/1371184742578720768/1647118044/1500x500')
	
	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = []
	objects = CustomUserManager()


	def __str__(self):
		return f'{self.email}'
    # campos foraneos
    # user.posts

	# def following(self):
	# 	user_ids = Relationship.objects.filter(from_user=self.user)\
	# 								.values_list('to_user_id', flat=True)
	# 	return User.objects.filter(id__in=user_ids)

	# def followers(self):
	# 	user_ids = Relationship.objects.filter(to_user=self.user)\
	# 								.values_list('from_user_id', flat=True)
	# 	return User.objects.filter(id__in=user_ids)
		
	

>>>>>>> 78e8157e87090d617eb91c9d38cd1e4995547a86

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user

<<<<<<< HEAD
=======
class Relationship(models.Model):
	from_user = models.ForeignKey(CustomUser, related_name='following', on_delete=models.CASCADE) 
	to_user = models.ForeignKey(CustomUser, related_name='follower', on_delete=models.CASCADE)
>>>>>>> 78e8157e87090d617eb91c9d38cd1e4995547a86

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
