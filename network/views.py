from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from network.models import Post, Comment
from network.permissions import IsAuthorPermission
from network.serializers import (
    PostSerializer,
    CommentSerializer,
    CommentCreateSerializer,
    PostCreateSerializer,
)


@extend_schema(tags=["post"])
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return PostCreateSerializer
        return PostSerializer

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        if self.action in ["retrieve", "list"]:
            return [permissions.AllowAny()]
        return [(permissions.IsAdminUser | IsAuthorPermission)()]


@extend_schema(tags=["comment"])
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CommentCreateSerializer
        return CommentSerializer

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        if self.action in ["retrieve", "list"]:
            return [permissions.AllowAny()]
        return [(permissions.IsAdminUser | IsAuthorPermission)()]
