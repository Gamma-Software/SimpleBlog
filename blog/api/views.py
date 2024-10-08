"""
This module defines the API views for the blog application.

It includes several classes that handle CRUD operations for blog posts and comments:
1. PostListCreateAPIView: Lists all posts and creates new posts.
2. PostRetrieveUpdateDestroyAPIView: Retrieves, updates, and deletes individual posts.
3. CommentListCreateAPIView: Lists all comments for a post and creates new comments.
4. CommentRetrieveUpdateDestroyAPIView: Retrieves, updates, and deletes individual comments.

These views utilize Django REST Framework's generic views to provide a RESTful API
for managing blog posts and comments.
"""

from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# Create your views here.
class PostListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to list all posts or create a new post.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a post by id.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to list all comments or create a new comment.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        """
        This method is used to get the queryset of comments for a specific post.
        """
        return Comment.objects.filter(post_id=self.kwargs["post_pk"]).order_by(
            "-created_at"
        )

    def perform_create(self, serializer):
        """
        This method is used to set the post_id for a new comment.
        """
        post = get_object_or_404(Post, id=self.kwargs["post_pk"])
        serializer.save(post=post)


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a comment by id.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        """
        This method is used to get the queryset of comments for a specific post.
        """
        return Comment.objects.filter(post_id=self.kwargs["post_pk"])
