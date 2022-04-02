from django.db import models
from django.utils import timezone
from users.models import Profile
# Create your models here.



class Post(models.Model):
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField()
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return self.content