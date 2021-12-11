from django.urls import path
from.views import *
app_name = 'blog'

urlpatterns = [
    path('', index_view, name='index_blog'),
    path('detail/<int:post_id>', detail_view, name='detail'),
    path('category/<str:cat_name>', category_view, name='category'),
]