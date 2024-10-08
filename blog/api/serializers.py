"""
This module defines serializers for the blog application.

It includes two main serializer classes:
1. CommentSerializer: Handles serialization and deserialization of Comment objects.
2. PostSerializer: Handles serialization and deserialization of Post objects,
   including nested comments.

These serializers are used to convert complex data types, such as Django model
instances, into Python native datatypes that can then be easily rendered into
JSON, XML or other content types. They also provide deserialization, allowing
parsed data to be converted back into complex types after first validating the
incoming data.

The PostSerializer includes a custom update method to handle nested comment
updates and creations when updating a post.
"""

from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"

    def update(self, instance, validated_data):
        comments_data = validated_data.pop("comments", None)
        instance = super().update(instance, validated_data)

        if comments_data is not None:
            for comment_data in comments_data:
                comment_id = comment_data.get("id", None)
                if comment_id:
                    comment = Comment.objects.get(id=comment_id, post=instance)
                    for attr, value in comment_data.items():
                        setattr(comment, attr, value)
                    comment.save()
                else:
                    Comment.objects.create(post=instance, **comment_data)

        return instance
