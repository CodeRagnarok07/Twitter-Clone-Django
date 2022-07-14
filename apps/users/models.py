from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.

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

class User(AbstractBaseUser, PermissionsMixin):
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
		
	



class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE) 
	to_user = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'




