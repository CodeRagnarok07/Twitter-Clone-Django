from django.utils.translation import gettext_lazy 
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""
    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)


    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class Profile(AbstractUser):
    username = None
    email = models.EmailField(gettext_lazy('email address'), unique=True)

    user_name = models.CharField(max_length=100, null=True, blank=True)
    profile_name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(default='Hola, twitter', max_length=100, null=True, blank=True)
    image = models.ImageField(default='default.png', null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # necesita de un manager que lo administre para crearlo con ciertos campos
    objects = CustomUserManager()

    def __str__(self):
        return f'Perfil de {self.user.email}'
    # campos foraneos
    # user.posts

    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user)\
            .values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)

    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user)\
            .values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)