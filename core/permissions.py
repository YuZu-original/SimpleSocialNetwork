from rest_framework import permissions


class IsObjCurrentUserPermission(permissions.BasePermission):
    message = "This is not you"

    def has_object_permission(self, request, view, obj):
        return obj == request.user
