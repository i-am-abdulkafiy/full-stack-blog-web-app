from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Post
from .forms import PostForm, RegistrationForm
from django.core.paginator import Paginator, EmptyPage,\
PageNotAnInteger
# Home View
@login_required(login_url='login')
def home(request):
	posts = Post.objects.all()
	paginator = Paginator(posts, 3)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'home.html', {'posts':posts, 'page':page})

# Sign Up
def sign_up(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('home')
	else:
		form = RegistrationForm()
	return render(request, 'registration/signup.html', {'form':form})

# Logout
def logout(request):
	logout(request)
	return redirect('home')

# New Post
@login_required(login_url='login')
def new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('home')
	else:
		form = PostForm()
	return render(request, 'blog/new_post.html', {'form':form})

# Post Detail
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/detail.html', {'post':post})

# Post Edit
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	form = PostForm(instance=post)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form = form.save()
			return redirect('home')
	return render(request, 'blog/update.html', {'form':form})

# Delete 
def delete_post(request, pk):
	posts = get_object_or_404(Post, pk=pk)
	posts = posts.delete()
	return redirect('home')
	
