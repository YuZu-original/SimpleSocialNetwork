from datetime import datetime

from rest_framework import serializers

from network.models import Post, Comment
from utils.serializer_validators import NotContainWords
from utils.utils import calculate_age

POST_BAD_WORDS = ["ерунда", "глупость", "чепуха"]


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[NotContainWords(POST_BAD_WORDS)])

    class Meta:
        model = Post
        read_only_fields = ("id", "author", "comments", "created_at", "updated_at")
        fields = (
            "id",
            "title",
            "text",
            "image",
            "author",
            "comments",
            "created_at",
            "updated_at",
        )


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField(validators=[NotContainWords(POST_BAD_WORDS)])

    def validate_author(self, value):
        age = calculate_age(value.date_of_birth)
        if age < 18:
            raise serializers.ValidationError(
                "You're still young. The minimum age is 18 years."
            )
        return value

    class Meta:
        model = Post
        read_only_fields = ("id", "author", "created_at", "updated_at")
        fields = ("id", "title", "text", "image", "author", "created_at", "updated_at")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        read_only_fields = ("id", "author", "post", "created_at", "updated_at")
        fields = ("id", "text", "author", "post", "created_at", "updated_at")


class CommentCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        read_only_fields = ("id", "author", "created_at", "updated_at")
        fields = ("id", "text", "author", "post", "created_at", "updated_at")
