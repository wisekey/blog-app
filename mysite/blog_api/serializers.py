from rest_framework import serializers
from typing import Any
from blog.models import Comment


class CommentSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    body = serializers.CharField()

    def create(self, validated_date: dict[str, Any]) -> Comment:
        return Comment(**validated_date)

    def update(self, instance: Comment, validated_data: dict[str, Any]) -> Comment:
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.body == validated_data.get("body", instance.body)
        return instance
