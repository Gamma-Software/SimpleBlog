"""
This module defines the database models for the blog application.

It includes two main models:
1. Post: Represents a blog post with title, content, and timestamps.
2. Comment: Represents a comment on a blog post, linked to a specific post.

These models form the core data structure for the blog, allowing for the creation
and management of posts and their associated comments.
"""

from django.db import models


# Create your models here.
class Post(models.Model):
    """
    Model representing a blog post.
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """
        Returns a string representation of the post.
        """
        return str(self.title)


class Comment(models.Model):
    """
    Model representing a comment on a blog post.
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """
        Returns a string representation of the comment.
        """
        return f"{self.author} commented"
