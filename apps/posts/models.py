from django.db import models
from django.utils import timezone
# Create your models here.

from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.CharField(max_length=280)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return self.content