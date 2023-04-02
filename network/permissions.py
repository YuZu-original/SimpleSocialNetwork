from rest_framework import permissions


class IsAuthorPermission(permissions.BasePermission):
    message = "You are not author"

    def has_object_permission(self, request, view, obj):
        return bool(request.user and obj.author == request.user)
