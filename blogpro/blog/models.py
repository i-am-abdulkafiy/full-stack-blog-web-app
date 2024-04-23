from django.db import models
from django.contrib.auth.models import User

# Post Model
class Post(models.Model):
	title = models.CharField(max_length=255, unique=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	# image = models.ImageField(upload_to='media/media', null=True, blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title

# Comment Model
