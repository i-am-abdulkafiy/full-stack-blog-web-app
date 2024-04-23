from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Owner)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	search_fields = ['title', 'author']
	list_display = ['title', 'created_on', 'author']
	list_filter = ['author', 'created_on']
