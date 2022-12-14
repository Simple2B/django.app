from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    CreatePost,
    PostDeleteView,
    PostUpdateView,
)


urlpatterns = [
    path("", PostListView.as_view(), name="posts_list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("create/", CreatePost.as_view(), name="create_post"),
    path("delete/<int:pk>", PostDeleteView.as_view(), name="delete_post"),
    path("update/<int:pk>", PostUpdateView.as_view(), name="update_post"),
]
