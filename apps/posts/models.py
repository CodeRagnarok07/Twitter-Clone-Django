from django.db import models
from django.utils import timezone
<<<<<<< HEAD
=======
from users.models import CustomUser
>>>>>>> 78e8157e87090d617eb91c9d38cd1e4995547a86
# Create your models here.

from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
	timestamp = models.DateTimeField(default=timezone.now)
<<<<<<< HEAD
	content = models.CharField(max_length=280)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
=======
	content = models.TextField()
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
>>>>>>> 78e8157e87090d617eb91c9d38cd1e4995547a86

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return self.content