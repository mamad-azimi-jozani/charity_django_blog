from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    date_hierarchy = "published_date"
    # exclude = ['title', 'content']
    list_display = ['title', 'status', 'published_date']
    list_filter = ['status']
    ordering = ['-created_date']
    search_fields = ['title', 'content']

