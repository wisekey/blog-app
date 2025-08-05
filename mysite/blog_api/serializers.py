from rest_framework import serializers
from typing import Any
from blog.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author", "title", "body", "created"]
