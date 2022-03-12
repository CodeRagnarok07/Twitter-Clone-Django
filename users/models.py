from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(default='Hola, twitter', max_length=100)
	image = models.URLField(default='https://st.depositphotos.com/2218212/2938/i/450/depositphotos_29387653-stock-photo-facebook-profile.jpg')
	image_header = models.URLField(default='https://pbs.twimg.com/profile_banners/1371184742578720768/1647118044/1500x500')
	
	def __str__(self):
		return f'{self.user.username}'
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


class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE) 
	to_user = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'


class Post(models.Model):
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField()
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return self.content


