from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post, Category
# Register your models here.
@admin.register(Post)
class AdminPost(SummernoteModelAdmin):
    date_hierarchy = "published_date"
    # exclude = ['title', 'content']
    list_display = ['title', 'status', 'author', 'published_date']
    list_filter = ['status']
    ordering = ['-created_date']
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass