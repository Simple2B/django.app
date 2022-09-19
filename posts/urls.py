from django.urls import path

from .views import *


urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('create/', CreatePost.as_view(), name='create_post'),
]
