from django.urls import path
from.views import *
app_name = 'blog'

urlpatterns = [
    path('', index_view, name='index_blog'),
    path('category/<str:cat_name>', index_view, name='category'),
    path('author/<str:author_name>', index_view, name='author'),
    path('detail/<int:post_id>', detail_view, name='detail'),
    path('tag/<str:tag_name>', index_view, name='tag'),
    path('search/', blog_search, name='search'),

]