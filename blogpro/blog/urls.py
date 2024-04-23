from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='home'),
	path('signup/', views.sign_up, name='signup'),
	path('new_post/', views.new_post, name='new'),
	path('post_edit/<int:pk>/', views.post_edit, name='edit'),
	path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
	path('delete/<int:pk>/', views.delete_post, name='delete'),
]