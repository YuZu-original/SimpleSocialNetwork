from django.urls import path
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path("users/login", views.LoginView.as_view()),
    path("users/update_password", views.UpdatePasswordView.as_view()),
] + router.urls
