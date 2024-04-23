from django import forms
from .models import Post
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Registration Form
class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

# Post Form
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ['author', 'created_on']

# Comment Form
