from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import User
from core.permissions import IsObjCurrentUserPermission
from core.serializers import CreateUserSerializer
from core.serializers import LoginUserSerializer
from core.serializers import UpdatePasswordSerializer
from core.serializers import UserSerializer


class LoginView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user=user)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == "create":
            return [permissions.AllowAny()]
        if self.action in ["list", "retrieve"]:
            return [(permissions.IsAdminUser | permissions.IsAuthenticated)()]
        if self.action in ["update", "partial_update"]:
            return [(permissions.IsAdminUser | (permissions.IsAuthenticated & IsObjCurrentUserPermission))()]
        return [permissions.IsAdminUser()]

    def perform_create(self, serializer):
        super().perform_create(serializer)
        login(
            self.request,
            user=serializer.user,
            backend="django.contrib.auth.backends.ModelBackend",
        )


class UpdatePasswordView(UpdateAPIView):
    model = User
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePasswordSerializer

    def get_object(self):
        return self.request.user
