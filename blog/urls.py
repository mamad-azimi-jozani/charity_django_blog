from django.urls import path
from.views import *
app_name = 'blog'

urlpatterns = [
    path('', index_view, name='index_blog'),
    path('category/<str:cat_name>', index_view, name='category'),
    path('detail/<int:post_id>', detail_view, name='detail'),
    
]