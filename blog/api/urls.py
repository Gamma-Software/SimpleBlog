from django.urls import path
from .views import (
    PostListCreateAPIView,
    PostRetrieveUpdateDestroyAPIView,
    CommentListCreateAPIView,
    CommentRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("posts/", PostListCreateAPIView.as_view(), name="post-list"),
    path(
        "posts/<int:pk>/",
        PostRetrieveUpdateDestroyAPIView.as_view(),
        name="post-detail",
    ),
    path(
        "posts/<int:post_pk>/comments/",
        CommentListCreateAPIView.as_view(),
        name="comment-list",
    ),
    path(
        "posts/<int:post_pk>/comments/<int:pk>/",
        CommentRetrieveUpdateDestroyAPIView.as_view(),
        name="comment-detail",
    ),
]
